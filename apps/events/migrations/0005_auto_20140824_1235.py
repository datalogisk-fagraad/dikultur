# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20140822_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag', blank=True, help_text='A comma-separated list of tags.'),
        ),
    ]
