# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-24 01:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20191123_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpurchase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
