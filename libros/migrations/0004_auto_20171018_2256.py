# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0003_auto_20171018_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(max_length=250),
        ),
    ]
