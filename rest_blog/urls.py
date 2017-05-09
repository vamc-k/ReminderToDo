from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_blog import views_class_based

urlpatterns = [
    url(r'^reminders/$', views_class_based.ReminderList.as_view()),
    url(r'^reminders/(?P<pk>[0-9]+)/$', views_class_based.ReminderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
