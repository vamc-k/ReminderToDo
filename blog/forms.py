from django.contrib.admin.widgets import AdminSplitDateTime
from django import forms
from blog.models import Reminder


class ReminderForm(forms.ModelForm):
    title = forms.CharField(max_length=25)
    message = forms.CharField(max_length=100)
    reminderTime = forms.DateTimeField()

    class Meta:
        model = Reminder
        fields = ['title', 'message', 'reminderTime']
