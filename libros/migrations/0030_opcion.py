# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0029_pregunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=256)),
                ('puntaje', models.PositiveIntegerField(choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')], default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('pregunta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.Pregunta')),
            ],
        ),
    ]
