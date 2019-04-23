# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=256)),
                ('text', models.TextField()),
                ('re_status', models.ForeignKey(null=True, to='websocial.Status', related_name='re')),
                ('shares_status', models.ForeignKey(null=True, to='websocial.Status', related_name='shares')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(unique=True, max_length=30)),
                ('url', models.URLField(max_length=256)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('following', models.ManyToManyField(to='websocial.User')),
                ('local_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(to='websocial.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(to='websocial.User'),
            preserve_default=True,
        ),
    ]
