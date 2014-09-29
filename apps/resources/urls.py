from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.ResourceCreate.as_view(), name='create'),

    url(r'^detail/(?P<slug>\S+)/remove_upvote$', views.resource_remove_upvote, name='remove_upvote'),
    url(r'^detail/(?P<slug>\S+)/upvote$', views.resource_upvote, name='upvote'),

    url(r'^detail/(?P<slug>\S+)/update/delete_file$', views.resource_file_delete, name='delete-file'),
    url(r'^detail/(?P<slug>\S+)/update$', views.ResourceUpdate.as_view(), name='update'),

    url(r'^detail/(?P<slug>\S+)$', views.ResourceDetail.as_view(), name='detail'),

    url(r'^$', views.ResourceList.as_view(), name='list'),
)
