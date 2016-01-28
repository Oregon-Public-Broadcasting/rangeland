# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grazing', '0004_auto_20160128_0737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health',
            name='auth_no',
        ),
    ]
