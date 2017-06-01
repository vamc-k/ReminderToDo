from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

from Reminder.celery import app
from blog.models import Reminder


@app.task(name='send_mail')
def send_mail_task(pk):
    reminder = Reminder.objects.get(pk=pk)
    user = User.objects.get(username=reminder.owner)
    send_mail(reminder.title, reminder.message, settings.EMAIL_HOST_USER,
              [user.email], fail_silently=False)
