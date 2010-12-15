# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from customfilefield import ContentTypeRestrictedFileField as RestrictedFileField
from luciernaga.thumbs import ImageWithThumbsField

class Informacion(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Informacion'

class Tema(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    especifico = models.BooleanField(verbose_name='Tema específico de Luciérnaga')
    imagen = models.ImageField(upload_to='temas/', help_text='Imagen que aparece en el banner superior. Tamaño 960x704', null=True, blank=True)
    logo = models.ImageField(upload_to='temas/', help_text='Logo superior. Tamaño 350x300', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Temas'

class Subtema(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    tema = models.ForeignKey(Tema)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Subtemas'

class Genero(models.Model):
    nombre = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Géneros'

class Coleccion(models.Model):
    user = models.ForeignKey(User)
    tema = models.ForeignKey(Tema)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Colecciones'
    
OWNER_CHOICES = (('luciernaga', 'Luciernaga'), ('red', 'Red Mesoamericana'))

class Video(models.Model):
    nombre = models.CharField(max_length=150)
    destacado = models.BooleanField(verbose_name='Marcar como destacado')
    portada = ImageWithThumbsField(upload_to='videos/thumbs', sizes=((80, 52), (112,158), (140,135), ), help_text='Portada de la produccion.')
    #portada = models.ImageField(upload_to='videos/thumbs', help_text='Portada de la produccion. Tamaño 112x158px ancho y alto respectivos')
    #archivo = RestrictedFileField(upload_to='videos',
    #                            content_types=['video/mpeg', 'video/x-msvideo', 'video/quicktime', 'video/x-flv', 'video/mp4'],
    #                            max_upload_size=104857600)
    archivo = models.FileField(upload_to='videos')
    sinopsis = models.TextField()
    realizacion = models.CharField(max_length=200)
    produccion = models.CharField(max_length=300, help_text='Nombre de productores separados por comas')
    anio = models.CharField(max_length=5)    
    tema = models.ForeignKey(Tema)
    subtema = models.ManyToManyField(Subtema)
    genero = models.ForeignKey(Genero)
    coleccion = models.ForeignKey(Coleccion, null=True, blank=True)
    owner = models.CharField(choices=OWNER_CHOICES, max_length=100)
    user = models.ForeignKey(User)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.user)

    def get_portada(self):
        if self.image:
            return u'<img alt="%s" title="%s" width="80" height="52" src="%s" />' % (self.photo_name(), self.photo_name(), self.image.url_80x52)
        else:
            return '(Without image)'
    get_portada.short_description = 'Portada'
    get_portada.allow_tags = True

    class Meta:
        verbose_name_plural = 'Videos'
        ordering = ['-id',]