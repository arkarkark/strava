# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0003_auto_20150628_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 0, 59, 16, 802575, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 0, 59, 16, 802615, tzinfo=utc)),
        ),
    ]
