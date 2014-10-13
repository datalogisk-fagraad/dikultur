from .abstract import *
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    """
    Placeholder so migrations won't break if a custom user is needed.
    """
    pass
