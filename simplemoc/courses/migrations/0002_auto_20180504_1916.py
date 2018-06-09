# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(verbose_name='imagem', blank=True, upload_to='courses/images'),
        ),
    ]
