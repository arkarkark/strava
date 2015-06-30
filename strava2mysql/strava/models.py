"""Models for Strava."""

import datetime
import inspect
import sys

import django
import django.db
import django.db.models
import stravalib

THISMODULE = sys.modules[__name__]

def MakeModel(name, model_class):
  "Turn a strava model class into a django model class."
  print "Making model: %s" % name
  props = {"__module__": __name__}
  for key, value in model_class.__dict__.items():
    if key == 'id':
      key = "%s_id" % name
    if isinstance(value, stravalib.attributes.Attribute):
      type_to_django = {
        unicode: django.db.models.CharField(max_length=200, default="", null=True),
        int: django.db.models.IntegerField(null=True),
        float: django.db.models.FloatField(null=True),
        bool: django.db.models.NullBooleanField(),
        datetime.datetime: django.db.models.DateTimeField(default=django.utils.timezone.now, null=True),
        datetime.date: django.db.models.DateField(default=django.utils.timezone.now, null=True),
        datetime.timedelta: django.db.models.DurationField(null=True),
      }

      if value.type in type_to_django:
        props[key] = type_to_django[value.type]
      elif isinstance(value, stravalib.attributes.EntityCollection):
        pass
      elif inspect.isclass(value.type) and issubclass(value.type, stravalib.model.ActivityTotals):
        pass
      else:
        print "UNKNOWN ATTRIBUTE TYPE: %s: %r" %(key, value.type)
  setattr(THISMODULE, name, type(name, (django.db.models.Model,), props))

def MakeModelsFromModule(mod):
  "Look at all the things in module mod and turn LoadableEntities into django models."
  for name, value in mod.__dict__.items():
    if inspect.isclass(value) and issubclass(value, stravalib.model.LoadableEntity):
      MakeModel(name, value)

MakeModelsFromModule(stravalib.model)
