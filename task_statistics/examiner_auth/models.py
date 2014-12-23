#coding=utf-8

from django.db import models
from django.contrib.auth.models import User

class StudyTeam(models.Model):
	studyTeam = models.CharField(u'组名', max_length = 30)
	
	def __unicode__(self):
		return self.studyTeam
		
	class Meta:
		verbose_name = u'学习小组'
		verbose_name_plural = u'学习小组'
		
class Grade(models.Model):
	grade = models.CharField(u'期次', max_length = 10)
	
	def __unicode__(self):
		return self.grade
	class Meta:
		verbose_name = u'期次信息'
		verbose_name_plural = u'期次信息'

class UserProfile(models.Model):
	user = models.OneToOneField(User, blank = True, \
				null = True, related_name = 'user', \
				verbose_name = u'审查员配置', \
				)
	name = models.CharField(u'姓名（拼音）', max_length = 20)
	nameZh = models.CharField(u'姓名', max_length = 10)
	examinationCode = models.CharField(u'审查代码', max_length = 6)
	studyTeam = models.ForeignKey('StudyTeam')
	grade = models.ForeignKey('Grade')
	
	class Meta:
		verbose_name = u'审查员配置'
		verbose_name_plural = u'审查员配置'
		
	def __unicode__(self):
		return self.nameZh