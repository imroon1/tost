# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-22 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20190321_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestemail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
