# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-08 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0012_card_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='default',
        ),
    ]