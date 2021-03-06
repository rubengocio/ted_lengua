# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0042_auto_20171114_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoevaluacion',
            name='opcion',
        ),
        migrations.RemoveField(
            model_name='autoevaluacion',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='autoevaluacion',
            name='opciones',
            field=models.ManyToManyField(blank=True, null=True, to='libros.Opcion'),
        ),
        migrations.AddField(
            model_name='autoevaluacion',
            name='preguntas',
            field=models.ManyToManyField(blank=True, null=True, to='libros.Pregunta'),
        ),
    ]
