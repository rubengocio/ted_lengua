# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0005_auto_20171018_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen_categoria',
            field=models.ImageField(upload_to='img/%Y/%m'),
        ),
    ]
