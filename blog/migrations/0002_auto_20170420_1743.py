# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='reminderTime',
            new_name='reminder_time',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='createdTime',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='modifiedTime',
        ),
        migrations.AddField(
            model_name='reminder',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 4, 20, 12, 13, 2, 192499, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reminder',
            name='modified_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 20, 12, 13, 16, 844829, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
