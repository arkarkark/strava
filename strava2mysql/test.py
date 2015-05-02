#!/usr/bin/python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "strava2mysql.settings")

from strava import models

if __name__ == "__main__":

  athlete = models.Athlete()
  athlete.firstname = "Fish"
  athlete.lastname = "Sticks"
  athlete.save()
  print athlete
