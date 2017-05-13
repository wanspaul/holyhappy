# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0004_bible_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bible',
            name='page',
        ),
    ]
