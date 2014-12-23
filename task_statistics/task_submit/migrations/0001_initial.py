# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='monthly_task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monthlyTask', models.DecimalField(verbose_name='\u4efb\u52a1\u91cf', max_digits=4, decimal_places=2)),
                ('month', models.DateField(verbose_name='\u6708\u4efd')),
                ('theExaminer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6309\u6708\u4efb\u52a1\u91cf',
                'verbose_name_plural': '\u6309\u6708\u4efb\u52a1\u91cf',
            },
            bases=None,
        ),
        migrations.CreateModel(
            name='task_submit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yiChuAn', models.DecimalField(default=0, verbose_name='\u5df2\u51fa\u6848', max_digits=4, decimal_places=2)),
                ('xyJian', models.DecimalField(default=0, verbose_name='XY\u6848\u4ef6', max_digits=4, decimal_places=2)),
                ('daiChuAn', models.DecimalField(default=0, verbose_name='\u5f85\u51fa\u6848', max_digits=4, decimal_places=2)),
                ('xinFenDaiShen', models.DecimalField(default=0, verbose_name='\u65b0\u5206\u5f85\u5ba1', max_digits=4, decimal_places=2)),
                ('chouZhongZhiJian', models.IntegerField(default=0, verbose_name='\u62bd\u4e2d\u8d28\u68c0\uff08\u6807\u51c6\u4ef6\uff09')),
                ('yiTongBeiZhu', models.CharField(default='\u65e0', max_length=200, verbose_name='\u4e00\u901a\u5907\u6ce8\uff08\u8c03\u5242\u60c5\u51b5\uff09')),
                ('shouQuan', models.DecimalField(default=0, verbose_name='\u6388\u6743', max_digits=4, decimal_places=2)),
                ('boHui', models.DecimalField(default=0, verbose_name='\u9a73\u56de', max_digits=4, decimal_places=2)),
                ('shiChe', models.DecimalField(default=0, verbose_name='\u89c6\u64a4', max_digits=4, decimal_places=2)),
                ('jieAnBeiZhu', models.CharField(default='\u65e0', max_length=200, verbose_name='\u51fa\u6848\u5907\u6ce8\uff08\u8c03\u5242\u60c5\u51b5\uff09')),
                ('submitDay', models.DateField(default=datetime.datetime(2014, 12, 19, 15, 14, 2, 77000), verbose_name='\u63d0\u4ea4\u65e5\u671f')),
                ('theExaminer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u91cf\u63d0\u4ea4',
                'verbose_name_plural': '\u4efb\u52a1\u91cf\u63d0\u4ea4',
            },
            bases=None,
        ),
    ]
