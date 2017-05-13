# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsongy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('joined', models.BooleanField(default=False)),
                ('person', models.ForeignKey(to='newsongy.Person')),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='Pray',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pray_dt', models.DateField()),
            ],
            options={
                'db_table': 'pray',
            },
        ),
        migrations.AddField(
            model_name='attendance',
            name='pray',
            field=models.ForeignKey(to='pray.Pray'),
        ),
    ]
