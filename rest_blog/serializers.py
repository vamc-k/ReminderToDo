from django.utils import timezone
from rest_framework import serializers
from blog.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'title', 'message', 'reminder_time', 'created_time', 'modified_time')

    def validate_reminder_time(self, reminder_time):
        """
        Check that the reminder time is not past.
        :param reminder_time: 
        :return: 
        """
        print("in reminder_time validation")
        if reminder_time <= timezone.now():
            raise serializers.ValidationError("Reminder should not be past.")
        return reminder_time
