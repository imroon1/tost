# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-01 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190301_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestemail',
            name='email',
            field=models.EmailField(),
        ),
    ]
