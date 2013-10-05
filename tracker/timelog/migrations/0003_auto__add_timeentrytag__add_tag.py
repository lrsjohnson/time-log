# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimeEntryTag'
        db.create_table(u'timelog_timeentrytag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelog.TimeEntry'])),
        ))
        db.send_create_signal(u'timelog', ['TimeEntryTag'])

        # Adding model 'Tag'
        db.create_table(u'timelog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelog.Tag'], blank=True)),
        ))
        db.send_create_signal(u'timelog', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'TimeEntryTag'
        db.delete_table(u'timelog_timeentrytag')

        # Deleting model 'Tag'
        db.delete_table(u'timelog_tag')


    models = {
        u'timelog.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timelog.Tag']", 'blank': 'True'})
        },
        u'timelog.timeentry': {
            'Meta': {'object_name': 'TimeEntry'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'timelog.timeentrytag': {
            'Meta': {'object_name': 'TimeEntryTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timelog.TimeEntry']"})
        }
    }

    complete_apps = ['timelog']