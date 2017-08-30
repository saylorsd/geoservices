# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-28 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoservices', '0018_auto_20170818_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchGeocodeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='geoservice/')),
                ('address_field', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GeocodeSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_string', models.CharField(max_length=200)),
                ('result_pin', models.CharField(max_length=16)),
            ],
        ),
    ]
