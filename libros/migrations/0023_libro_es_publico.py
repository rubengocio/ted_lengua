# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0022_comentario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='es_publico',
            field=models.BooleanField(default=False),
        ),
    ]