# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180505_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contatos', 'verbose_name': 'Contato', 'ordering': ['name']},
        ),
    ]
