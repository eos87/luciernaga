# -*- coding: UTF-8 -*-
from haystack.indexes import *
from haystack import site
from models import *
import datetime

class EventoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='titulo')
    contenido = CharField(model_attr='contenido')
    direccion = CharField(model_attr='direccion')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Evento.objects.all()

site.register(Evento, EventoIndex)

class NoticiaIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    titulo = CharField(model_attr='titulo')
    contenido = CharField(model_attr='contenido')
    fecha = DateField(model_attr='fecha')

    def get_queryset(self):
        return Noticia.objects.all()

site.register(Noticia, NoticiaIndex)


