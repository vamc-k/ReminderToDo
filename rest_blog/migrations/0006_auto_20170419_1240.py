# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 12:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rest_blog', '0005_auto_20170419_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 12, 40, 41, 382308, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='modifiedTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 19, 12, 40, 41, 382338, tzinfo=utc)),
        ),
    ]