from multimedia.forms import *

def variables(request):
    videoForm = VideoBuscar()
    dicc = {
            'videoForm': videoForm,
           }
    return dicc
