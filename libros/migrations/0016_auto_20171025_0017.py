# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0015_libro_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='calificacion',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]