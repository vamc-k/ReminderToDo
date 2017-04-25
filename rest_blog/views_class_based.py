
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.models import Reminder
from rest_blog.permissions import IsOwner
from rest_blog.serializers import ReminderSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


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
            reminder = 204
        return reminder

    def get(self, request, pk, format=None):
        content = ""
        reminder = self.get_object(pk)
        if reminder == 204:
            content = {
                'status': 204,
                'message': 'No reminder with the id you provided.'
            }
            return Response(content)
        serializer = ReminderSerializer(reminder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reminder = self.get_object(pk)
        if reminder == 204:
            content = {
                'status': 204,
                'message': 'No reminder with the id you provided.'
            }
            return Response(content)
        data = JSONParser().parse(request)
        serializer = ReminderSerializer(reminder, data=data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        reminder = self.get_object(pk)
        if reminder == 204:
            content = {
                'status': 204,
                'message': 'No reminder with the id you provided.'
            }
            return Response(content)
        reminder.delete()
        content = {
            'status': 202,
            'message': 'Deleted sucessfully.'
        }
        return Response(content)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
