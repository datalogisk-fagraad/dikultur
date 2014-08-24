# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', related_name='user_set', related_query_name='user', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', related_name='user_set', related_query_name='user', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
