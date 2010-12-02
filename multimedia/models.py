# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User
from customfilefield import ContentTypeRestrictedFileField as RestrictedFileField

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
    portada = models.ImageField(upload_to='videos/thumbs', help_text='Portada de la produccion. Tamaño 112x158px ancho y alto respectivos')
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

    class Meta:
        verbose_name_plural = 'Videos'
        ordering = ['-id',]

import uuid
import os
import re 

p = re.compile(r'[^0-9a-zA-Z\._]+')

def repl(match):
    chars = {u'á': u'a', u'Á':u'A', u'é':u'e', u'É':u'E', u'í': u'i', u'Í':u'I', u'ó':u'o', u'Ó':'O', u'ú':u'u', u'Ú':'U', u'ñ':u'n', u'ü':u'u',}
    a = ''
    for i in match.group():
        print i
        if i in chars:
            a = a + chars[i]
        else:
            a = a + '_'
    return a

#metodo para cambiar nombre a archivos con tildes
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    nombre = p.sub(repl, filename.split('.')[-2])
    print nombre
    filename = "%s.%s" % (nombre, ext)
    return os.path.join(instance.ruta, filename)

class Archivo(models.Model):
    archivo = models.FileField(upload_to = get_file_path)
    ruta = 'otro/'


