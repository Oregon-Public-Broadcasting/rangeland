# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0004_auto_20160125_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allotment',
            old_name='allotment_id',
            new_name='allotment_unique',
        ),
        migrations.AlterField(
            model_name='allotment',
            name='amp_implement_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
