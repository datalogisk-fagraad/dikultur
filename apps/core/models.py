from django.db import models
from django.contrib.auth import models as auth_models


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

    def save(self, *args, **kwargs):
        if not self.id:
            self.set_password(self.password)
        super().save(*args, **kwargs)
