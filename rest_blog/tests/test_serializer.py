from django.test import TestCase

from blog.models import Reminder
from rest_blog.serializers import ReminderSerializer


class ReminderSerializerTest(TestCase):

    def test_serializer(self):

        # Do the serialization
        actual_output = ReminderSerializer(Reminder.objects.all(), many=True).data
        # Did it work?
        self.assertEqual(actual_output, actual_output)
