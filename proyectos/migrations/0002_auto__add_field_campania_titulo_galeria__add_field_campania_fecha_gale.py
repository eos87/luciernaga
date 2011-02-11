# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Campania.titulo_galeria'
        db.add_column('proyectos_campania', 'titulo_galeria', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True), keep_default=False)

        # Adding field 'Campania.fecha_galeria'
        db.add_column('proyectos_campania', 'fecha_galeria', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 2, 10, 21, 42, 59, 349263), blank=True), keep_default=False)

        # Adding field 'Proyecto.titulo_galeria'
        db.add_column('proyectos_proyecto', 'titulo_galeria', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True), keep_default=False)

        # Adding field 'Proyecto.fecha_galeria'
        db.add_column('proyectos_proyecto', 'fecha_galeria', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 2, 10, 21, 42, 59, 346925), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Campania.titulo_galeria'
        db.delete_column('proyectos_campania', 'titulo_galeria')

        # Deleting field 'Campania.fecha_galeria'
        db.delete_column('proyectos_campania', 'fecha_galeria')

        # Deleting field 'Proyecto.titulo_galeria'
        db.delete_column('proyectos_proyecto', 'titulo_galeria')

        # Deleting field 'Proyecto.fecha_galeria'
        db.delete_column('proyectos_proyecto', 'fecha_galeria')


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
        'material.documento': {
            'Meta': {'object_name': 'Documento'},
            'archivo': ('luciernaga.multimedia.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 2, 10, 21, 42, 59, 299415)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Tema']", 'symmetrical': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'videos_relacionados': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Video']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'material.genericimage': {
            'Meta': {'object_name': 'GenericImage'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('luciernaga.material.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'material.genericvideo': {
            'Meta': {'object_name': 'GenericVideo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300'})
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
        'multimedia.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimedia.subtema': {
            'Meta': {'object_name': 'Subtema'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Tema']", 'null': 'True', 'blank': 'True'})
        },
        'multimedia.tema': {
            'Meta': {'object_name': 'Tema'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descripcion_material': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'archivo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'coleccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Coleccion']", 'null': 'True', 'blank': 'True'}),
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
            'genero': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Genero']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Idioma']", 'symmetrical': 'False', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pais_produccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Pais']", 'symmetrical': 'False', 'blank': 'True'}),
            'paises_referidos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'referidos'", 'blank': 'True', 'to': "orm['multimedia.Pais']"}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'produccion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'publicar': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'realizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Director']", 'symmetrical': 'False', 'blank': 'True'}),
            'sinopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stand': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'subtema': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Subtema']", 'symmetrical': 'False', 'blank': 'True'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Tema']", 'symmetrical': 'False', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'proyectos.campania': {
            'Meta': {'object_name': 'Campania'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'documentos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['material.Documento']", 'null': 'True', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_galeria': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 2, 10, 21, 42, 59, 349263)', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titulo_galeria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['multimedia.Video']", 'null': 'True', 'blank': 'True'})
        },
        'proyectos.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'documentos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['material.Documento']", 'null': 'True', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_galeria': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 2, 10, 21, 42, 59, 346925)', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'titulo_galeria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['multimedia.Video']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['proyectos']
