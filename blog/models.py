from django.db import models
from django.utils import timezone


# Create your models here.

class Reminder(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    reminderTime = models.DateTimeField()
    createdTime = models.DateTimeField(default=timezone.now())
    modifiedTime = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = "Reminder"
