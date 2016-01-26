# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0003_auto_20160125_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allotment',
            name='auth_no',
            field=models.ManyToManyField(to='grazing.Operator', null=True, blank=True),
            preserve_default=True,
        ),
    ]
