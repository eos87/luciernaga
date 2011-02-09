# -*- coding: utf-8 -*-
import random

CAPTCHA_LENGTH = 5
CAPTCHA_CHALLENGE_FUNCT = 'luciernaga.djcaptcha.utils.code_generator'
CAPTCHA_CHALLENGE_FUNCT = 'luciernaga.djcaptcha.utils.code_generator'
CAPTCHA_NOISE_FUNCTIONS = ('luciernaga.djcaptcha.utils.noise_arcs','luciernaga.djcaptcha.utils.noise_dots',)
CAPTCHA_FILTER_FUNCTIONS = ('luciernaga.djcaptcha.utils.post_smooth',)
CAPTCHA_FOREGROUND_COLOR = '#000000'

def code_generator():
    chars,ret = u'abcdefghijklmnopqrstuvwxyz', u''
    for i in range(CAPTCHA_LENGTH):
        ret += random.choice(chars)
    return ret.upper(),ret

def _callable_from_string(string_or_callable):
    if callable(string_or_callable):
        return string_or_callable
    else:
        return getattr(__import__( '.'.join(string_or_callable.split('.')[:-1]), {}, {}, ['']), string_or_callable.split('.')[-1])

def get_code():
    return _callable_from_string(CAPTCHA_CHALLENGE_FUNCT)

def noise_arcs(draw,image):
    size = image.size
    draw.arc([-20,-20, size[0],20], 0, 295, fill=CAPTCHA_FOREGROUND_COLOR)
    draw.line([-20,20, size[0]+20,size[1]-20], fill=CAPTCHA_FOREGROUND_COLOR)
    draw.line([-20,0, size[0]+20,size[1]], fill=CAPTCHA_FOREGROUND_COLOR)
    return draw

def noise_dots(draw,image):
    size = image.size
    for p in range(int(size[0]*size[1]*0.1)):
        draw.point((random.randint(0, size[0]),random.randint(0, size[1])), fill=CAPTCHA_FOREGROUND_COLOR )
    return draw

def post_smooth(image):
    try:
        import ImageFilter
    except ImportError:
        from PIL import ImageFilter
    return image.filter(ImageFilter.SMOOTH)

def noise_functions():
    if CAPTCHA_NOISE_FUNCTIONS:
        return map(_callable_from_string, CAPTCHA_NOISE_FUNCTIONS)
    return list()

def filter_functions():
    if CAPTCHA_FILTER_FUNCTIONS:
        return map(_callable_from_string, CAPTCHA_FILTER_FUNCTIONS)
    return list()