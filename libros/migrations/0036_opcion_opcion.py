# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0035_auto_20171107_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcion',
            name='opcion',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opcion_padre', to='libros.Opcion'),
        ),
    ]