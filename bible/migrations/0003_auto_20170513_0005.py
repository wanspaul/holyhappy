# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0002_auto_20170512_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bible',
            name='read_dt',
        ),
        migrations.AddField(
            model_name='bible',
            name='day',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
