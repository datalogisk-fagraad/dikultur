from django.db import models


class TimestampedModel(models.Model):
    """
    Simple abstract model that gives deriving models created and updated
    fields.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
