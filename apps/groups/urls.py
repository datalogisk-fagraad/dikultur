from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(
        r'^detail/(?P<slug>\S+)/calendar\.ics$',
        views.GroupICal.as_view(),
        name='ical'
    ),

    url(
        r'^detail/(?P<slug>\S+)/calend[ae]r(|\.ics)$',
        views.GroupICal.as_view(),
        name='ical'
    ),

    url(
        r'^detail/(?P<slug>\S+)/update$',
        views.GroupUpdate.as_view(),
        name='update'
    ),

    url(
        r'^detail/(?P<slug>\S+)/members$',
        views.GroupMembers.as_view(),
        name='members'
    ),

    url(
        r'^detail/(?P<slug>\S+)/join$',
        views.GroupJoin.as_view(),
        name='join'
    ),

    url(
        r'^detail/(?P<slug>\S+)/make-admin/(?P<user_id>\d+)$',
        views.GroupMakeAdmin.as_view(),
        name='make-admin'
    ),

    url(
        r'^detail/(?P<slug>\S+)/remove-admin/(?P<user_id>\d+)$',
        views.GroupRemoveAdmin.as_view(),
        name='remove-admin'
    ),

    url(
        r'^detail/(?P<slug>\S+)$',
        views.GroupDetail.as_view(),
        name='detail'
    ),

    url(
        r'^create$',
        views.GroupCreate.as_view(),
        name='create'
    ),

    url(
        r'^$',
        views.GroupList.as_view(),
        name='list'
    ),
)
