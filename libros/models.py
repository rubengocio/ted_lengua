import random

from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=22)
    slug = AutoSlugField(populate_from='nombre')
    descripcion = models.TextField(max_length=250, null=False, blank=False)
    imagen_categoria = models.ImageField(upload_to='media/%Y/%m')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.nombre)

class Imagen(models.Model):
    titulo = models.CharField(max_length=256)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='media/%Y/%m')
    categoria = models.ForeignKey(Categoria)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.titulo)

    def get_images_by_paginate(self, category):
        images_list = Imagen.objects.filter(categoria=category)
        contador = 1
        max = 4
        row = []
        images = []
        for image in images_list:

            if contador > max:
                contador = 1
                images.append(row)
                row = []

            row.append(image)
            contador = contador + 1

        if len(row) > 0:
            images.append(row)

        return images


class Libro(models.Model):
    titulo = models.CharField(max_length=256)
    slug = AutoSlugField(populate_from='titulo')
    introduccion = models.TextField(max_length=512)
    imagen = models.ForeignKey(Imagen)
    usuario = models.ForeignKey(User)
    categoria = models.ForeignKey(Categoria)
    calificacion = models.IntegerField(default=None, null=True, blank=True)
    es_publico = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.titulo)

    @staticmethod
    def get_destacados():
        libros_destacados = Libro.objects.filter(es_publico=True).order_by('?')[:4]
        return libros_destacados


class Capitulo(models.Model):
    libro = models.ForeignKey(Libro)
    titulo = models.CharField(max_length=256)
    imagen = models.ForeignKey(Imagen)
    texto = models.TextField()
    orden = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.titulo)

    class Meta:
        unique_together = ('libro', 'orden')


class Comentario(models.Model):
    libro = models.ForeignKey(Libro)
    comentario = models.CharField(max_length=512)
    usuario = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.comentario)


class Contenido(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    texto = models.TextField()
    usuario = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)