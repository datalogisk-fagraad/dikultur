# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20140823_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcefile',
            name='resource',
            field=models.ForeignKey(to='resources.Resource', related_name='files'),
        ),
        migrations.AlterField(
            model_name='resourcelink',
            name='resource',
            field=models.ForeignKey(to='resources.Resource', related_name='links'),
        ),
    ]
