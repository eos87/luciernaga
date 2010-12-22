import csv
from django.db.models import Field
from django.db.models import get_model
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from luciernaga.multimedia.models import *
from luciernaga.shortcuts import get_object_or_create

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, ** kwargs):
    csv_reader = csv.reader(unicode_csv_data, dialect=dialect, ** kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

"""def run(obj, filename):
    reader = unicode_csv_reader(open(filename))
    i = 0
    f = Field()
    for field in reader:
        size = len(field)-1
        for value in field:
            tipo = obj._meta.fields[i].get_internal_type()
            name = obj._meta.fields[i].name
            if tipo == 'ForeignKey':
                FK = obj._meta.fields[i].rel.to
                obj2 = FK.objects.get(pk=int(value))
                setattr(obj, name, obj2)
            else:
                setattr(obj, name, value)
            i=i+1 if i<size else 0
        obj.save()
    print 'Import successfull :)'"""

def run():
    filename = '/home/eos87/code/base2.csv'
    reader = unicode_csv_reader(open(filename))
    #leer linea por linea
    for field in reader:
        obj = Video()
        obj.portada = 'videos/thumbs/pendiente.png '
        obj.archivo = 'videos/prueba.flv'
        obj.user = User.objects.get(pk=1)
        obj.owner = 'luciernaga'
        if field[0] != '':
            obj.anio = field[0]
        else:
            obj.anio = '--'
        obj.codigo = field[1]
        if field[2] != 'No' or field[2] != 'no':
            obj.derechos_autor = 'si'
        else:
            obj.derechos_autor = 'no'
        obj.duracion = field[3]
        if field[4] != '':
            obj.elenco = field[4].replace(';', ',')
        #obteniendo o creando generos
        if field[5] != '':
            try:
                genero = Genero.objects.get(slug=slugify(field[5]))
            except:
                genero = Genero()
                genero.nombre = field[5]
                genero.slug = slugify(field[5])
                genero.save()
            obj.genero = genero
        else:
            obj.genero = Genero.objects.get(pk=1)

        if field[7] != '':
            if field[7] != 'Color':
                obj.color = 'blanco-negro'
            else:
                obj.color = 'color'
            #print obj.color
        
        #produccion
        if field[10] != '':
            obj.produccion = field[10].replace(';', ',')
            #print obj.produccion

        if field[13] != '':
            obj.sinopsis = field[13]

        if field[15] != '':
            obj.nombre = field[15]

        obj.save()
        print obj

        #obteniendo o creando idiomas ULTIMOS PASOS
        if field[6] != '':
            idioma = get_object_or_create(Idioma, nombre=field[6])
            obj.idioma.add(idioma)
            obj.save()

        if field[8] != '':
            lista = field[8].split(';')
            for i in lista:
                pais = get_object_or_create(Pais, nombre=i)
                obj.pais_produccion.add(pais)
                obj.save()

        if field[9] != '':
            lista = field[9].split(';')
            for i in lista:
                pais = get_object_or_create(Pais, nombre=i)
                obj.paises_referidos.add(pais)
                obj.save()
                
        if field[12] != '':
            lista = field[12].split(';')
            for i in lista:
                director = get_object_or_create(Director, nombre=i)
                obj.realizacion.add(director)
                obj.save()

        if field[14] != '':
            lista = field[14].split(';')
            for i in lista:
                if i.isupper():
                    if i != '':
                        tema = get_object_or_create(Tema, nombre=i)                        
                        obj.tema.add(tema)
                        obj.save()
                else:
                    if i != '':
                        subtema = get_object_or_create(Subtema, nombre=i)                    
                        obj.subtema.add(subtema)
                        obj.save()
                