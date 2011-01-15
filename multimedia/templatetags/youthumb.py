from urlparse import parse_qs
from django import template
from django.template.defaultfilters import stringfilter
import urlparse

register = template.Library()

@stringfilter
def replace(value, arg):
    return value.replace(arg, '/embed/')

@stringfilter
def id(value):
    url_data = urlparse.urlparse(value)
    query = urlparse.parse_qs(url_data.query)
    video = query["v"][0]
    return video

@stringfilter
def img(value):
    dicc = {
        0: 'cero.png',
        1: 'uno.png',
        2: 'dos.png',
        3: 'tres.png',
        4: 'cuatro.png',
        5: 'cinco.png',
        6: 'seis.png',
        7: 'siete.png',
        8: 'ocho.png',
        9: 'nueve.png',
    }
    first = value[0]
    last = value[1]
    return "<img width='28' src='/files/images/%s' alt='numeros'><img width='28' src='/files/images/%s' alt='numeros'>" % (dicc[int(first)], dicc[int(last)])

@stringfilter
def youthumbnail(value, args):
    '''returns youtube thumb url
    args s, l (small, large)'''
    qs = value.split('?')
    video_id = parse_qs(qs[1])['v'][0]

    if args == 's':
        return "http://img.youtube.com/vi/%s/2.jpg" % video_id
    elif args == 'l':
        return "http://img.youtube.com/vi/%s/0.jpg" % video_id
    else:
        return None

@stringfilter
def youtube_video_id(value):
    qs = value.split('?')
    video_id = parse_qs(qs[1])['v'][0]
    return video_id

register.filter('youthumbnail', youthumbnail)
register.filter('youtube_video_id', youtube_video_id)
register.filter('replace', replace)
register.filter('get_id', id)
register.filter('get_img', img)