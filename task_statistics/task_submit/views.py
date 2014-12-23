#coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from datetime import datetime
from decimal import Decimal, Context, getcontext

from task_submit.form import task_submit_form
from task_submit.models import task_submit

# Create your views here.
def index(request):
	return render_to_response('task_submit/task_submit.html')
	
# submit form
def task_submit_form_page(request):
	form = task_submit_form()
	return render_to_response('task_submit/submit.html', \
			{'form': form, 'user' : request.user}, \
			context_instance = RequestContext(request))
		
# after submit, show info
def task_info_page(request):
	context = {}
	task_info = task_submit.objects.filter(theExaminer = request.user).latest('submitTime')
	# get and calc task info
	decimalContext = Context(prec = 4)	# set Decimal precision
	# yi tong
	context['yiTongRenWuLiang'] = 8.05
	context['yiChuAn'] = task_info.yiChuAn
	context['xyJian'] = task_info.xyJian
	context['xyLv'] = task_info.xyJian / task_info.yiChuAn
	context['yiTongLv'] = decimalContext.divide(task_info.yiChuAn, Decimal(8.05)) * 100
	#jie an
	context['jieAnRenWuLiang'] = 2
	context['shouQuan'] = task_info.shouQuan
	context['boHui'] = task_info.boHui
	context['shiChe'] = task_info.shiChe
	context['jieAnLiang'] = decimalContext.add( \
				decimalContext.add(context['shouQuan'], context['boHui']), \
				context['shiChe'])
	context['jieAnLv'] = decimalContext.divide(context['jieAnLiang'], Decimal(context['jieAnRenWuLiang'])) * 100

	return render(request, 'task_submit/task_info.html', context)
