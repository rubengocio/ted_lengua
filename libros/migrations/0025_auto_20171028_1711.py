# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0024_auto_20171028_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='introduccion',
            field=models.TextField(max_length=512),
        ),
    ]