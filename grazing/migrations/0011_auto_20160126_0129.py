# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0010_auto_20160126_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='amp_implement_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
