# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-06 06:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0005_auto_20191105_2258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Card',
            new_name='Charge',
        ),
    ]