# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0039_auto_20171112_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipopregunta',
            name='orden',
            field=models.IntegerField(default=1),
        ),
    ]
