# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20140928_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupdetails',
            name='group',
        ),
        migrations.DeleteModel(
            name='GroupDetails',
        ),
    ]