# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-11-16 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_line1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_line2',
            new_name='address_line_2',
        ),
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, help_text='Shipping to? Who is it for?', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='nickname',
            field=models.CharField(blank=True, help_text='Internal Reference Nickname', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing address'), ('shipping', 'Shipping address')], max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='United States of America', max_length=120),
        ),
    ]
