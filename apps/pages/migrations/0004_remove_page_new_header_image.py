# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150713_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='new_header_image',
        ),
    ]
