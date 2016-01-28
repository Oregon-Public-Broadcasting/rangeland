# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0003_auto_20160128_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health',
            name='field_office',
        ),
        migrations.AlterField(
            model_name='health',
            name='auth_no',
            field=models.ForeignKey(to='grazing.Authorization'),
            preserve_default=True,
        ),
    ]
