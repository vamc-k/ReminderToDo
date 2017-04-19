from rest_framework import serializers
from django.utils import timezone
from blog.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'title', 'message', 'reminderTime', 'createdTime', 'modifiedTime')
