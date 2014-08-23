from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^create$', views.EventCreate.as_view(), name='create'),
    url(r'^(?P<slug>\S+)/update$', views.EventUpdate.as_view(), name='update'),
    url(r'^(?P<slug>\S+)$', views.EventDetail.as_view(), name='detail'),
    url(r'^$', views.EventList.as_view(), name='list'),
)