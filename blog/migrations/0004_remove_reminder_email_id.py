# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170523_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='email_id',
        ),
    ]
