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

    @property
    def get_nombre_singular(self):
        if self.nombre[-1:] == 's':
            return self.nombre[0:len(self.nombre)-1]
        else:
            return self.nombre


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
        return "%s" % self.titulo

    def __unicode__(self):
        return "%s" % self.titulo

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


PUNTAJE = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class TipoPregunta(models.Model):
    texto = models.CharField(max_length=127)
    iso = models.CharField(max_length=3)
    orden = models.IntegerField(default=1)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return '%s' % self.texto

    def __unicode__(self):
        return '%s' % self.texto

    @property
    def get_questions(self):
        return Pregunta.objects.filter(tipo_pregunta=self)

    @property
    def get_puntaje(self):
        puntaje = 0
        preguntas = Pregunta.objects.filter(tipo_pregunta=self)
        for pregunta in preguntas:
            puntaje += pregunta.get_puntaje
        return puntaje


class Pregunta(models.Model):
    tipo_pregunta = models.ForeignKey(TipoPregunta, null=True, blank=True, default=None)
    texto = models.CharField(max_length=256)
    puntaje = models.PositiveIntegerField(default=0, choices=PUNTAJE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.texto

    def __unicode__(self):
        return '%s' % self.texto

    @property
    def get_options(self):
        return Opcion.objects.filter(pregunta=self)

    @property
    def count_options(self):
        return Opcion.objects.filter(pregunta=self).count()

    @property
    def get_puntaje(self):
        puntos = self.puntaje

        opciones = Opcion.objects.filter(pregunta=self)
        for opcion in opciones:
            puntos += opcion.puntaje

        return puntos


class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    texto = models.CharField(max_length=256)
    puntaje = models.PositiveIntegerField(default=0, choices=PUNTAJE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.texto

    def __unicode__(self):
        return '%s' % self.texto


class Autoevaluacion(models.Model):
    libro = models.ForeignKey(Libro)
    preguntas = models.CharField(max_length=512, null=True, blank=True)
    opciones = models.CharField(max_length=512, null=True, blank=True)
    puntaje = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.libro)

    def __unicode__(self):
        return '%s' % (self.libro)
