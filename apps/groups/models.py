from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField


class Group(models.Model):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField()
    website = models.URLField(null=True, blank=True)

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through='GroupMembership'
    )

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.name


class GroupMembership(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='memberships'
    )

    group = models.ForeignKey(
        'Group',
        related_name='memberships'
    )

    class Meta:
        verbose_name = 'group membership'
        verbose_name_plural = 'group memberships'
