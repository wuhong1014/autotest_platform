from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def login(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user']=username
            request.session.set_expiry(0)#关闭浏览器session失效
            return  redirect('/home')
        else:
            return render(request,'login.html',{'error':'username or password error!'})
    return render(request,'login.html')
@login_required(login_url='/login/')
def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')

def left(request):
    return render(request,'left.html')
def top(request):
    return render(request,'top.html')
def welcome(request):
    return render(request,'welcome.html')
