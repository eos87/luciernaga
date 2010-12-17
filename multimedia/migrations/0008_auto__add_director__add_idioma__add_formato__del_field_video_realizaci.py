# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Director'
        db.create_table('multimedia_director', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('multimedia', ['Director'])

        # Adding model 'Idioma'
        db.create_table('multimedia_idioma', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('multimedia', ['Idioma'])

        # Adding model 'Formato'
        db.create_table('multimedia_formato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('multimedia', ['Formato'])

        # Deleting field 'Video.realizacion'
        db.delete_column('multimedia_video', 'realizacion')

        # Adding field 'Video.duracion'
        db.add_column('multimedia_video', 'duracion', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)

        # Adding field 'Video.color'
        db.add_column('multimedia_video', 'color', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)

        # Adding field 'Video.elenco'
        db.add_column('multimedia_video', 'elenco', self.gf('django.db.models.fields.CharField')(default='', max_length=250), keep_default=False)

        # Adding field 'Video.creditos'
        db.add_column('multimedia_video', 'creditos', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Video.derechos_autor'
        db.add_column('multimedia_video', 'derechos_autor', self.gf('django.db.models.fields.CharField')(default='', max_length=10), keep_default=False)

        # Adding field 'Video.comentarios'
        db.add_column('multimedia_video', 'comentarios', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Video.stand'
        db.add_column('multimedia_video', 'stand', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True), keep_default=False)

        # Adding field 'Video.fila'
        db.add_column('multimedia_video', 'fila', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True), keep_default=False)

        # Adding field 'Video.publicar'
        db.add_column('multimedia_video', 'publicar', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding M2M table for field realizacion on 'Video'
        db.create_table('multimedia_video_realizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False)),
            ('director', models.ForeignKey(orm['multimedia.director'], null=False))
        ))
        db.create_unique('multimedia_video_realizacion', ['video_id', 'director_id'])

        # Adding M2M table for field pais_produccion on 'Video'
        db.create_table('multimedia_video_pais_produccion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False)),
            ('pais', models.ForeignKey(orm['red.pais'], null=False))
        ))
        db.create_unique('multimedia_video_pais_produccion', ['video_id', 'pais_id'])

        # Adding M2M table for field paises_referidos on 'Video'
        db.create_table('multimedia_video_paises_referidos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False)),
            ('pais', models.ForeignKey(orm['red.pais'], null=False))
        ))
        db.create_unique('multimedia_video_paises_referidos', ['video_id', 'pais_id'])

        # Adding M2M table for field formato_original on 'Video'
        db.create_table('multimedia_video_formato_original', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False)),
            ('formato', models.ForeignKey(orm['multimedia.formato'], null=False))
        ))
        db.create_unique('multimedia_video_formato_original', ['video_id', 'formato_id'])

        # Adding M2M table for field formatos_distribucion on 'Video'
        db.create_table('multimedia_video_formatos_distribucion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['multimedia.video'], null=False)),
            ('formato', models.ForeignKey(orm['multimedia.formato'], null=False))
        ))
        db.create_unique('multimedia_video_formatos_distribucion', ['video_id', 'formato_id'])


    def backwards(self, orm):
        
        # Deleting model 'Director'
        db.delete_table('multimedia_director')

        # Deleting model 'Idioma'
        db.delete_table('multimedia_idioma')

        # Deleting model 'Formato'
        db.delete_table('multimedia_formato')

        # Adding field 'Video.realizacion'
        db.add_column('multimedia_video', 'realizacion', self.gf('django.db.models.fields.CharField')(default=1, max_length=200), keep_default=False)

        # Deleting field 'Video.duracion'
        db.delete_column('multimedia_video', 'duracion')

        # Deleting field 'Video.color'
        db.delete_column('multimedia_video', 'color')

        # Deleting field 'Video.elenco'
        db.delete_column('multimedia_video', 'elenco')

        # Deleting field 'Video.creditos'
        db.delete_column('multimedia_video', 'creditos')

        # Deleting field 'Video.derechos_autor'
        db.delete_column('multimedia_video', 'derechos_autor')

        # Deleting field 'Video.comentarios'
        db.delete_column('multimedia_video', 'comentarios')

        # Deleting field 'Video.stand'
        db.delete_column('multimedia_video', 'stand')

        # Deleting field 'Video.fila'
        db.delete_column('multimedia_video', 'fila')

        # Deleting field 'Video.publicar'
        db.delete_column('multimedia_video', 'publicar')

        # Removing M2M table for field realizacion on 'Video'
        db.delete_table('multimedia_video_realizacion')

        # Removing M2M table for field pais_produccion on 'Video'
        db.delete_table('multimedia_video_pais_produccion')

        # Removing M2M table for field paises_referidos on 'Video'
        db.delete_table('multimedia_video_paises_referidos')

        # Removing M2M table for field formato_original on 'Video'
        db.delete_table('multimedia_video_formato_original')

        # Removing M2M table for field formatos_distribucion on 'Video'
        db.delete_table('multimedia_video_formatos_distribucion')


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
            'especifico': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'multimedia.video': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Video'},
            'anio': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'coleccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Coleccion']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comentarios': ('django.db.models.fields.TextField', [], {}),
            'creditos': ('django.db.models.fields.TextField', [], {}),
            'derechos_autor': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'duracion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'elenco': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fila': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'formato_original': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Formato']", 'symmetrical': 'False'}),
            'formatos_distribucion': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'distribucion'", 'symmetrical': 'False', 'to': "orm['multimedia.Formato']"}),
            'genero': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Genero']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pais_produccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['red.Pais']", 'symmetrical': 'False'}),
            'paises_referidos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'referidos'", 'symmetrical': 'False', 'to': "orm['red.Pais']"}),
            'portada': ('luciernaga.thumbs.ImageWithThumbsField', [], {'max_length': '100'}),
            'produccion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'publicar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'realizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Director']", 'symmetrical': 'False'}),
            'sinopsis': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'stand': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subtema': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['multimedia.Subtema']", 'symmetrical': 'False'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimedia.Tema']"}),
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
