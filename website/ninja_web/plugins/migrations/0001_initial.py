# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Plugin'
        db.create_table('plugins_plugin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('version', self.gf('django.db.models.fields.CharField')(max_length='32')),
            ('upload_date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('zip_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('tags', self.gf('tagging.fields.TagField')()),
        ))
        db.send_create_signal('plugins', ['Plugin'])

        # Adding model 'Vote'
        db.create_table('plugins_vote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('plugin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['plugins.Plugin'])),
            ('rate', self.gf('django.db.models.fields.DecimalField')(default=2.5, max_digits=3, decimal_places=2)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('voter_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal('plugins', ['Vote'])

        # Adding unique constraint on 'Vote', fields ['plugin', 'user']
        db.create_unique('plugins_vote', ['plugin_id', 'user_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Vote', fields ['plugin', 'user']
        db.delete_unique('plugins_vote', ['plugin_id', 'user_id'])

        # Deleting model 'Plugin'
        db.delete_table('plugins_plugin')

        # Deleting model 'Vote'
        db.delete_table('plugins_vote')


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
        'plugins.plugin': {
            'Meta': {'object_name': 'Plugin'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'upload_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': "'32'"}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'plugins.vote': {
            'Meta': {'unique_together': "(('plugin', 'user'),)", 'object_name': 'Vote'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['plugins.Plugin']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'default': '2.5', 'max_digits': '3', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'voter_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['plugins']
