# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-01 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190228_0629'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestemail',
            old_name='timestam',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='guestemail',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='guestemail',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]
