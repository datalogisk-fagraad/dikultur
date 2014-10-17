from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from . import views

urlpatterns = patterns('',
    url(r'^(?P<slug>all)$', views.BlogIndex.as_view(), name='all'),
    url(r'^(?P<blog_slug>\S+)/(?P<slug>\S+)/update$', views.PostUpdate.as_view(), name='post-update'),
    url(r'^(?P<blog_slug>\S+)/(?P<slug>\S+)$', views.PostDetail.as_view(), name='post-detail'),
    url(r'^(?P<slug>\S+)/create$', views.PostCreate.as_view(), name='create'),
    url(r'^(?P<slug>\S+)/$', views.BlogDetail.as_view(), name='blog-detail'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('blogs:all', kwargs={'slug': 'all'})), name='root'),
)
