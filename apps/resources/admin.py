from django.contrib import admin

from .models import Resource, ResourceFile, ResourceLink, ResourceUpvote


class ResourceFileInline(admin.TabularInline):
    model = ResourceFile


class ResourceLinkInline(admin.TabularInline):
    model = ResourceLink


class ResourceAdmin(admin.ModelAdmin):
    model = Resource
    inlines = [ResourceFileInline, ResourceLinkInline]


admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceFile)
admin.site.register(ResourceLink)
admin.site.register(ResourceUpvote)