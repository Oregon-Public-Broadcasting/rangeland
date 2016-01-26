# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0009_auto_20160126_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='amp_implement_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
