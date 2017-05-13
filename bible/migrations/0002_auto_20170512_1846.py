# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bible',
            name='objective',
        ),
        migrations.AddField(
            model_name='bible',
            name='memo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bible',
            name='title',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
