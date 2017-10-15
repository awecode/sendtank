# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171013_1418'),
        ('tank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
        ),
    ]
