# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0045_auto_20171114_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoevaluacion',
            name='opciones',
        ),
        migrations.AddField(
            model_name='autoevaluacion',
            name='opciones',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.RemoveField(
            model_name='autoevaluacion',
            name='preguntas',
        ),
        migrations.AddField(
            model_name='autoevaluacion',
            name='preguntas',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
