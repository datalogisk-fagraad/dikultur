from django.db import models
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.utils.text import slugify


class Event(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)

    place = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    description = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    group = models.ForeignKey(auth_models.Group, null=True, blank=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('events:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if not self.id:
            self.slug = slugify(self.title)

        super().save(force_insert, force_update, using, update_fields)


class GroupDetail(models.Model):
    group = models.OneToOneField(auth_models.Group)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.group


class User(auth_models.AbstractUser):
    """
    Placeholder so migrations won't break if a custom user is needed.
    """
    pass
