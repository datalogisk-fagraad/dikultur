from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<slug>\S+)/create$', views.PostCreate.as_view(), name='create'),

    url(r'^all$', views.PostList.as_view(), name='list'),
    url(r'^(?P<slug>\S+)$', views.PostList.as_view(), name='list'),
    url(r'^$', views.BlogList.as_view(), name='bloglist'),
)
