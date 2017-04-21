from django.db import models


# Create your models here.

class Reminder(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    reminderTime = models.DateTimeField(default=timezone.now())
    createdTime = models.DateTimeField(auto_now_add=True)
    modifiedTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Reminder"
