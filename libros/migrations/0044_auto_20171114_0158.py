# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0043_auto_20171114_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoevaluacion',
            name='opciones',
        ),
        migrations.AddField(
            model_name='autoevaluacion',
            name='opciones',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.Opcion'),
        ),
        migrations.RemoveField(
            model_name='autoevaluacion',
            name='preguntas',
        ),
        migrations.AddField(
            model_name='autoevaluacion',
            name='preguntas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.Pregunta'),
        ),
    ]
