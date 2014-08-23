from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>\S+)$', views.ResourceDetail.as_view(), name='detail'),
    url(r'^$', views.ResourceList.as_view(), name='list'),
)
