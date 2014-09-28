# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_auto_20140919_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcefile',
            name='title',
        ),
    ]
