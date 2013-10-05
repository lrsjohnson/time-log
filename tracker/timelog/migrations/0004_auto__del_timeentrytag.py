# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TimeEntryTag'
        db.delete_table(u'timelog_timeentrytag')

        # Adding M2M table for field tags on 'TimeEntry'
        m2m_table_name = db.shorten_name(u'timelog_timeentry_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('timeentry', models.ForeignKey(orm[u'timelog.timeentry'], null=False)),
            ('tag', models.ForeignKey(orm[u'timelog.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['timeentry_id', 'tag_id'])


    def backwards(self, orm):
        # Adding model 'TimeEntryTag'
        db.create_table(u'timelog_timeentrytag', (
            ('time_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelog.TimeEntry'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'timelog', ['TimeEntryTag'])

        # Removing M2M table for field tags on 'TimeEntry'
        db.delete_table(db.shorten_name(u'timelog_timeentry_tags'))


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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['timelog.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['timelog']