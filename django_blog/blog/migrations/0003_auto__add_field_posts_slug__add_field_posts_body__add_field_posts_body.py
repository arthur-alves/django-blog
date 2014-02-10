# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Posts.slug'
        db.add_column(u'blog_posts', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=12312, max_length=100),
                      keep_default=False)

        # Adding field 'Posts.body'
        db.add_column(u'blog_posts', 'body',
                      self.gf('markupfield.fields.MarkupField')(default=1213123, rendered_field=True),
                      keep_default=False)

        # Adding field 'Posts.body_markup_type'
        db.add_column(u'blog_posts', 'body_markup_type',
                      self.gf('django.db.models.fields.CharField')(default=12131321, max_length=30),
                      keep_default=False)

        # Adding field 'Posts._body_rendered'
        db.add_column(u'blog_posts', '_body_rendered',
                      self.gf('django.db.models.fields.TextField')(default=2123132123),
                      keep_default=False)


        # Changing field 'Posts.title'
        db.alter_column(u'blog_posts', 'title', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Posts.resumo'
        db.alter_column(u'blog_posts', 'resumo', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting field 'Posts.slug'
        db.delete_column(u'blog_posts', 'slug')

        # Deleting field 'Posts.body'
        db.delete_column(u'blog_posts', 'body')

        # Deleting field 'Posts.body_markup_type'
        db.delete_column(u'blog_posts', 'body_markup_type')

        # Deleting field 'Posts._body_rendered'
        db.delete_column(u'blog_posts', '_body_rendered')


        # Changing field 'Posts.title'
        db.alter_column(u'blog_posts', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Posts.resumo'
        db.alter_column(u'blog_posts', 'resumo', self.gf('django.db.models.fields.TextField')(max_length=1000))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        u'blog.posts': {
            'Meta': {'object_name': 'Posts'},
            '_body_rendered': ('django.db.models.fields.TextField', [], {}),
            'body': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'body_markup_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['auth.User']"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resumo': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wording': ('django.db.models.fields.TextField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']