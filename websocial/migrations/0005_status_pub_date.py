# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('websocial', '0004_auto_20150216_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 16, 15, 24, 43, 85995, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
