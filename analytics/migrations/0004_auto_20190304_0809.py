# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-04 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20190303_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersession',
            old_name='endded',
            new_name='ended',
        ),
    ]
