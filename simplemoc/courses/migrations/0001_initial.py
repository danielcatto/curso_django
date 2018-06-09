# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('start_date', models.DateField(blank=True, verbose_name='Data de Início', null=True)),
                ('image', models.ImageField(verbose_name='imagem', upload_to='courses/images')),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
            ],
        ),
    ]
