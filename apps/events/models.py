from django.db import models
from django.conf import settings
from django.contrib.auth import models as auth_models
from django_extensions.db.fields import AutoSlugField
from apps.core.models import TimestampedModel

from apps.groups.models import Group

import icalendar

from taggit.managers import TaggableManager


class Event(TimestampedModel):

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')

    place = models.CharField(max_length=255)

    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    description = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    group = models.ForeignKey(Group, null=True, blank=True)

    tags = TaggableManager(blank=True)

    public = models.BooleanField(default=False)

    ical = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('events:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        # We need the slug to create description for the iCal generation
        if not self.slug:
            super().save(*args, **kwargs)

        event = icalendar.Event()

        event.add('dtstart', self.start)

        if self.end:
            event.add('dtend', self.end)

        event.add('summary', self.title)
        event.add('description', self.get_absolute_url())
        self.ical = event.to_ical()

        super().save(*args, **kwargs)
