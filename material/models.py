# -*- coding: UTF-8 -*-
import datetime
from django.db import models
from luciernaga.multimedia.customfilefield import ContentTypeRestrictedFileField as RestrictedFileField
from luciernaga.multimedia.models import *
from luciernaga.thumbs import ImageWithThumbsField

class Documento(models.Model):
    titulo = models.CharField(max_length=150)
    portada = ImageWithThumbsField(upload_to='documentos/thumbs', sizes=((80, 52), (112, 158), (140, 135),), help_text='Portada del documento.')
    descripcion = models.TextField(blank=True, default='', help_text='Descripción corta del video')
    fecha = models.DateTimeField(default=datetime.datetime.now())
    archivo = RestrictedFileField(upload_to='documentos', content_types=['application/pdf',], max_upload_size=5242880, help_text='Formato PDF, Tamaño máx. 50MB')
    tema = models.ManyToManyField(Tema)
    videos_relacionados = models.ManyToManyField(Video, blank=True, verbose_name='Videos relacionados (max. 3)')

    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha']

class FotoPortada(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotoportada/')
    slug = models.SlugField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['-id']

class GenericVideo(models.Model):
    titulo = models.CharField(max_length=150)
    url = models.CharField(max_length=300, help_text='Introduzca la URL del video. Ejm: http://www.youtube.com/watch?v=rEi6Me2K2RY')