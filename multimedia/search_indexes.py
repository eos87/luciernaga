# -*- coding: UTF-8 -*-
from haystack.indexes import *
from haystack import site
from models import *
import datetime

class VideoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    nombre = CharField(model_attr='nombre')
    sinopsis = CharField(model_attr='sinopsis')
    produccion = CharField(model_attr='produccion')

    def get_queryset(self):
        return Video.objects.filter(publicar=True)

site.register(Video, VideoIndex)
