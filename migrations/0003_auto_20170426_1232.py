# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-26 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoservices', '0002_pghhood_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geocategory',
            name='id',
            field=models.CharField(max_length=60, primary_key=True, serialize=False),
        ),
    ]
