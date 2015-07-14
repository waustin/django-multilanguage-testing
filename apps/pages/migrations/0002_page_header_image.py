# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='header_image',
            field=filebrowser.fields.FileBrowseField(help_text=b'Header image for the top of the page.', max_length=200, blank=True),
        ),
    ]
