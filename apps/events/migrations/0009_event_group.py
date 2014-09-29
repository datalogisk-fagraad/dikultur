# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20140929_1816'),
        ('events', '0008_auto_20140929_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.ForeignKey(null=True, blank=True, to='groups.Group'),
            preserve_default=True,
        ),
    ]
