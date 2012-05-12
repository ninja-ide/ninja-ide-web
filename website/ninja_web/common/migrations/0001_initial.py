# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DownloadUrl'
        db.create_table('common_downloadurl', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('os', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('common', ['DownloadUrl'])


    def backwards(self, orm):
        
        # Deleting model 'DownloadUrl'
        db.delete_table('common_downloadurl')


    models = {
        'common.downloadurl': {
            'Meta': {'object_name': 'DownloadUrl'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['common']
