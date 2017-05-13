# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsongy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bible',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('objective', models.IntegerField()),
                ('read', models.BooleanField(default=False)),
                ('read_dt', models.DateField()),
                ('person', models.ForeignKey(to='newsongy.Person')),
            ],
            options={
                'db_table': 'bible',
            },
        ),
    ]
