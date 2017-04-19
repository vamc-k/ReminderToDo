from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^getAll/$', views.get_all, name='fetch'),
    url(r'^add/$', views.create_reminder, name='add'),
    url(r'^save/(?P<id>\d+)/$', views.save_reminder, name='create'),
    url(r'^edit/(?P<id>\d+)/$', views.edit_reminder, name='edit'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_reminder, name='delete'),
    url(r'^$', views.index),
]