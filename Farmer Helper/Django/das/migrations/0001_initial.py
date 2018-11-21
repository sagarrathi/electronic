# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChartDb'
        db.create_table('das_chartdb', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sd', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rtc', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dht', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('month', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hour', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sec', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hum', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('temp', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rain', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('soil', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('light', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('hour_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('day_time', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('full_time', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('das', ['ChartDb'])


    def backwards(self, orm):
        # Deleting model 'ChartDb'
        db.delete_table('das_chartdb')


    models = {
        'das.chartdb': {
            'Meta': {'object_name': 'ChartDb'},
            'day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'day_time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dht': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'full_time': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hour': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hour_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'light': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rain': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rtc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sec': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'soil': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['das']