# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0010_address_addressvisible'),
    ]

    operations = [
        migrations.AddField(
            model_name='jacobsdata',
            name='comments',
            field=models.TextField(blank=True, help_text='e.g. exchange semester, several degrees etc.', null=True),
        ),
    ]