from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# 账号admin 邮箱admin@mail.com 密码li123456789

def login(request):
	return render(request,"login.html")

def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user) #登录
			request.session['user']=username #添加浏览器cookie
			response = HttpResponseRedirect('/event_manage')
			return response
		else:
			return render(request,'login.html',{'error':'username or password error!'})

@login_required
def event_manage(request):
	username = request.session.get('user','') #读取浏览器cookie
	return render(request,"event_manage.html",{"user":username})