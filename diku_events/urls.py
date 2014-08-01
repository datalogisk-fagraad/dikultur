from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('events.urls', namespace='events', app_name='events')),

    url(r'^admin/', include(admin.site.urls)),
)
