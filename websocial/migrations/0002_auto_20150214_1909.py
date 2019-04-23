# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('websocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(null=True, blank=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, to='websocial.User', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='local_user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
    ]
