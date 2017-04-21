from django.db import models


# Create your models here.
from django.utils import timezone


class Reminder(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    reminder_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Reminder"
