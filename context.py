from multimedia.forms import *
import datetime

def variables(request):
    temas_material = []
    videos_count = Video.objects.filter(publicar=True).count()
    videoForm = VideoBuscar()
    for tema in Tema.objects.all():
        if tema.has_material():
            temas_material.append(tema)

    dicc = {
            'videoForm': videoForm,
            'v_count': videos_count,
            'temas_material': temas_material,
            'date': datetime.datetime.now(),
            'infos': Informacion.objects.all().exclude(slug='intro'),
            'temasall': Tema.objects.all(),
            'temas': Tema.objects.filter(especifico=True)
           }
    return dicc
