from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

import views

urlpatterns = [
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^profile/$', views.show_user), 
    url(r'^$', views.show_user),

]
