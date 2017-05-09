from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Reminder(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    reminder_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='reminders')
    highlighted = models.TextField()

    class Meta:
        db_table = "Reminder"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
