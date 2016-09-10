#coding=utf-8

from django.shortcuts import render, render_to_response, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.utils import timezone


from datetime import datetime
from decimal import Decimal, Context, getcontext

from task_submit.form import task_submit_form
from task_submit.models import task_submit as ts
from task_submit.models import monthly_task as mt

# submit form
@login_required
def task_submit_form_page(request):
	form = task_submit_form(request.POST)
	if form.is_valid():
		last_update_time = ts.object.filter(\
				theExaminer = request.user).latest(\
				submitTime)
		if last_update_time.date() == timezone.now.date():
			last_update_time.delete() 
		submit = form.save(commit = False)
		#submit.full_clean()
		submit.theExaminer = reqeust.user
		submit.submitTime = timezone.now()
		submit.save()
	return render_to_response('task_submit/submit.html', \
			{'form': form, 'user' : request.user}, \
			context_instance = RequestContext(request))
		
# after submit, show info
@login_required
def task_info_page(request):
	context = {}
	# task_info = ts.objects.all().filter(ts.theExaminer == request.user).latest('submitTime')
	task_info = get_list_or_404(ts, theExaminer = request.user).lastest('submitTime')
	today = timezone.now()
	if task_info : 
		last_update = task_info.submitTime
		if ((last_update.year == today.year) and (last_update.month == today.month)) :
			# get and calc task info
			decimalContext = Context(prec = 4)	# set Decimal precision
			# yi tong
			context['yiTongRenWuLiang'] = mt.objects.all().filter(theExaminer = request.user and year == today.year and month == today.month).monthly_task
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
		else:
			# get and calc task info
			decimalContext = Context(prec = 4)	# set Decimal precision
			# yi tong
			context['yiTongRenWuLiang'] = 8.05
			context['yiChuAn'] = 0
			context['xyJian'] = 0
			context['xyLv'] = 0
			context['yiTongLv'] = decimalContext.divide(0, Decimal(8.05)) * 100
			#jie an
			context['jieAnRenWuLiang'] = 2
			context['shouQuan'] = 0
			context['boHui'] = 0
			context['shiChe'] = 0
			context['jieAnLiang'] = 0
			context['jieAnLv'] = 0 * 100
	

	return render(request, 'task_submit/task_info.html', context)
