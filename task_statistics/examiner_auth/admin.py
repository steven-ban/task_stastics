#coding=utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import UserProfile, StudyTeam, Grade

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	fk_name = 'user'
	max_num = 1
	
class UserAdmin(UserAdmin):
	inlines = (UserProfileInline, ) # 在admin页面中操作扩展字段
#	fields = ['username', 'userProfile.nameZh', 'userProfile.examinationCode', 'userProfile.studyTeam', \
#		'userProfile.grade']
#	list_display = ('username', 'userProfile.nameZh', \
##		'userProfile.examinationCode', 'userProfile.studyTeam', \
##		'userProfile.grade'\
#		)

admin.site.register(StudyTeam)
admin.site.register(Grade)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)