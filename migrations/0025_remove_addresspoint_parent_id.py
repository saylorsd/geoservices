# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-29 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoservices', '0024_auto_20170829_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresspoint',
            name='parent_id',
        ),
    ]
