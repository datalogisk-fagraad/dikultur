# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='datetime',
            new_name='start',
        ),
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
