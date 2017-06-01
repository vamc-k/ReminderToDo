from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_blog import views

urlpatterns = [
    url(r'^reminders/$', views.ReminderList.as_view()),
    url(r'^reminders/(?P<pk>[0-9]+)/$', views.ReminderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
