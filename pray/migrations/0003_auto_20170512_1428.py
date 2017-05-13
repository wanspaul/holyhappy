# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pray', '0002_pray_pray_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='joined',
            new_name='joined_afternoon',
        ),
        migrations.RemoveField(
            model_name='pray',
            name='pray_time',
        ),
        migrations.AddField(
            model_name='attendance',
            name='joined_morning',
            field=models.BooleanField(default=False),
        ),
    ]
