from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^detail/(?P<slug>\S+)/calendar\.ics$', views.GroupICal.as_view(), name='ical'),
    url(r'^detail/(?P<slug>\S+)/calend[ae]r(|\.ics)$', views.GroupICal.as_view(), name='ical'),
    url(r'^detail/(?P<slug>\S+)$', views.GroupDetail.as_view(), name='detail'),
    url(r'^$', views.GroupList.as_view(), name='list'),
)
