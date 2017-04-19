from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_blog.models import Reminder
from rest_blog.serializers import ReminderSerializer


@api_view(['GET', 'POST'])
def reminder_list(request):
    """
    List all code snippets, or create a new Reminder.
    """
    if request.method == 'GET':
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def reminder_detail(request, pk):
    """
    Retrieve, update or delete a Reminder.
    """
    try:
        reminder = Reminder.objects.get(pk=pk)
    except Reminder.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReminderSerializer(reminder)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReminderSerializer(reminder, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        reminder.delete()
        return HttpResponse(status=204)
