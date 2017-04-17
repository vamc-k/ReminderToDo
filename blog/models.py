from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class Reminder(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    reminderTime = models.DateTimeField()
    createdTime = models.DateTimeField(default=datetime.now())
    modifiedTime = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "Reminder"
