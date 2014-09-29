from django.db import models
from django.contrib.auth import models as auth_models


class GroupDetails(models.Model):
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
