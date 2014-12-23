#coding = utf-8

from django.contrib import admin

from task_submit.models import task_submit, monthly_task

class task_submitAdmin(admin.ModelAdmin):
	fields = ['theExaminer', 'yiChuAn', 'xyJian', 'daiChuAn', 'xinFenDaiShen', \
		'chouZhongZhiJian', 'yiTongBeiZhu', 'shouQuan', \
		'boHui', 'shiChe', 'jieAnBeiZhu', 'submitTime']
	list_display = ('theExaminer', 'yiChuAn', 'xyJian', 'daiChuAn', 'xinFenDaiShen', \
		'chouZhongZhiJian', 'yiTongBeiZhu', 'shouQuan', \
		'boHui', 'shiChe', 'jieAnBeiZhu', 'submitTime')
		
class monthly_taskAdmin(admin.ModelAdmin):
	fields = ['theExaminer', 'monthlyTask', 'month']
	list_display = ('theExaminer', 'monthlyTask', 'month')

admin.site.register(task_submit, task_submitAdmin)
admin.site.register(monthly_task, monthly_taskAdmin)

