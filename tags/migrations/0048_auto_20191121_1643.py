# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-21 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0047_auto_20191121_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]