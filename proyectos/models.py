# -*- coding: UTF-8 -*-
from django.db import models
from luciernaga.material.models import *
from luciernaga.multimedia.models import *
from luciernaga.thumbs import ImageWithThumbsField
from luciernaga.utils import get_file_path
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^luciernaga\.thumbs\.ImageWithThumbsField"])

class Base(models.Model):
    titulo = models.CharField(max_length=200)
    portada = ImageWithThumbsField(upload_to=get_file_path, sizes=((175, 110), (385, 240), ), help_text='Formatos permitidos: .jpg .png .gif')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    documentos = models.ManyToManyField(Documento, verbose_name='Documentos relacionados', blank=True, null=True)
    videos = models.ManyToManyField(Video, verbose_name='Videos Relacionados', blank=True, null=True)
    slug = models.SlugField(editable=False)

    fileDir = 'images/'

    class Meta:
        abstract = True
        ordering = ['-id']

class Proyecto(Base):
    titulo_galeria = models.CharField(max_length=150, blank=True, default='')
    fecha_galeria = models.DateTimeField(blank=True, default=datetime.datetime.now())
    image = generic.GenericRelation(GenericImage)
    video = generic.GenericRelation(GenericVideo)
    
    def __unicode__(self):
        return self.titulo

    def save(self):
        if not self.id:
            n = Proyecto.objects.all().count()
            self.slug = '%s-%s' % (str(n + 1), slugify(self.titulo))
        else:
            pass
        super(Proyecto, self).save()


class Campania(Base):
    titulo_galeria = models.CharField(max_length=150, blank=True, default='')
    fecha_galeria = models.DateTimeField(blank=True, default=datetime.datetime.now())
    image = generic.GenericRelation(GenericImage)
    video = generic.GenericRelation(GenericVideo)
    
    def __unicode__(self):
        return self.titulo

    def save(self):
        if not self.id:
            n = Campania.objects.all().count()
            self.slug = '%s-%s' % (str(n + 1), slugify(self.titulo))
        else:
            pass
        super(Campania, self).save()

    class Meta:
        verbose_name = 'Campaña'
        verbose_name_plural = 'Campañas'

