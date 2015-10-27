#!/usr/bin/python

import datetime
import logging
import os
import subprocess
import BaseHTTPServer
import urlparse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "strava2mysql.settings")

from tqdm import tqdm

from django.utils import timezone
from django.db.transaction import atomic
timezone.now()

import stravalib
import strava.models

import django
django.setup()

def Exists(src):
  src_type = src.__class__.__name__
  return ExistsByTypeAndId(src_type, src.id)

def ExistsByTypeAndId(src_type, id):
  db_class = getattr(strava.models, src_type)
  db_items = db_class.objects.filter(id=id)
  return len(db_items) > 0

IGNORED_MODEL_TYPES = ["SegmentEfforAchievement"]

def UpdateModel(src):
  src_type = src.__class__.__name__
  if not hasattr(strava.models, src_type):
    if src_type not in IGNORED_MODEL_TYPES:
      log.error("Unknown model type: %r", src_type)
    return
  db_class = getattr(strava.models, src_type)
  db_items = db_class.objects.filter(id=src.id)
  if len(db_items) > 0:
    log.debug("Found existsing %s: %r", src_type, src.id)
    db_obj = db_items[0]
  else:
    log.debug("Making new %s: %r", src_type, src.id)
    db_obj = db_class(id=src.id)
  for key in dir(src):
    if key in db_obj.__dict__:
      value = getattr(src, key)
      if type(value) == datetime.timedelta:
        value = value.seconds
      # log.debug("Setting %r to %r", key, value)
      setattr(db_obj, key, value)
    else:
      id_key = "%s_id" % key
      if id_key in db_obj.__dict__:
        value = getattr(src, key)
        if value is None or not hasattr(value, "id"):
          continue
        value = value.id
        try:
          # activity.map_id is something crazy like "a7467474" same with gear too.
          value = int(value)
          # log.debug("Setting ID %r to %r", key, value)
          setattr(db_obj, id_key, value)
        except:
          pass
  log.debug("Saving %s %d", src_type, db_obj.id)
  db_obj.save()
  # now update any list items in here
  for key in dir(src):
    if not hasattr(src, key):
      # log.info("Ignoring not hasattr %r", key)
      continue
    value = getattr(src, key)
    if type(value) == list:
      log.debug("Updating list: %r", key)
      for item in value:
        UpdateModel(item)

def UpdateItems(items):
  count = 0
  for item in tqdm(items):
    UpdateModel(item)
    count += 1
    if False and count > 0:
      break

def dump(obj):
  for key in dir(obj):
    print "dump", key, getattr(obj, key)

def LoadStream(client, activity_id):
  stream_types = ['time', 'latlng', 'altitude', 'distance', 'velocity_smooth', 'grade_smooth']
  streams = client.get_activity_streams(activity_id, stream_types, resolution='medium')

  db_items = strava.models.ActivityStream.objects.filter(activity_id=activity_id)
  if len(db_items) > 0:
    log.info("ActivityStream for activity_id %d already exists", activity_id)
    # return # TODO(ark): unless --force
    activity_stream_obj = db_items[0]
  else:
    activity_stream_obj = strava.models.ActivityStream(activity_id=activity_id)
    activity_stream_obj.save()

  UpdateActivityStreamData(activity_stream_obj.id, streams, stream_types)

@atomic
def UpdateActivityStreamData(activity_stream_id, streams, stream_types):

  strava.models.ActivityStreamDataPoint.objects.filter(activity_stream_id=activity_stream_id).delete()

  data_length = None
  for stream_type in stream_types:
    if stream_type in streams:
      if data_length is None:
        data_length = len(streams[stream_type].data)
      else:
        assert(data_length == len(streams[stream_type].data))

  log.info("Loading ActivityStream (%d data points)", data_length)

  for index in tqdm(range(0, data_length)):
    activity_stream_data_point_obj = strava.models.ActivityStreamDataPoint(
      activity_stream_id=activity_stream_id
    )

    noattr = set()
    for key, stream in streams.items():
      if key == 'latlng':
        activity_stream_data_point_obj.latitude = streams['latlng'].data[index][0]
        activity_stream_data_point_obj.longitude = streams['latlng'].data[index][1]
      else:
        if hasattr(activity_stream_data_point_obj, key):
          setattr(activity_stream_data_point_obj, key, streams[key].data[index])
        else:
          noattr.add(key)
    if noattr:
      log.info("Unknown keys from activity_stream_data_point: %r", noattr)
      return
    activity_stream_data_point_obj.save()

def Strava2Mysql(client):
  """Load data into a nysql database."""
  athlete = client.get_athlete()
  log.info("For Athlete %s %s %s", athlete.id, athlete.firstname, athlete.lastname)

  UpdateModel(athlete)

  UpdateItems(client.get_athlete_friends())
  UpdateItems(client.get_athlete_followers())

  count = 0
  for activity in client.get_activities():
    log.info("Looking at activity: %r %s", activity.id, activity.name)

    if not Exists(activity):
      activity = client.get_activity(activity.id)
      UpdateModel(activity)
      log.info("Loading Segments")
      for segment_effort in tqdm(activity.segment_efforts):
        if not ExistsByTypeAndId("Segment", segment_effort.segment.id):
          segment = client.get_segment(segment_effort.segment.id)
          UpdateModel(segment)
      LoadStream(client, activity.id)

def MakeAllActivitiesPrivate(client):
  """Called after all the authentication is done"""
  athlete = client.get_athlete()
  log.info("For Athlete %(id)s", {"id": athlete.id})
  activities = client.get_activities()
  for activity in activities:
    if not activity.private:
      log.info(activity)
      client.update_activity(activity.id, private=True)

ALL_DONE_WITH_HTTPD = False

def StravaAuthenticate(callback):
  """Get some strava access codes either from a file or via oauth type dance."""
  client = stravalib.client.Client()

  access_token = None

  if os.path.exists("access_token"):
    access_token = open("access_token").read().strip()

  if access_token:
    log.info("re using access token from disk")
    client.access_token = access_token
    callback(client)
  else:
    log.info("getting access token via web browser")

    client_id, secret = open("client.secret").read().strip().split(",")
    port = 1969

    url = "http://localhost:%d/authorized" % port

    authorize_url = client.authorization_url(client_id=client_id, redirect_uri=url, scope="view_private,write")
    log.info("Opening: %s", authorize_url)
    subprocess.call(["open", authorize_url])


    def UseCode(code):
      """Turn the code from the oauth dance into an access token, store it and call the callback."""
      access_token = client.exchange_code_for_token(client_id=client_id, client_secret=secret, code=code)
      client.access_token = access_token
      open("access_token", "w").write(access_token)
      callback(client)

    class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
      """Simple http server to do the oauth dance."""
      def do_GET(self):  # pylint: disable=invalid-name
        """handle a get reuqest method to parse out the code."""
        if self.path.startswith("/authorized"):
          self.wfile.write("<script>window.close();</script>")
          code = urlparse.parse_qs(urlparse.urlparse(self.path).query)["code"][0]
          global ALL_DONE_WITH_HTTPD  # pylint: disable=global-statement
          ALL_DONE_WITH_HTTPD = True
          UseCode(code)

    httpd = BaseHTTPServer.HTTPServer(("localhost", port), MyHandler)
    while not ALL_DONE_WITH_HTTPD:
      httpd.handle_request()

def Main():
  """Main."""
  StravaAuthenticate(Strava2Mysql)

logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)

log = logging.getLogger("stravasuck")  # pylint: disable=invalid-name
log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)


if __name__ == '__main__':
  Main()
