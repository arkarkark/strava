# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0010_auto_20150630_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='best_efforts_id',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='segment_efforts_id',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='splits_metric_id',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='splits_standard_id',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='bikes_id',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='clubs_id',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='shoes_id',
        ),
        migrations.RemoveField(
            model_name='baseactivityzone',
            name='distribution_buckets_id',
        ),
        migrations.RemoveField(
            model_name='baseeffort',
            name='achievements_id',
        ),
        migrations.AddField(
            model_name='activity',
            name='besteffort',
            field=models.ForeignKey(to='strava.BestEffort', null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='segmenteffort',
            field=models.ForeignKey(to='strava.SegmentEffort', null=True),
        ),
        migrations.AddField(
            model_name='athlete',
            name='club',
            field=models.ForeignKey(to='strava.Club', null=True),
        ),
    ]
