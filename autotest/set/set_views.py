from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.urls import reverse

from .models import Set
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
#系统配置
@login_required(login_url='/login/')
def set_manage(request):
    username=request.session.get('user','')
    search_setname = request.GET.get('setname', '')
    currentPage=int(request.GET.get('page',1))
    set_search_result=Set.objects.filter(setname__icontains=search_setname).order_by('-id')
    paginator=Paginator(set_search_result,10)
    try:
        set_list=paginator.page(currentPage)
    except Exception:
        set_list=paginator.page(1)
    return render(request,'set_manage.html',{'user':username,'sets':set_list,'currentPage':currentPage,'search_setname':search_setname})

#新增|编辑页面
@login_required(login_url='/login/')
def set_detail(request):
    username = request.session.get('user', '')
    action = request.GET.get('action', '')
    sets = None
    set_id=''
    if action == 'add':
        pass
    elif action == 'edit':
        set_id = request.GET.get('set_id', '')
        sets = Set.objects.filter(id=set_id)
    return render(request, 'set_detail.html',{'sets': sets, 'user': username,'set_id':set_id})
@login_required(login_url='/login/')
def set_del(request):
    set_id = request.GET.get('set_id', '')
    sets = Set.objects.filter(id=set_id)
    sets.delete()
    return redirect(reverse('set_manage'))
@login_required(login_url='/login/')
def set_save(request):
    set_id = request.GET.get('set_id', '')
    if request.POST:
        setname=request.POST.get('setname','')
        setvalue=request.POST.get('setvalue','')
        if not set_id:
            Set.objects.create(setname=setname,setvalue=setvalue)
        else:
            Set.objects.filter(id=set_id).update(setname=setname,setvalue=setvalue)
    return redirect(reverse('set_manage'))

#用户管理

@login_required(login_url='/login/')
def set_user(request):
    user_list=User.objects.all()
    username=request.session.get('user','')
    search_username=request.GET.get('user_name','')
    user_search_result = User.objects.filter(username__icontains=search_username).order_by('-id')
    currentPage=int(request.GET.get('page',1))
    paginator=Paginator(user_search_result,10)
    try:
        user_list=paginator.page(currentPage)
    except Exception:
        user_list=paginator.page(1)
    return render(request,'set_user.html',{'user':username,'users':user_list,'search_username':search_username,'currentPage':currentPage})

@login_required(login_url='/login/')
def user_search(request):
    username=request.session.get('user','')
    search_username=request.GET.get('user_name','')
    user_search_result=User.objects.filter(username__icontains=search_username).order_by('-id')
    return render(request,'set_user.html',{'user':username,"users":user_search_result,'search_username':search_username})