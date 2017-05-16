import json

from django.contrib.auth.models import User, AnonymousUser
from django.core.management import call_command

from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase


class CreateReminderTest(APITestCase):
    """Test for creation of Reminder."""
    def setUp(self):
        self.user = User.objects.create_user(username='testing', password='testing', email='testing@gmail.com')
        self.data = {'title': 'sample testing', 'message': 'hello this is for testing',
                     'owner': 'testing', 'reminder_time': '2017-05-22T12:53:43.429547Z'
                     }
        call_command(
            'loaddata',
            'reminders_list.json',
            verbosity=0
        )

        self.anonymous_user = AnonymousUser()

    def test_can_create_reminder(self):
        """Create Reminder"""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/'
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'sample testing')
        self.assertEqual(response.data['reminder_time'], '2017-05-22T12:53:43.429547Z')
        self.assertEqual(response.data['owner'], 'testing')
        self.assertEqual(response.data['message'], 'hello this is for testing')

    def test_can_create_reminder_bad_request(self):
        """Create reminder with in-correct data gives bad-request"""
        self.client.force_authenticate(user=self.user)
        self.data.clear()
        url = '/rest_blog/reminders/'
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], ['This field is required.'])
        self.assertEqual(response.data['title'], ['This field is required.'])
        self.assertEqual(response.data['reminder_time'], ['This field is required.'])


class ReadReminderTest(APITestCase):
    """Test for reading Reminders"""
    def setUp(self):
        self.user = User.objects.create_user(username='testing', password='testing', email='testing@gmail.com')
        call_command(
            'loaddata',
            'reminders_list.json',
            verbosity=0
        )

    def test_can_read_reminder_list(self):
        """Can read list of reminders"""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_reminder_details(self):
        """Can read a reminder by pk"""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task-1')
        self.assertEqual(response.data['message'], 'Have to submit Assignment by today')
        self.assertEqual(response.data['reminder_time'], '2017-05-20T05:09:59Z')
        self.assertEqual(response.data['modified_time'], '2017-04-26T07:00:46.395000Z')
        self.assertEqual(response.data['created_time'], '2017-04-24T09:33:24.285000Z')
        self.assertEqual(response.data['owner'], 'testing')

    def test_can_read_reminder_details_not_found(self):
        """Read a reminder by pk which is not exists will gives resource Not-Found"""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/20/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'No resourse found with the ID you are looking.')


class UpdateReminderTest(APITestCase):
    """Test for updating Reminder"""
    def setUp(self):
        self.user = User.objects.create_user(username='testing', password='testing', email='testing@gmail.com')
        call_command(
            'loaddata',
            'reminders_list.json',
            verbosity=0
        )
        self.data = {'title': 'Updated testing', 'message': 'hello this test is for update',
                     'owner': 'testing', 'reminder_time': '2017-05-22T12:53:43.429547Z'
                     }

    def test_can_update_reminder(self):
        """Can update a reminder by pk with correct data."""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/10/'
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated testing')
        self.assertEqual(response.data['message'], 'hello this test is for update')
        self.assertEqual(response.data['owner'], 'testing')
        self.assertEqual(response.data['reminder_time'], '2017-05-22T12:53:43.429547Z')

    def test_can_update_reminder_not_found(self):
        """Updating a reminder by pk which is not exists gives resource Not-Found."""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/5/'
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'No resourse found with the ID you are looking.')

    def test_can_update_reminder_bad_request_reminder_time(self):
        """Updating a reminder by pk with in-correct reminder_time gives Bad-Request."""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/1/'
        self.data = {'title': 'sample testing', 'message': 'hello this is for testing',
                     'reminder_time': '2017-05-12T12:53:43.429547Z'
                     }
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['reminder_time'], ['Reminder should not be past.'])

    def test_can_update_reminder_bad_request_title(self):
        """Updating a reminder by pk with in-correct title gives Bad-Request."""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/1/'
        self.data = {'title': '', 'message': 'hello this is for testing',
                     'reminder_time': '2017-08-30T12:53:43.429547Z'
                     }
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'], ['This field may not be blank.'])

    def test_can_update_reminder_bad_request_message(self):
        """Updating a reminder by pk with in-correct message gives Bad-Request."""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/1/'
        self.data = {'title': 'sample testing', 'message': '',
                     'reminder_time': '2017-08-30T12:53:43.429547Z'
                     }
        response = self.client.put(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], ['This field may not be blank.'])


class DeleteReminderTest(APITestCase):
    """Test for deleting the Reminder"""
    def setUp(self):
        self.user = User.objects.create_user(username='testing', password='testing', email='testing@gmail.com')
        call_command(
            'loaddata',
            'reminders_list.json',
            verbosity=0
        )

    def test_can_delete_reminder(self):
        """Delete a reminder by pk."""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_can_delete_reminder_not_found(self):
        """Delete a reminder by pk which is not exists gives resource Not-Found."""
        self.client.force_authenticate(user=self.user)
        url = '/rest_blog/reminders/12/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'No resourse found with the ID you are looking.')
