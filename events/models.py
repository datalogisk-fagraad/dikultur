from django.db import models
from django.utils.text import slugify


class Event(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)

    place = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    description = models.TextField()

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
