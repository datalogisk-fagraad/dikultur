# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20141013_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='is_open',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
