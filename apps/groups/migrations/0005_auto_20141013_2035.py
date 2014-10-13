# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_groupmembership_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 47, 764259), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 49, 212749), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupmembership',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 50, 687812), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupmembership',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 52, 44528), auto_now=True),
            preserve_default=False,
        ),
    ]
