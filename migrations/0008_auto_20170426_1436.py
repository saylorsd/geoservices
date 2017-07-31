# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-26 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoservices', '0007_auto_20170426_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='acmunicipality',
            name='muni_type',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='acmunicipality',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='geoservices.RegionType'),
        ),
    ]
