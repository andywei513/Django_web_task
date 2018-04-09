from django.shortcuts import render,render_to_response


# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from app123.models import Article,User

#-------登录验证----------
from django.contrib import auth
from django.template import RequestContext
from django import forms
import time
#--------------------------

# def Index(request):
#     return render(request, 'login.html')


# def Login(request):
#     return render(request, 'login.html')


def article_index(request):  #文章录入系统
    article_list = Article.objects.all()
    return render(request,'article.html',{'article_list':article_list})

#-----------------------------------
#login system
#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
#注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            # return HttpResponse('regist success!!')
            return render(request, 'success.html', {'username': username})
    else:
        uf = UserForm()
    return render(request,'regist.html',{'uf':uf})



#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转
                return render(request,'index.html',{'username':username})
            else:
                #比较失败
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render(request,'login.html',{'uf':uf})

#登陆成功
def index(request):

    username = request.COOKIES.get('username','')
    return render(request,'index.html' ,{'username':username})


#退出
def logout(request):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

