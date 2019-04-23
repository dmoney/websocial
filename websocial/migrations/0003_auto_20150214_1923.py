# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websocial', '0002_auto_20150214_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='re_status',
            field=models.ForeignKey(related_name='re', null=True, blank=True, to='websocial.Status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='shares_status',
            field=models.ForeignKey(related_name='shares', null=True, blank=True, to='websocial.Status'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='url',
            field=models.URLField(blank=True, null=True, max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.URLField(blank=True, null=True, max_length=256),
            preserve_default=True,
        ),
    ]
