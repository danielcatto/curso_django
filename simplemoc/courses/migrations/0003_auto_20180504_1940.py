# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180504_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(upload_to='courses/images', null=True, verbose_name='imagem', blank=True),
        ),
    ]
