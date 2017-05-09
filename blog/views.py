
from django.shortcuts import render
from django.utils import timezone

from blog.models import Reminder
from blog.forms import ReminderForm


def index(request):
    return render(request, "blog/index.html", {})


def error(request):
    return render(request, "blog/error.html", {})


def create_reminder(request):
    reminder = Reminder()
    reminder_form = ReminderForm(instance=reminder)
    id = 0
    return render(request, "blog/reminderForm.html", {'reminder_form': reminder_form, 'id': id})


def get_all(request):
    reminders = Reminder.objects.all()
    return render(request, "blog/showReminder.html", {'reminders': reminders})


def save_reminder(request, id):
    if request.method == 'POST':
        reminder_form = ReminderForm(request.POST)
        if reminder_form.is_valid():
            if int(id) > 0:
                reminder = Reminder.objects.get(id=id)
                reminder.title = reminder_form.cleaned_data['title']
                reminder.message = reminder_form.cleaned_data['message']
                reminder.reminder_time = reminder_form.cleaned_data['reminder_time']
                reminder.modified_time = timezone.now()
                reminder.save()
            else:
                reminder_form.modified_time = timezone.now()
                reminder_form.save()
        else:
            return render(request, "blog/reminderForm.html",
                          {'reminder_form': reminder_form, 'id': id})
    reminders = Reminder.objects.all()
    return render(request, "blog/showReminder.html", {'reminders': reminders})


def edit_reminder(request, id):
    reminder = Reminder.objects.get(id=id)
    reminder_form = ReminderForm(instance=reminder)
    return render(request, "blog/reminderForm.html", {'reminder_form': reminder_form, 'id': id})


def delete_reminder(request, id):
    reminder = Reminder.objects.get(id=id)
    reminder.delete()
    reminders = Reminder.objects.all()
    return render(request, "blog/showReminder.html", {'reminders': reminders})
