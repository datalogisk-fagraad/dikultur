from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from apps.core.views import FrontPage, ProfileView, Logout

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),

    url(r'^accounts/logout/$', Logout.as_view(), name='account_logout'),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^resources/', include('apps.resources.urls',
                                namespace='resources',
                                app_name='resources')),

    url(r'^events/', include('apps.events.urls',
                             namespace='events',
                             app_name='events')),

    url(r'^groups/', include('apps.groups.urls',
                             namespace='groups',
                             app_name='groups')),

    url(r'^$', FrontPage.as_view(), name='frontpage'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
