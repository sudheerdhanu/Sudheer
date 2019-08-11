from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from EmployeeApp import views

urlpatterns = [

    url(r'^$',views.home,name='home'),
    url(r'^register$',views.register,name='home'),
    url(r'^login$',views.login,name='home'),
    url(r'^emp/$', views.emp),
    url(r'^show/$', views.show),
    url(r'^Accept/$', views.accept),
    url(r'^edit/(?P<id>\d+)/$', views.edit),
    url(r'^delete/(?P<id>\d+)/$', views.destroy),
]