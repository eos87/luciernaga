from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from luciernaga.multimedia.models import *
from xml.etree import ElementTree as ET

class Command(BaseCommand):

    help = "Whatever you want to print here"

    def handle(self, ** options):
        run()

def run():
    file = '/home/eos87/code/salida.xml'
    try:
        tree = ET.parse(file)
    except Exception, inst:
        print "Unexpected error opening %s: %s" % (xml_file, inst)
        return

    root = tree.getroot()
    elems = root.findall('ROW')
    for e in elems:
        id = e.getchildren()[0].find('DATA').text
        value = e.getchildren()[1].find('DATA').text
        if id != None:
            try:
                pk = str(int(id))
                objs = Video.objects.filter(codigo=pk)[:1]
            except:
                objs = Video.objects.filter(codigo=id)[:1]
            for obj in objs:
                if value != None:
                    obj.sinopsis = value
                else:
                    obj.sinopsis = 'pendiente'
                obj.save()
        