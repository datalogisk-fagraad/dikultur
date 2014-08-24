from django.db import models
from django.conf import settings
from django.contrib.auth import models as auth_models
from django_extensions.db.fields import AutoSlugField

from taggit.managers import TaggableManager


class Event(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')

    place = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    description = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    group = models.ForeignKey(auth_models.Group, null=True, blank=True)

    tags = TaggableManager(blank=True)

    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('events:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
