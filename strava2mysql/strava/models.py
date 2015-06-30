"""Models for Strava."""

import datetime
import inspect
import sys

from django.utils import timezone
timezone.now()

import django
import django.db
import django.db.models
import stravalib

# from south.modelsinspector import add_introspection_rules

class BigAutoField(django.db.models.fields.AutoField):
  """Auto incrementing big field."""
  def db_type(self, connection):
    if 'mysql' in connection.__class__.__module__:
      return 'bigint AUTO_INCREMENT'
    return super(BigAutoField, self).db_type(connection)

# add_introspection_rules([], ["^MYAPP\.fields\.BigAutoField"])



THISMODULE = sys.modules[__name__]

model_deps = {}
model_props = {}

def MakeModel(name, model_class):
  "Turn a strava model class into a django model class."
  print "Making model: %s" % name
  model_deps[name] = []
  props = {
    "__module__": __name__,
    "id": BigAutoField(primary_key=True),
  }
  for key in dir(model_class):
    if not hasattr(model_class, key):
      continue
    value = getattr(model_class, key)
    if key == 'id':
      key = "%s_id" % name
    if isinstance(value, stravalib.attributes.Attribute):
      type_to_django = {
        unicode: django.db.models.CharField(max_length=200, default="", null=True),
        int: django.db.models.BigIntegerField(null=True),
        float: django.db.models.FloatField(null=True),
        bool: django.db.models.NullBooleanField(),
        datetime.datetime: django.db.models.DateTimeField(default=django.utils.timezone.now, null=True),
        datetime.date: django.db.models.DateField(default=django.utils.timezone.now, null=True),
        datetime.timedelta: django.db.models.DurationField(null=True),
      }

      if value.type in type_to_django:
        props[key] = type_to_django[value.type]
      elif isinstance(value, stravalib.attributes.EntityCollection):
        if name == "BaseEffort" or key == "achievements":
          print "Skipping", name, key
          continue # WTF
        model_deps[name].append(value.type.__name__)
      elif isinstance(value, stravalib.attributes.EntityAttribute):
        props["%s_id" % key] = django.db.models.IntegerField(null=True)
      elif isinstance(value, stravalib.attributes.EntityCollection):
        pass
      elif inspect.isclass(value.type) and issubclass(value.type, stravalib.model.ActivityTotals):
        pass
      else:
        # print "UNKNOWN ATTRIBUTE TYPE: %s: %r" %(key, value.type)
        pass
    else:
      # print "Unknown type:", name, key, value
      pass
  model_props[name] = props

def MakeModelsFromModule(mod):
  "Look at all the things in module mod and turn LoadableEntities into django models."
  for name, value in mod.__dict__.items():
    if inspect.isclass(value) and issubclass(value, stravalib.model.LoadableEntity):
      MakeModel(name, value)
  # clean out deps
  for name, deps in model_deps.items():
    # print "Before", name, deps
    model_deps[name] = [x for x in deps if x in model_props]
    # print "After", name, model_deps[name]

  while len(model_props) > 0:
    clean_deps = {}
    for k, v in model_deps.items():
      if len(v) > 0:
        clean_deps[k] = v
    #  print ""
    #  print "len(model_props)", len(model_props)
    #  print clean_deps
    #  print model_props.keys()

    old_model_props = model_props.copy()
    for name, props in old_model_props.items():
      if len(model_deps[name]) == 0:
        print "Really making", name
        new_type = type(name, (django.db.models.Model,), props)
        setattr(THISMODULE, name, new_type)
        # remove this from all the model_deps now we've made it.
        for dep_name, deps in model_deps.items():
          if name in deps:
            print "Adding ForeignKey", name, " to ", dep_name
            model_props[dep_name][name.lower()] = django.db.models.ForeignKey(new_type, null=True)
            deps.remove(name)
        del model_props[name]

MakeModelsFromModule(stravalib.model)
