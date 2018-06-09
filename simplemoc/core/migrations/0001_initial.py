# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name='Nome', max_length=100)),
                ('description', models.TextField(verbose_name='Descrição', max_length=250)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('status', models.BooleanField(verbose_name='Estatos')),
            ],
        ),
    ]
