# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0008_health_year_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='public_acres',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
