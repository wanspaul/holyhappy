# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0003_auto_20170513_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='bible',
            name='page',
            field=models.IntegerField(default=0),
        ),
    ]
