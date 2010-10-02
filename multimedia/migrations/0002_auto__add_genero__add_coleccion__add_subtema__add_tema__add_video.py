# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Genero'
        db.create_table('multimedia_genero', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('multimedia', ['Genero'])

        # Adding model 'Coleccion'
        db.create_table('multimedia_coleccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('tema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Tema'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('multimedia', ['Coleccion'])

        # Adding model 'Subtema'
        db.create_table('multimedia_subtema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Tema'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('multimedia', ['Subtema'])

        # Adding model 'Tema'
        db.create_table('multimedia_tema', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('especifico', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('multimedia', ['Tema'])

        # Adding model 'Video'
        db.create_table('multimedia_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('portada', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('archivo', self.gf('luciernaga.multimedia.customfilefield.ContentTypeRestrictedFileField')(max_length=100)),
            ('sinopsis', self.gf('django.db.models.fields.TextField')()),
            ('realizacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('produccion', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('anio', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('tema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Tema'])),
            ('genero', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Genero'])),
            ('coleccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimedia.Coleccion'], null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('multimedia', ['Video'])

        # Adding M2M table for field subtema on 'Video'
        db.create_table('multimedia_video_subtema', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False)),
            ('subtema', models.ForeignKey(orm['multimedia.subtema'], null=False))
        ))
        db.create_unique('multimedia_video_subtema', ['video_id', 'subtema_id'])


    def backwards(self, orm):
        
        # Deleting model 'Genero'
        db.delete_table('multimedia_genero')

        # Deleting model 'Coleccion'
        db.delete_table('multimedia_coleccion')

        # Deleting model 'Subtema'
        db.delete_table('multimedia_subtema')

        # Deleting model 'Tema'
        db.delete_table('multimedia_tema')

        # Deleting model 'Video'
        db.delete_table('multimedia_video')

        # Removing M2M table for field subtema on 'Video'
        db.delete_table('multimedia_video_subtema')


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
        'multimedia.genero': {
            'Meta': {'object_name': 'Genero'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'multimedia.video': {
            'Meta': {'object_name': 'Video'},
            'anio': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'archivo': ('luciernaga.multimedia.customfilefield.ContentTypeRestrictedFileField', [], {'max_length': '100'}),
            'coleccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Coleccion']", 'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Genero']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'portada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'produccion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'realizacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sinopsis': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'subtema': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Subtema']", 'symmetrical': 'False'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Tema']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['multimedia']
