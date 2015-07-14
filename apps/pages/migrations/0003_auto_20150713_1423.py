# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='header_image',
        ),
        migrations.AddField(
            model_name='page',
            name='new_header_image',
            field=filer.fields.image.FilerImageField(related_name='page_header_image', blank=True, to='filer.Image', null=True),
        ),
    ]
