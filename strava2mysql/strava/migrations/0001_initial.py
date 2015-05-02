# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('profile_medium', models.CharField(max_length=200)),
                ('profile', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('friend', models.CharField(max_length=200)),
                ('follower', models.CharField(max_length=200)),
                ('premium', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('approve_followers', models.BooleanField()),
                ('follower_count', models.IntegerField()),
                ('friend_count', models.IntegerField()),
                ('mutual_friend_count', models.IntegerField()),
                ('date_preference', models.CharField(max_length=200)),
                ('measurement_preference', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('super_user', models.BooleanField()),
                ('biggest_ride_distance', models.FloatField()),
                ('biggest_climb_elevation_gain', models.FloatField()),
                ('email_language', models.CharField(max_length=200)),
                ('weight', models.FloatField()),
                ('max_heartrate', models.FloatField()),
                ('username', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('instagram_username', models.CharField(max_length=200)),
                ('offer_in_app_payment', models.BooleanField()),
                ('global_privacy', models.BooleanField()),
                ('receive_newsletter', models.BooleanField()),
                ('email_kom_lost', models.BooleanField()),
                ('dateofbirth', models.DateField()),
                ('facebook_sharing_enabled', models.BooleanField()),
                ('ftp', models.CharField(max_length=200)),
                ('profile_original', models.CharField(max_length=200)),
                ('premium_expiration_date', models.IntegerField()),
                ('email_send_follower_notices', models.BooleanField()),
                ('plan', models.CharField(max_length=200)),
                ('agreed_to_terms', models.CharField(max_length=200)),
                ('follower_request_count', models.IntegerField()),
                ('email_facebook_twitter_friend_joins', models.BooleanField()),
                ('receive_kudos_emails', models.BooleanField()),
                ('receive_follower_feed_emails', models.BooleanField()),
                ('receive_comment_emails', models.BooleanField()),
                ('sample_race_distance', models.IntegerField()),
                ('sample_race_time', models.IntegerField()),
            ],
        ),
    ]
