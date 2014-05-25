# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'book_author', (
            (u'richtextpage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.RichTextPage'], unique=True, primary_key=True)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'book', ['Author'])

        # Adding model 'Book'
        db.create_table(u'book_book', (
            (u'richtextpage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.RichTextPage'], unique=True, primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'book', ['Book'])

        # Adding M2M table for field Authors on 'Book'
        m2m_table_name = db.shorten_name(u'book_book_Authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'book.book'], null=False)),
            ('author', models.ForeignKey(orm[u'book.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding model 'Excerpt'
        db.create_table(u'book_excerpt', (
            (u'richtextpage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.RichTextPage'], unique=True, primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Book'])),
        ))
        db.send_create_signal(u'book', ['Excerpt'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'book_author')

        # Deleting model 'Book'
        db.delete_table(u'book_book')

        # Removing M2M table for field Authors on 'Book'
        db.delete_table(db.shorten_name(u'book_book_Authors'))

        # Deleting model 'Excerpt'
        db.delete_table(u'book_excerpt')


    models = {
        u'book.author': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Author', '_ormbases': [u'pages.RichTextPage']},
            'dob': ('django.db.models.fields.DateField', [], {}),
            u'richtextpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.RichTextPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'book.book': {
            'Authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'books'", 'blank': 'True', 'to': u"orm['book.Author']"}),
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Book', '_ormbases': [u'pages.RichTextPage']},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'richtextpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.RichTextPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'book.excerpt': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'Excerpt', '_ormbases': [u'pages.RichTextPage']},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']"}),
            u'richtextpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.RichTextPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'pages.richtextpage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'RichTextPage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['book']