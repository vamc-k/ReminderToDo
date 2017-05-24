from datetime import datetime, tzinfo

import pytz
from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Reminder
from rest_blog.permissions import IsOwner
from rest_blog.serializers import ReminderSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions

from rest_blog.tasks import send_mail_task


class ReminderList(APIView):
    """
    List all Reminders, or create a new Reminder.
    """

    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get(self, request, format=None):
        reminders = self.get_queryset(request.user)
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            reminder = Reminder.objects.get(pk=serializer.data['id'])
            send_mail_task.apply_async(args=[serializer.data['id']],
                                       eta=reminder.reminder_time)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_queryset(self, user):
        return Reminder.objects.filter(owner=user)


class ReminderDetail(APIView):
    """
    Retrieve, update or delete a Reminder.
    """
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Reminder.objects.all()

    def get_object(self, pk):
        reminders = self.get_queryset()
        try:
            reminder = reminders.get(pk=pk)
            self.check_object_permissions(self.request, reminder)
        except Reminder.DoesNotExist:
            raise NotFound(detail="No resourse found with the ID you are looking.", code=None)
        return reminder

    def get(self, request, pk, format=None):
        content = ""
        reminder = self.get_object(pk)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reminder = self.get_object(pk)

        serializer = ReminderSerializer(reminder, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        reminder = self.get_object(pk)

        reminder.delete()
        return Response(status=202)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
