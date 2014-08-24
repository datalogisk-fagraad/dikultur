from django.db import models
from django.conf import settings

from django_extensions.db.fields import AutoSlugField

from taggit.managers import TaggableManager


class Resource(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()

    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = 'resource'
        verbose_name_plural = 'resources'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('resources:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ResourceFile(models.Model):
    resource = models.ForeignKey('Resource', related_name='files')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources')

    class Meta:
        verbose_name = 'resource file'
        verbose_name_plural = 'resource files'


class ResourceLink(models.Model):
    resource = models.ForeignKey('Resource', related_name='links')
    title = models.CharField(max_length=255)
    url = models.URLField()