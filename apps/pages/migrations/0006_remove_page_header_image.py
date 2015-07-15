# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_page_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='header_image',
        ),
    ]
