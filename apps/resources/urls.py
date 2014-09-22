from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>\S+)/remove_upvote$', views.resource_remove_upvote, name='remove_upvote'),
    url(r'^(?P<slug>\S+)/upvote$', views.resource_upvote, name='upvote'),
    url(r'^(?P<slug>\S+)$', views.ResourceDetail.as_view(), name='detail'),
    url(r'^$', views.ResourceList.as_view(), name='list'),
)
