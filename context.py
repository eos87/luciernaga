from multimedia.forms import *

def variables(request):
    videos_count = Video.objects.all().count()
    videoForm = VideoBuscar()
    dicc = {
            'videoForm': videoForm,
            'v_count': videos_count,
           }
    return dicc
