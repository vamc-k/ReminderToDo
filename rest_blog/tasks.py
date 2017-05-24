from __future__ import absolute_import, unicode_literals

import os
from os import name

from celery import Celery
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
# set the default Django settings module for the 'celery' program.
from celery.task import periodic_task

from blog.models import Reminder

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Reminder.settings')

app = Celery('Reminder', backend='amqp', broker='amqp://')
app.config_from_object('Reminder.settings')


@app.task(name='sample_task')
def task1(x, y):
    print('task is running...!')
    return x+2+y


@app.task(name='send_mail')
def send_mail_task(pk):
    result = ''
    print('send mail sechduled...')
    reminder = Reminder.objects.get(pk=pk)
    user = User.objects.get(username=reminder.owner)
    result = send_mail(reminder.title, reminder.message, settings.EMAIL_HOST_USER,
              [user.email], fail_silently=False)
    if result>0:
        print('send mail successfully to '+user.email+' for reminder-'+pk)
        result = 'send mail successfully to '+user.email+' for reminder-'+pk
    else:
        result = 'Failed to send mail.'
    return result
