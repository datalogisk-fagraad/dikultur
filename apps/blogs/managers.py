from django.db import models


class PostQuerySet(models.QuerySet):
    def deleted(self):
        return self.filter(is_deleted=True)

    def live(self):
        return self.filter(is_deleted=False)

    def public(self):
        return self.filter(public=True, is_deleted=False)
