# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20140824_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
