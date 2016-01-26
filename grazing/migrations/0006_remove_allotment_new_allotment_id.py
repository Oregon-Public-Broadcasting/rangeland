# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0005_auto_20160126_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allotment',
            name='new_allotment_id',
        ),
    ]
