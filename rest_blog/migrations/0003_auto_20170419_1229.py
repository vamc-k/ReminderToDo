# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 12:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rest_blog', '0002_auto_20170419_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 12, 29, 45, 740856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='modifiedTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 12, 29, 45, 740886, tzinfo=utc)),
        ),
    ]
