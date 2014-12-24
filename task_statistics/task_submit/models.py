#! /usr/bin/python
#coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import datetime

class task_submit(models.Model):
	theExaminer = models.ForeignKey(User)
	yiChuAn = models.DecimalField(u'已出案', max_digits = 4, decimal_places = 2, default = 0)
	xyJian = models.DecimalField(u'XY案件', max_digits = 4, decimal_places = 2, default = 0)
	daiChuAn = models.DecimalField(u'待出案', max_digits = 4, decimal_places = 2, default = 0)
	xinFenDaiShen = models.DecimalField(u'新分待审', max_digits = 4, decimal_places = 2, default = 0)
	chouZhongZhiJian = models.IntegerField(u'抽中质检（标准件）', default = 0)
	yiTongBeiZhu = models.CharField(u'一通备注（调剂情况）', max_length = 200, default = u'无')
	shouQuan = models.DecimalField(u'授权', max_digits = 4, decimal_places = 2, default = 0)
	boHui = models.DecimalField(u'驳回', max_digits = 4, decimal_places = 2, default = 0)
	shiChe = models.DecimalField(u'视撤', max_digits = 4, decimal_places = 2, default = 0)
	jieAnBeiZhu = models.CharField(u'出案备注（调剂情况）', max_length = 200, default = u'无')
	submitTime = models.DateTimeField(u'提交时间')
	
	def __unicode__(self):
		curtime = datetime.now().isoformat(' ');  
		return u"%s 提交于 %s" %(self.theExaminer.username, curtime)
	
	class Meta:
		verbose_name = u'任务量提交'
		verbose_name_plural = u'任务量提交'

YearChoice = ( \
		(u'2012年', 2012), \
		(u'2013年', 2013), \
		(u'2014年', 2014), \
		(u'2015年', 2015), \
		(u'2016年', 2016), \
		)
MonthChoice = ( \
		(u'一月', 1), \
		(u'二月', 2), \
		(u'三月', 3), \
		(u'四月', 4), \
		(u'五月', 5), \
		(u'六月', 6), \
		(u'七月', 7), \
		(u'八月', 8), \
		(u'九月', 9), \
		(u'十月', 10), \
		(u'十一月', 11), \
		(u'十二月', 12)\
		)
		
# monthly task
class monthly_task(models.Model):
	theExaminer = models.ForeignKey(User)
	monthlyTask = models.DecimalField(u'任务量', max_digits = 4, decimal_places = 2)
	year = models.PositiveIntegerField(u'年份', choices = YearChoice)
	month = models.PositiveIntegerField(u'月份', choices = MonthChoice)
	
	def __unicode__(self):
		return u'按月任务量'
	class Meta:
		verbose_name = u'按月任务量'
		verbose_name_plural = u'按月任务量'