# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-03-20 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190320_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestemail',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
