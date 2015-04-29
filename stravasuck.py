#!/usr/bin/python

import logging
import os
import subprocess
import BaseHTTPServer
import urlparse

import stravalib


logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)

log = logging.getLogger("stravasuck")  # pylint: disable=invalid-name
log.setLevel(logging.DEBUG)

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
  StravaAuthenticate(MakeAllActivitiesPrivate)


if __name__ == '__main__':
  Main()
