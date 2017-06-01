from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Reminder.settings')

app = Celery('Reminder', backend='amqp', broker='amqp://')
app.config_from_object('Reminder.settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
