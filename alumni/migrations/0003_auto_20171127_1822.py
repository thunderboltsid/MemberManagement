# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_auto_20171127_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='set_address',
        ),
        migrations.RemoveField(
            model_name='approval',
            name='set_jacobs',
        ),
        migrations.RemoveField(
            model_name='approval',
            name='set_job',
        ),
        migrations.RemoveField(
            model_name='approval',
            name='set_social',
        ),
        migrations.AlterField(
            model_name='alumni',
            name='birthday',
            field=models.DateField(help_text='Your birthday in the format YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='approval',
            field=models.BooleanField(default=False, help_text='Has the user been approved by an admin?'),
        ),
        migrations.AlterField(
            model_name='jobinformation',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='alumni.Alumni'),
        ),
    ]
