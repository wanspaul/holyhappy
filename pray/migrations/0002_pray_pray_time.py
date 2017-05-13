# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pray', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pray',
            name='pray_time',
            field=models.CharField(max_length=1, default='M'),
            preserve_default=False,
        ),
    ]
