from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from blog.models import Reminder
from blog.forms import ReminderForm


def index(request):
    return render(request, "blog/index.html", {})


def add(request):
    r = Reminder()
    form = ReminderForm(instance=r)
    uid = 0
    return render(request, "blog/reminderForm.html", {'form': form, 'operation': 'new', 'id': uid})


def getAll(request):
    reminders = Reminder.objects.all()
    return render(request, "blog/showReminder.html", {'reminders': reminders})


def save_reminder(request, operation,uid):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            print("SUCCESS")
            if int(uid) > 0:
                r = Reminder.objects.get(id=uid)
                r.title = form.cleaned_data['title']
                r.message = form.cleaned_data['message']
                r.reminderTime = form.cleaned_data['reminderTime']
                r.modifiedTime = timezone.now()
                r.save()
            else:
                form.modifiedTime = timezone.now()
                form.save()
        else:
            print("ERROR")

    reminders = Reminder.objects.all()
    return render(request, "blog/showReminder.html", {'reminders': reminders})


def edit(request, uid):
    r = Reminder.objects.get(id=uid)
    form = ReminderForm(instance=r)
    return render(request, "blog/reminderForm.html", {'form': form, 'operation':'edit', 'id':uid})


def delete(request, uid):
    r = Reminder.objects.get(id=uid)
    r.delete()
    reminders = Reminder.objects.all()
    return render(request, "blog/showReminder.html", {'reminders': reminders})
