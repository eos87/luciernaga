# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from luciernaga.thumbs import ImageWithThumbsField

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    bandera = models.ImageField(upload_to='red/paises/')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Paises'


class Perfil(models.Model):
    user = models.ForeignKey(User)
    logo = ImageWithThumbsField(upload_to='red/perfiles/', sizes=((150,140),), blank=True, null=True)
    descripcion = models.TextField()
    fundada = models.IntegerField()
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Perfiles de miembros'


class Contenido(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Contenidos'

class Documentos(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    archivo = models.FileField(upload_to='red/documentos/')

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Documentos'
