from django.contrib import admin
from django.urls import path
from django.conf.urls import url  #新增

from app123 import views



urlpatterns = [

       path('', views.login, name = 'login'),
       path('login/', views.login,name = 'login'),
       path('regist/',views.regist,name = 'regist'),
       path('index/', views.index, name='index'),
       path('logout/', views.logout, name='logout'),
       path('index/deliver/',views.deliverdata,name = 'deliver')
       # path('article_index/',views.article_index,name = 'article_index'),
]