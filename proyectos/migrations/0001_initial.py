# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Proyecto'
        db.create_table('proyectos_proyecto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('portada', self.gf('luciernaga.thumbs.ImageWithThumbsField')(max_length=100)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('proyectos', ['Proyecto'])

        # Adding M2M table for field documentos on 'Proyecto'
        db.create_table('proyectos_proyecto_documentos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['proyectos.proyecto'], null=False)),
            ('documento', models.ForeignKey(orm['material.documento'], null=False))
        ))
        db.create_unique('proyectos_proyecto_documentos', ['proyecto_id', 'documento_id'])

        # Adding M2M table for field videos on 'Proyecto'
        db.create_table('proyectos_proyecto_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proyecto', models.ForeignKey(orm['proyectos.proyecto'], null=False)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False))
        ))
        db.create_unique('proyectos_proyecto_videos', ['proyecto_id', 'video_id'])

        # Adding model 'Campania'
        db.create_table('proyectos_campania', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('portada', self.gf('luciernaga.thumbs.ImageWithThumbsField')(max_length=100)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('proyectos', ['Campania'])

        # Adding M2M table for field documentos on 'Campania'
        db.create_table('proyectos_campania_documentos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('campania', models.ForeignKey(orm['proyectos.campania'], null=False)),
            ('documento', models.ForeignKey(orm['material.documento'], null=False))
        ))
        db.create_unique('proyectos_campania_documentos', ['campania_id', 'documento_id'])

        # Adding M2M table for field videos on 'Campania'
        db.create_table('proyectos_campania_videos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('campania', models.ForeignKey(orm['proyectos.campania'], null=False)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False))
        ))
        db.create_unique('proyectos_campania_videos', ['campania_id', 'video_id'])


    def backwards(self, orm):
        
        # Deleting model 'Proyecto'
        db.delete_table('proyectos_proyecto')

        # Removing M2M table for field documentos on 'Proyecto'
        db.delete_table('proyectos_proyecto_documentos')

        # Removing M2M table for field videos on 'Proyecto'
        db.delete_table('proyectos_proyecto_videos')

        # Deleting model 'Campania'
        db.delete_table('proyectos_campania')

        # Removing M2M table for field documentos on 'Campania'
        db.delete_table('proyectos_campania_documentos')

        # Removing M2M table for field videos on 'Campania'
        db.delete_table('proyectos_campania_videos')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'material.documento': {
            'Meta': {'ordering': "['-fecha']", 'object_name': 'Documento'},
            'archivo': ('luciernaga.multimedia.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 14, 15, 39, 55, 386740)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'tema': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Tema']", 'symmetrical': 'False'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'videos_relacionados': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Video']", 'symmetrical': 'False', 'blank': 'True'})
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
            'especifico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'multimedia.video': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Video'},
            'anio': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'archivo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'coleccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Coleccion']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'comentarios': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creditos': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'derechos_autor': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'publicar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['multimedia.Video']", 'null': 'True', 'blank': 'True'})
        },
        'proyectos.proyecto': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Proyecto'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'documentos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['material.Documento']", 'null': 'True', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['multimedia.Video']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['proyectos']
