#coding=utf-8

from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.utils import timezone


from datetime import datetime
from decimal import Decimal, Context, getcontext

from task_submit.form import task_submit_form
from task_submit.models import task_submit as ts

@login_required
def show_user(request) : 
    return render_to_response('profile.html', {'user' : request.user})

