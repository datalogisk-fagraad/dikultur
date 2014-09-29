# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('core', '0002_auto_20140824_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.TextField()),
                ('url', models.URLField(null=True, blank=True)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='groupdetail',
            name='group',
        ),
        migrations.DeleteModel(
            name='GroupDetail',
        ),
    ]
