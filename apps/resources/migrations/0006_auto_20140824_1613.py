# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20140824_1235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcelink',
            options={'verbose_name': 'resource link', 'verbose_name_plural': 'resource links'},
        ),
    ]
