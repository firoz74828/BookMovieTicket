# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 09:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_auto_20180420_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 4, 25, 14, 55, 34, 215000)),
        ),
    ]
