# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_remove_resourcefile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 53, 657540), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 55, 8608), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcefile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 56, 242466), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcefile',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 57, 429585), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 34, 58, 750451), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourcelink',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 35, 0, 524252), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourceupvote',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 35, 2, 95237), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourceupvote',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 13, 20, 35, 3, 625203), auto_now=True),
            preserve_default=False,
        ),
    ]
