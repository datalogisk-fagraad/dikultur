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

    def upvote(self, user):
        """
        Raises IntegrityError if user has already upvoted resource
        :param user:
        """
        try:
            self.resourceupvote_set.create(user=user, resource=self)
        except ResourceUpvote.DoesNotExist:
            pass

    def remove_upvote(self, user):
        try:
            upvote = self.resourceupvote_set.get(user=user, resource=self)
            upvote.delete()
        except ResourceUpvote.DoesNotExist:
            pass

    @property
    def upvotes(self):
        return self.resourceupvote_set.count()


class ResourceUpvote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    resource = models.ForeignKey('Resource')

    class Meta:
        unique_together = ('user', 'resource')


class ResourceFile(models.Model):
    resource = models.ForeignKey('Resource', related_name='files')
    file = models.FileField(upload_to='resources')

    class Meta:
        verbose_name = 'resource file'
        verbose_name_plural = 'resource files'

    @property
    def filename(self):
        return self.file.name.split('/')[-1]


class ResourceLink(models.Model):
    resource = models.ForeignKey('Resource', related_name='links')
    title = models.CharField(max_length=255)
    url = models.URLField()

    class Meta:
        verbose_name = 'resource link'
        verbose_name_plural = 'resource links'
