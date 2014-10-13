# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20141012_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmembership',
            name='is_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
