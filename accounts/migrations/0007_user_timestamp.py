# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-01 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190301_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
