# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Tema.especifico'
        db.alter_column('multimedia_tema', 'especifico', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'Video.destacado'
        db.alter_column('multimedia_video', 'destacado', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'Video.color'
        db.alter_column('multimedia_video', 'color', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True))

        # Changing field 'Video.fila'
        db.alter_column('multimedia_video', 'fila', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True))

        # Changing field 'Video.creditos'
        db.alter_column('multimedia_video', 'creditos', self.gf('django.db.models.fields.TextField')(blank=True))

        # Changing field 'Video.produccion'
        db.alter_column('multimedia_video', 'produccion', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True))

        # Changing field 'Video.elenco'
        db.alter_column('multimedia_video', 'elenco', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True))

        # Changing field 'Video.anio'
        db.alter_column('multimedia_video', 'anio', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True))

        # Changing field 'Video.genero'
        db.alter_column('multimedia_video', 'genero_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Genero'], blank=True))

        # Changing field 'Video.publicar'
        db.alter_column('multimedia_video', 'publicar', self.gf('django.db.models.fields.BooleanField')(blank=True))

        # Changing field 'Video.sinopsis'
        db.alter_column('multimedia_video', 'sinopsis', self.gf('django.db.models.fields.TextField')(blank=True))

        # Changing field 'Video.derechos_autor'
        db.alter_column('multimedia_video', 'derechos_autor', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True))

        # Changing field 'Video.stand'
        db.alter_column('multimedia_video', 'stand', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True))

        # Changing field 'Video.tema'
        db.alter_column('multimedia_video', 'tema_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Tema'], blank=True))

        # Changing field 'Video.duracion'
        db.alter_column('multimedia_video', 'duracion', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True))

        # Changing field 'Video.coleccion'
        db.alter_column('multimedia_video', 'coleccion_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Coleccion'], blank=True))

        # Changing field 'Video.comentarios'
        db.alter_column('multimedia_video', 'comentarios', self.gf('django.db.models.fields.TextField')(blank=True))


    def backwards(self, orm):
        
        # Changing field 'Tema.especifico'
        db.alter_column('multimedia_tema', 'especifico', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Video.destacado'
        db.alter_column('multimedia_video', 'destacado', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Video.color'
        db.alter_column('multimedia_video', 'color', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Video.fila'
        db.alter_column('multimedia_video', 'fila', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True))

        # Changing field 'Video.creditos'
        db.alter_column('multimedia_video', 'creditos', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Video.produccion'
        db.alter_column('multimedia_video', 'produccion', self.gf('django.db.models.fields.CharField')(max_length=300))

        # Changing field 'Video.elenco'
        db.alter_column('multimedia_video', 'elenco', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'Video.anio'
        db.alter_column('multimedia_video', 'anio', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'Video.genero'
        db.alter_column('multimedia_video', 'genero_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Genero']))

        # Changing field 'Video.publicar'
        db.alter_column('multimedia_video', 'publicar', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'Video.sinopsis'
        db.alter_column('multimedia_video', 'sinopsis', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Video.derechos_autor'
        db.alter_column('multimedia_video', 'derechos_autor', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Video.stand'
        db.alter_column('multimedia_video', 'stand', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True))

        # Changing field 'Video.tema'
        db.alter_column('multimedia_video', 'tema_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Tema']))

        # Changing field 'Video.duracion'
        db.alter_column('multimedia_video', 'duracion', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Video.coleccion'
        db.alter_column('multimedia_video', 'coleccion_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Coleccion'], null=True, blank=True))

        # Changing field 'Video.comentarios'
        db.alter_column('multimedia_video', 'comentarios', self.gf('django.db.models.fields.TextField')())


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.coleccion': {
            'Meta': {'object_name': 'Coleccion'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Tema']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'multimedia.director': {
            'Meta': {'object_name': 'Director'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.formato': {
            'Meta': {'object_name': 'Formato'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'multimedia.genero': {
            'Meta': {'object_name': 'Genero'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'multimedia.idioma': {
            'Meta': {'object_name': 'Idioma'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'multimedia.informacion': {
            'Meta': {'object_name': 'Informacion'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'multimedia.subtema': {
            'Meta': {'object_name': 'Subtema'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Tema']"})
        },
        'multimedia.tema': {
            'Meta': {'object_name': 'Tema'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'especifico': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'multimedia.video': {
            'Meta': {'object_name': 'Video'},
            'anio': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'coleccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Coleccion']", 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'comentarios': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creditos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'derechos_autor': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'elenco': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'fila': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'formato_original': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Formato']", 'symmetrical': 'False', 'blank': 'True'}),
            'formatos_distribucion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'distribucion'", 'blank': 'True', 'to': "orm['multimedia.Formato']"}),
            'genero': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Genero']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pais_produccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['red.Pais']", 'symmetrical': 'False', 'blank': 'True'}),
            'paises_referidos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'referidos'", 'blank': 'True', 'to': "orm['red.Pais']"}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'produccion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'publicar': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'realizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Director']", 'symmetrical': 'False', 'blank': 'True'}),
            'sinopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'stand': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'subtema': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Subtema']", 'symmetrical': 'False', 'blank': 'True'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Tema']", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'red.pais': {
            'Meta': {'object_name': 'Pais'},
            'bandera': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['multimedia']
