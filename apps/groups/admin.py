from django.contrib import admin
from . import models


class GroupMembershipInline(admin.TabularInline):
    model = models.GroupMembership


class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupMembershipInline]


admin.site.register(models.Group, GroupAdmin)
