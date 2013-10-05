# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tag.parent'
        db.alter_column(u'timelog_tag', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelog.Tag'], null=True))

    def backwards(self, orm):

        # Changing field 'Tag.parent'
        db.alter_column(u'timelog_tag', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['timelog.Tag']))

    models = {
        u'timelog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['timelog.Tag']", 'null': 'True', 'blank': 'True'})
        },
        u'timelog.timeentry': {
            'Meta': {'object_name': 'TimeEntry'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['timelog.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['timelog']