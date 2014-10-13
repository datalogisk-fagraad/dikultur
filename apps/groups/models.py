from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField

from ..core.models import TimestampedModel


class Group(TimestampedModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField()

    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mailinglist_signup = models.URLField(null=True, blank=True)

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='GroupMembership'
    )

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('groups:detail', kwargs={'slug': self.slug})

    @property
    def admins(self):
        return self.members.filter(memberships__is_admin=True)


class GroupMembership(TimestampedModel):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='memberships'
    )

    group = models.ForeignKey(
        'Group',
        related_name='memberships'
    )

    is_admin = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'group membership'
        verbose_name_plural = 'group memberships'
