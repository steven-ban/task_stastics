#coding=utf-8

from django.forms import ModelForm
from task_submit.models import task_submit

class task_submit_form(ModelForm):
	class Meta:
		model = task_submit
		fields = ('yiChuAn', 'xyJian', 'daiChuAn', 'xinFenDaiShen', 'chouZhongZhiJian', \
				'yiTongBeiZhu', 'shouQuan', 'boHui', 'shiChe', 'jieAnBeiZhu')