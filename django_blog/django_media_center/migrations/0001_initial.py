# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageUp'
        db.create_table(u'django_media_center_imageup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_img', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'django_media_center', ['ImageUp'])


    def backwards(self, orm):
        # Deleting model 'ImageUp'
        db.delete_table(u'django_media_center_imageup')


    models = {
        u'django_media_center.imageup': {
            'Meta': {'object_name': 'ImageUp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title_img': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['django_media_center']