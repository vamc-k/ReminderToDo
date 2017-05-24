# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170424_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='email_id',
            field=models.EmailField(default=datetime.datetime(2017, 5, 23, 12, 53, 51, 680120, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reminder',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]
