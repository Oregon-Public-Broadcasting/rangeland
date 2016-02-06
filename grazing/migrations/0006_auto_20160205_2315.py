# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0005_remove_health_auth_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boundary',
            name='allotment_number',
        ),
        migrations.RemoveField(
            model_name='health',
            name='causal_factors_date',
        ),
        migrations.RemoveField(
            model_name='health',
            name='description',
        ),
        migrations.RemoveField(
            model_name='health',
            name='land_health_eval_date',
        ),
        migrations.RemoveField(
            model_name='health',
            name='land_health_status',
        ),
        migrations.RemoveField(
            model_name='health',
            name='livestock_factor',
        ),
        migrations.RemoveField(
            model_name='health',
            name='nepa_date',
        ),
        migrations.RemoveField(
            model_name='health',
            name='nepa_identifier',
        ),
        migrations.RemoveField(
            model_name='health',
            name='nepa_type',
        ),
        migrations.RemoveField(
            model_name='health',
            name='permit_status',
        ),
        migrations.RemoveField(
            model_name='health',
            name='year_released',
        ),
        migrations.AddField(
            model_name='health',
            name='ecoregion1',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='ecoregion2',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='ecoregion3',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='lhs',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='lhs2007',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='lhs2012',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
