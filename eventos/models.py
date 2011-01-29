# -*- coding: UTF-8 -*-
from django.db import models
from luciernaga.thumbs import ImageWithThumbsField
from luciernaga.utils import get_file_path
from luciernaga.material.models import *
from django.template.defaultfilters import slugify

class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    portada = ImageWithThumbsField(upload_to=get_file_path, sizes=((175, 110), (385, 240), ), help_text='Formatos permitidos: .jpg .png .gif')
    fecha = models.DateTimeField()
    hora = models.CharField(max_length=100, help_text='Ej: 3pm-7pm')
    direccion = models.CharField(max_length=200, blank=True, default='')
    contenido = models.TextField()
    documentos = models.ManyToManyField(Documento, verbose_name='Documentos relacionados', blank=True, null=True)
    slug = models.SlugField(editable=False)

    fileDir = 'eventos/images/'

    class Meta:
        ordering = ['-fecha']

    def __unicode__(self):
        return self.titulo

    def save(self):
        if not self.id:
            n = Evento.objects.all().count()
            s = '%s-%s' % (str(n + 1), slugify(self.titulo))
            self.slug = s[0:49]
        else:
            pass
        super(Evento, self).save()

    def get_full_url(self):
        return '/eventos/%s' % self.slug

    def get_model(self):
        return '[Evento] '

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    portada = ImageWithThumbsField(upload_to=get_file_path, sizes=((175, 110), (385, 240), ), help_text='Formatos permitidos: .jpg .png .gif')
    fecha = models.DateTimeField()    
    contenido = models.TextField()
    documentos = models.ManyToManyField(Documento, verbose_name='Documentos relacionados', blank=True, null=True)
    slug = models.SlugField(editable=False)

    fileDir = 'noticias/images/'

    class Meta:
        ordering = ['-fecha']

    def __unicode__(self):
        return self.titulo

    def save(self):
        if not self.id:
            n = Noticia.objects.all().count()
            s = '%s-%s' % (str(n + 1), slugify(self.titulo))
            self.slug = s[0:49]
        else:
            pass
        super(Noticia, self).save()

    def get_full_url(self):
        return '/noticias/%s' % self.slug

    def get_model(self):
        return '[Noticia] '
