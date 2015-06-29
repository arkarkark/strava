# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0002_auto_20150628_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rando',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('n0', models.CharField(default=b'', max_length=200)),
                ('n1', models.CharField(default=b'', max_length=200)),
                ('n2', models.CharField(default=b'', max_length=200)),
                ('n3', models.CharField(default=b'', max_length=200)),
                ('n4', models.CharField(default=b'', max_length=200)),
                ('n5', models.CharField(default=b'', max_length=200)),
                ('n6', models.CharField(default=b'', max_length=200)),
                ('n7', models.CharField(default=b'', max_length=200)),
                ('n8', models.CharField(default=b'', max_length=200)),
                ('n9', models.CharField(default=b'', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='athlete',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 0, 36, 28, 262760, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 0, 36, 28, 262793, tzinfo=utc)),
        ),
    ]
