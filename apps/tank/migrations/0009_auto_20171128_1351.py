# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 13:51
from __future__ import unicode_literals

import apps.send.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0008_auto_20171128_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='channels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('HousedSMS', apps.send.models.HousedSMS)], max_length=255), blank=True, default=['HousedSMS'], null=True, size=None),
        ),
    ]
