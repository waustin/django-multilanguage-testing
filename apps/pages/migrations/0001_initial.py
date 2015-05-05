# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_es', models.CharField(max_length=100, null=True)),
                ('relative_url', models.CharField(unique=True, max_length=250, editable=False, db_index=True)),
                ('display_order', models.PositiveIntegerField(default=1, help_text=b'Controls order that pages are displayed', db_index=True)),
                ('content', models.TextField(blank=True)),
                ('content_en', models.TextField(null=True, blank=True)),
                ('content_es', models.TextField(null=True, blank=True)),
                ('head_title', models.CharField(default=b'', help_text=b'Page Title for head. Max length 100 characters.', max_length=100, blank=True)),
                ('head_title_en', models.CharField(default=b'', max_length=100, null=True, help_text=b'Page Title for head. Max length 100 characters.', blank=True)),
                ('head_title_es', models.CharField(default=b'', max_length=100, null=True, help_text=b'Page Title for head. Max length 100 characters.', blank=True)),
                ('meta_description', models.CharField(default=b'', help_text=b'Page Meta Description Field. Max length 200 characters.', max_length=200, blank=True)),
                ('meta_description_en', models.CharField(default=b'', max_length=200, null=True, help_text=b'Page Meta Description Field. Max length 200 characters.', blank=True)),
                ('meta_description_es', models.CharField(default=b'', max_length=200, null=True, help_text=b'Page Meta Description Field. Max length 200 characters.', blank=True)),
                ('is_hidden', models.BooleanField(default=False, help_text=b"Hidden pages do not show up in search or have a valid URL. They are useful for grouping similar pages by a parent page you don't want vislbe on the site")),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='pages.Page', null=True)),
            ],
            options={
                'ordering': ('lft',),
            },
        ),
        migrations.CreateModel(
            name='PageTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Unique Name/ID for a template.', unique=True, max_length=100)),
                ('file_name', models.CharField(help_text=b'Full Path and file name of the template.', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(blank=True, to='pages.PageTemplate', help_text=b'The template used to display this page. If blank the default template is used.', null=True),
        ),
    ]
