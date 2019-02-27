from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import show_user

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='examiner_auth/login.html'), name='login'),
    url(r'^logout/$', auth_views.logout),
    url(r'^profile/$', show_user), 
    url(r'^$', show_user),

]
