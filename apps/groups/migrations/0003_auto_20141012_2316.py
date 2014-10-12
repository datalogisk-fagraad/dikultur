# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20140929_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='email',
            field=models.EmailField(blank=True, max_length=75, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='mailinglist_signup',
            field=models.URLField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
