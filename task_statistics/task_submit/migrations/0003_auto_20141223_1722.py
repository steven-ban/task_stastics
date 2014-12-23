# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task_submit', '0002_auto_20141219_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_submit',
            name='sumitTime',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 17, 22, 58, 698000), verbose_name='\u63d0\u4ea4\u65f6\u95f4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task_submit',
            name='submitDay',
            field=models.DateField(default=datetime.datetime(2014, 12, 23, 17, 22, 58, 698000), verbose_name='\u63d0\u4ea4\u65e5\u671f'),
            preserve_default=True,
        ),
    ]
