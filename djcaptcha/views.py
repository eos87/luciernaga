from cStringIO import StringIO
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from models import CaptchaStore
import utils
import re, random, os

NON_DIGITS_RX = re.compile('[^\d]')
CAPTCHA_FONT_PATH = os.path.dirname(__file__) + '/fonts/ubuntu-r.ttf'
CAPTCHA_FONT_SIZE = 22
CAPTCHA_BACKGROUND_COLOR = '#c3f5cc'
CAPTCHA_FOREGROUND_COLOR = '#000000'
CAPTCHA_LETTER_ROTATION = (-35,35)

def captcha(request, key):    
    store = get_object_or_404(CaptchaStore, hashkey=key)
    text=store.code

    if CAPTCHA_FONT_PATH.lower().strip().endswith('ttf'):
        font = ImageFont.truetype(CAPTCHA_FONT_PATH, CAPTCHA_FONT_SIZE)
    else:
        font = ImageFont.load(CAPTCHA_FONT_PATH)

    size = font.getsize(text)
    size = (size[0]*2,size[1])
    image = Image.new('RGB', size , CAPTCHA_BACKGROUND_COLOR)

    try:
        PIL_VERSION = int(NON_DIGITS_RX.sub('',Image.VERSION))
    except:
        PIL_VERSION = 116

    xpos = 2
    for char in text:
        fgimage = Image.new('RGB', size, CAPTCHA_FOREGROUND_COLOR)
        charimage = Image.new('L', font.getsize(' %s ' % char), '#000000')
        chardraw = ImageDraw.Draw(charimage)
        chardraw.text((0,0), ' %s '%char, font=font, fill='#ffffff')
        if CAPTCHA_LETTER_ROTATION:
            if PIL_VERSION >= 116:
                charimage = charimage.rotate(random.randrange( *CAPTCHA_LETTER_ROTATION ), expand=0, resample=Image.BICUBIC)
            else:
                charimage = charimage.rotate(random.randrange( *CAPTCHA_LETTER_ROTATION ), resample=Image.BICUBIC)
        charimage = charimage.crop(charimage.getbbox())
        maskimage = Image.new('L', size)

        maskimage.paste(charimage, (xpos, 4, xpos+charimage.size[0], 4+charimage.size[1] ))
        size = maskimage.size
        image = Image.composite(fgimage, image, maskimage)
        xpos = xpos + 2 + charimage.size[0]

    image = image.crop((0,0,xpos+1,size[1]))        
    draw = ImageDraw.Draw(image)

    for f in utils.noise_functions():
        draw = f(draw,image)
    for f in utils.filter_functions():
        image = f(image)

    out = StringIO()
    image.save(out,"PNG")
    out.seek(0)

    response = HttpResponse()
    response['Content-Type'] = 'image/png'
    response.write(out.read())

    return response