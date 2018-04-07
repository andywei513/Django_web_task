from django.contrib import admin
from django.urls import path
from django.conf.urls import url  #新增

from app123 import views



urlpatterns = [

      # path('', views.Index, name = 'index'),
       path('login/', views.login,name = 'login'),
]