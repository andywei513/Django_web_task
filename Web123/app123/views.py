from django.shortcuts import render,render_to_response


# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

from app123.models import Article,User

#-------登录验证----------
from django.contrib import auth
from django.template import RequestContext
from django import forms
import time
import sqlite3
from django.http import JsonResponse
import json
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

def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

def deliverdata(request):
    if request.method == 'GET' and request.GET.get('data') == '1':
        dictd = {}
        con = sqlite3.connect('andy.db')
        # con.row_factory = dict_factory
        cur = con.cursor()
        cur.execute('select stockname,roe from profit limit 20')
        data = cur.fetchall()
        # data = data[1:3]
        con.commit()
        con.close()
        # return data
        # data = {"stockname":["a","b","c"],"roe":[100,123,99]}
        dt = {}
        for (m, n) in data:
            dt.setdefault(m, []).append(n)

        stockname = []
        roe = []
        for i in dt.keys():
            stockname.append(i)
            roe.append(dt[i])
        # roe =np.array(roe)
        # roe2 = roe.tolist()

        mb = []
        for i in roe:
            m = i[0]
            mb.append(m)

        dictd = {"stockname": stockname, "roe": mb}

        return JsonResponse( dictd, safe=False, json_dumps_params={'ensure_ascii': False})
        # return JsonResponse(data,safe=False)
    return render(request,dictd)