# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 08:15
from __future__ import unicode_literals

import apps.send.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0003_auto_20171015_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='channels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('HousedSMS', apps.send.models.HousedSMS)], max_length=255), blank=True, null=True, size=None),
        ),
    ]
