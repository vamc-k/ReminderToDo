from django.utils import timezone
from rest_framework import serializers

from blog.models import Reminder

from django.contrib.auth.models import User


class ReminderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reminder
        fields = ('id', 'title', 'message', 'reminder_time', 'created_time', 'modified_time', 'owner')

    def validate_reminder_time(self, reminder_time):
        """
        Check that the reminder time is not past.
        :param reminder_time: 
        :return: 
        """
        if reminder_time <= timezone.now():
            raise serializers.ValidationError("Reminder should not be past.")
        return reminder_time


class UserSerializer(serializers.ModelSerializer):
    reminders = serializers.PrimaryKeyRelatedField(many=True, queryset=Reminder.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'reminders', 'token')
