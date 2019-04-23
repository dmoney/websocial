# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websocial', '0003_auto_20150214_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='remote',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='remote',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
