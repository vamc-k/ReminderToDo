
from django import forms
from blog.models import Reminder


class ReminderForm(forms.ModelForm):
    title = forms.CharField(min_length=6, max_length=25)
    message = forms.CharField(min_length=10, max_length=100)
    reminder_time = forms.DateTimeField()

    class Meta:
        model = Reminder
        fields = ['title', 'message', 'reminder_time']
