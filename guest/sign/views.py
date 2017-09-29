from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def login(request):
	return render(request,"login.html")

def event_manage(request):
	return render(request,"event_manage.html")

def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if username == '123' and password == '123456':
			return HttpResponseRedirect('/event_manage')
		else:
			return render(request,'login.html',{'error':'username or password error!'})
