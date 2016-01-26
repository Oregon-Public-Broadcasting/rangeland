# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0006_remove_allotment_new_allotment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allotment',
            name='permitted_aums',
        ),
        migrations.RemoveField(
            model_name='allotment',
            name='susp_use_temp',
        ),
        migrations.RemoveField(
            model_name='allotment',
            name='suspended_aums',
        ),
    ]
