# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
                ('reminder_time', models.DateTimeField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Reminder',
            },
        ),
    ]
