from django.conf.urls import url
from rest_blog import views

urlpatterns = [
    url(r'^reminders/$', views.reminder_list),
    url(r'^reminders/(?P<pk>[0-9]+)/$', views.reminder_detail),
]
