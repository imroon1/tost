# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-07 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_charge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='last_4',
            new_name='last4',
        ),
    ]