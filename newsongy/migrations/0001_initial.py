# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(choices=[('U', '대학부'), ('Y', '청년부')], max_length=1)),
                ('group', models.CharField(max_length=3)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
