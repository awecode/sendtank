# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0002_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tank.List'),
        ),
    ]