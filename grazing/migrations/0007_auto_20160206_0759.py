# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0006_auto_20160205_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='allotment',
            field=models.ForeignKey(to='grazing.Allotment', null=True),
            preserve_default=True,
        ),
    ]
