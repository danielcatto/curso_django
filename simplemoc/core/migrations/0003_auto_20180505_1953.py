# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180505_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.TextField(null=True, verbose_name='Estatos', blank=True),
        ),
    ]
