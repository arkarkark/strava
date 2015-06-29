# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('strava', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='agreed_to_terms',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='approve_followers',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='biggest_climb_elevation_gain',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='biggest_ride_distance',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='city',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='country',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 0, 31, 35, 98586, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='date_preference',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='dateofbirth',
            field=models.DateField(default=datetime.date(1970, 1, 1)),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='description',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='email',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='email_facebook_twitter_friend_joins',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='email_kom_lost',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='email_language',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='email_send_follower_notices',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='facebook_sharing_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='firstname',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='follower',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='follower_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='follower_request_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='friend',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='friend_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='ftp',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='global_privacy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='instagram_username',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='lastname',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='max_heartrate',
            field=models.FloatField(default=-1.0),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='measurement_preference',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='mutual_friend_count',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='offer_in_app_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='plan',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='premium_expiration_date',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='profile',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='profile_medium',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='profile_original',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='receive_comment_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='receive_follower_feed_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='receive_kudos_emails',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='receive_newsletter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='sample_race_distance',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='sample_race_time',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='sex',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='state',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='super_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 0, 31, 35, 98721, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='username',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='weight',
            field=models.FloatField(default=-1.0),
        ),
    ]
