#coding=utf-8

from django.conf.urls import include, url
from task_submit import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'task_statistics.views.home', name='home'),

    url(r'^$', views.index, name=u'任务量'),
    url(r'submit', views.task_submit_form_page, name = u"任务量提交"),
    url(r'task_info', views.task_info_page, name = u"任务量完成信息"),
]
