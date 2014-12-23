# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task_submit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_submit',
            name='submitDay',
            field=models.DateField(default=datetime.datetime(2014, 12, 19, 15, 18, 12, 302000), verbose_name='\u63d0\u4ea4\u65e5\u671f'),
            preserve_default=True,
        ),
    ]
