# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='auth_no',
            field=models.ForeignKey(to='grazing.Authorization'),
            preserve_default=True,
        ),
    ]
