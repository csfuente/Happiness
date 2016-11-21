# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0004_auto_20161111_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measur',
            name='alegria',
        ),
        migrations.RemoveField(
            model_name='measur',
            name='amor',
        ),
        migrations.RemoveField(
            model_name='measur',
            name='envidia',
        ),
        migrations.RemoveField(
            model_name='measur',
            name='ira',
        ),
        migrations.RemoveField(
            model_name='measur',
            name='miedo',
        ),
        migrations.RemoveField(
            model_name='measur',
            name='sorpresa',
        ),
        migrations.RemoveField(
            model_name='measur',
            name='tristeza',
        ),
        migrations.AddField(
            model_name='measur',
            name='negative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='measur',
            name='neutral',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='measur',
            name='positive',
            field=models.IntegerField(default=0),
        ),
    ]
