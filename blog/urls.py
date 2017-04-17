from django.conf.urls import url
from blog import views

urlpatterns = urlpatterns = [
    url(r'^getAll/$', views.getAll, name='fetch'),
    url(r'^add/$', views.add, name='add'),
    url(r'^save/(?P<operation>\w+)/(?P<uid>\d+)/$', views.save_reminder, name='create'),
    url(r'^edit/(?P<uid>\d+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<uid>\d+)/$', views.delete, name='delete'),
    url(r'^$',views.index),
]