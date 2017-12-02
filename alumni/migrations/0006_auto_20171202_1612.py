# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_auto_20171202_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinformation',
            name='customer',
            field=models.CharField(blank=True, help_text='The stripe cusomter id for the user', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paymentinformation',
            name='subscription',
            field=models.CharField(blank=True, help_text='The payment token for the customer', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paymentinformation',
            name='token',
            field=models.CharField(blank=True, help_text='The stripe card token for the user', max_length=255, null=True),
        ),
    ]