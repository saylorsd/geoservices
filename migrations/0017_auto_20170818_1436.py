# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-18 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoservices', '0016_auto_20170818_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcel',
            old_name='mapblocklo',
            new_name='mapblocklot',
        ),
    ]
