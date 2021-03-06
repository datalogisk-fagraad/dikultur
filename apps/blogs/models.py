from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager
from .managers import PostQuerySet


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')

    description = models.TextField(null=True, blank=True)
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Post(models.Model):
    objects = PostQuerySet.as_manager()
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    content = models.TextField()

    blog = models.ForeignKey('Blog', related_name='posts')

    tags = TaggableManager(blank=True)

    public = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blogs:post-detail', kwargs={'blog_slug':self.blog.slug, 'slug': self.slug})

    def __str__(self):
        return self.title
