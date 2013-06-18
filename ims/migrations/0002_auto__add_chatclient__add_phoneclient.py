# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChatClient'
        db.create_table(u'ims_chatclient', (
            ('ch_d', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('client_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('gist', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'ims', ['ChatClient'])

        # Adding model 'PhoneClient'
        db.create_table(u'ims_phoneclient', (
            ('ph_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('client_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_number', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('gist', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'ims', ['PhoneClient'])


    def backwards(self, orm):
        # Deleting model 'ChatClient'
        db.delete_table(u'ims_chatclient')

        # Deleting model 'PhoneClient'
        db.delete_table(u'ims_phoneclient')


    models = {
        u'ims.chatclient': {
            'Meta': {'object_name': 'ChatClient'},
            'ch_d': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gist': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ims.phoneclient': {
            'Meta': {'object_name': 'PhoneClient'},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gist': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'ph_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ims']