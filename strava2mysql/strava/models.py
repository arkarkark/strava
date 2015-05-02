"""Models for Strava."""

import pytz
import datetime

from django.db import models


# Create your models here.

class Athlete(models.Model):
  """An Athlete."""
  firstname = models.CharField(max_length=200, default="")
  lastname = models.CharField(max_length=200, default="")
  profile_medium = models.CharField(max_length=200, default="")
  profile = models.CharField(max_length=200, default="")
  city = models.CharField(max_length=200, default="")
  state = models.CharField(max_length=200, default="")
  country = models.CharField(max_length=200, default="")
  sex = models.CharField(max_length=200, default="")
  friend = models.CharField(max_length=200, default="")
  follower = models.CharField(max_length=200, default="")
  premium = models.BooleanField(default=False)

  created_at = models.DateTimeField(default=datetime.datetime.now(pytz.utc)) # auto_now_add=True, default="")
  updated_at = models.DateTimeField(default=datetime.datetime.now(pytz.utc)) # auto_now=True, default="")

  approve_followers = models.BooleanField(default=False)

  follower_count = models.IntegerField(default=-1)
  friend_count = models.IntegerField(default=-1)
  mutual_friend_count = models.IntegerField(default=-1)
  date_preference = models.CharField(max_length=200, default="")
  measurement_preference = models.CharField(max_length=200, default="")
  email = models.CharField(max_length=200, default="")

  super_user = models.BooleanField(default=False)
  biggest_ride_distance = models.FloatField(default=-1.0)
  biggest_climb_elevation_gain = models.FloatField(default=-1.0)

  email_language = models.CharField(max_length=200, default="")

  # A bunch more undocumented detailed-resolution attribs
  weight = models.FloatField(default=-1.0)
  max_heartrate = models.FloatField(default=-1.0)

  username = models.CharField(max_length=200, default="")
  description = models.CharField(max_length=200, default="")
  instagram_username = models.CharField(max_length=200, default="")

  offer_in_app_payment = models.BooleanField(default=False)
  global_privacy = models.BooleanField(default=False)
  receive_newsletter = models.BooleanField(default=False)
  email_kom_lost = models.BooleanField(default=False)
  dateofbirth = models.DateField(default=datetime.date(1970, 1, 1))
  facebook_sharing_enabled = models.BooleanField(default=False)
  ftp = models.CharField(max_length=200, default="")
  profile_original = models.CharField(max_length=200, default="")
  premium_expiration_date = models.IntegerField(default=-1)
  email_send_follower_notices = models.BooleanField(default=False)
  plan = models.CharField(max_length=200, default="")
  agreed_to_terms = models.CharField(max_length=200, default="")
  follower_request_count = models.IntegerField(default=-1)
  email_facebook_twitter_friend_joins = models.BooleanField(default=False)
  receive_kudos_emails = models.BooleanField(default=False)
  receive_follower_feed_emails = models.BooleanField(default=False)
  receive_comment_emails = models.BooleanField(default=False)

  sample_race_distance = models.IntegerField(default=-1)
  sample_race_time = models.IntegerField(default=-1)


  #  clubs = EntityCollection(Club, (DETAILED,, default="")) #: (detailed-only) Which clubs athlete belongs to. (:class:`list` of :class:`stravalib.model.Club`)
  #  bikes = EntityCollection(Bike, (DETAILED,)) #: (detailed-only) Which bikes this athlete owns. (:class:`list` of :class:`stravalib.model.Bike`)
  #  shoes = EntityCollection(Shoe, (DETAILED,)) #: (detailed-only) Which shoes this athlete owns. (:class:`list` of :class:`stravalib.model.Shoe`)
  #
  #  # Some undocumented summary & detailed  attributes
  #  ytd_run_totals = EntityAttribute(ActivityTotals, (SUMMARY, DETAILED)) #: (undocumented) Year-to-date totals for runs. (:class:`stravalib.model.ActivityTotals`)
  #  recent_run_totals = EntityAttribute(ActivityTotals, (SUMMARY, DETAILED)) #: (undocumented) Recent totals for runs. (:class:`stravalib.model.ActivityTotals`)
  #  all_run_totals = EntityAttribute(ActivityTotals, (SUMMARY, DETAILED)) #: (undocumented) All-time totals for runs. (:class:`stravalib.model.ActivityTotals`)
  #
  #  ytd_ride_totals = EntityAttribute(ActivityTotals, (SUMMARY, DETAILED)) #: (undocumented) Year-to-date totals for rides. (:class:`stravalib.model.ActivityTotals`)
  #  recent_ride_totals = EntityAttribute(ActivityTotals, (SUMMARY, DETAILED)) #: (undocumented) Recent totals for rides. (:class:`stravalib.model.ActivityTotals`)
  #  all_ride_totals = EntityAttribute(ActivityTotals, (SUMMARY, DETAILED)) #: (undocumented) All-time totals for rides. (:class:`stravalib.model.ActivityTotals`)
