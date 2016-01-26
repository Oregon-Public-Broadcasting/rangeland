# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0002_boundary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health',
            name='cause_not_met',
        ),
        migrations.DeleteModel(
            name='Cause',
        ),
        migrations.RemoveField(
            model_name='health',
            name='standards_not_met',
        ),
        migrations.DeleteModel(
            name='Standard',
        ),
        migrations.AddField(
            model_name='health',
            name='land_health_status',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='health',
            name='livestock_factor',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nepatype',
            name='abbr',
            field=models.CharField(max_length=4, null=True),
            preserve_default=True,
        ),
    ]
