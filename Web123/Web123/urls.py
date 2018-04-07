"""Web123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf.urls import url,include  #新增
#
#
# admin.autodiscover()
from app123 import views

# #
# urlpatterns = [
#     # path('^admin/', admin.site.urls),
#     path('index/', views.Index),
#     path('login/', views.Login),
#                ]

urlpatterns = [

    path('app123/', include('app123.urls')),
    # path('app123/',views.article_index),
    # path('users/',views.login), #登录
    # path('users/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
