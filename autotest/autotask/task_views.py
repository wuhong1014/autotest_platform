import os
from apitest import tasks#导入才能找到task中的任务名称
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from djcelery.models import IntervalSchedule,CrontabSchedule,PeriodicTask
from django.conf import settings
from autotest.celery import app
# Create your views here.
def task_manage(request):
    username = request.session.get('user', '')
    search_taskname = request.GET.get('taskname', '')
    task_search_result = PeriodicTask.objects.filter(name__icontains=search_taskname).order_by('-id')
    paginator = Paginator(task_search_result, 10)
    currentPage = int(request.GET.get('page', 1))
    try:
        task_list = paginator.page(currentPage)
    except Exception:
        task_list = paginator.page(1)
    return render(request, 'task_manage.html',
                  {'user': username, 'tasks': task_list, 'search_taskname': search_taskname, 'currentPage': currentPage})


def task_detail(request):
    username = request.session.get('user', '')
    action = request.GET.get('action', '')
    tasks = None
    task_id = ''
    crontabs = CrontabSchedule.objects.all()
    intervals = IntervalSchedule.objects.all()
    apptasknames=[]
    for appname in app.tasks.items():
        if 'celery' not in appname[0]:
            apptasknames.append(appname[0])
    if action == 'add':#由于没有找到自动获取任务名称的方法，没有加入新增功能
        pass
    elif action == 'edit':
        task_id = request.GET.get('task_id', '')
        tasks = PeriodicTask.objects.filter(id=task_id)

    return render(request, 'task_detail.html',
                  {'crontabs': crontabs, 'intervals': intervals, 'tasks': tasks,'apptasknames':apptasknames, 'user': username,
                   'task_id': task_id})


def task_del(request):
    task_id = request.GET.get('task_id', '')
    task = PeriodicTask.objects.filter(id=task_id)
    task.delete()
    return redirect(reverse('task_manage'))

def task_save(request):
    # 由于没有找到自动获取任务名称的方法，没有加入新增功能
    task_id=request.GET.get('task_id','')
    if request.POST:
        name=request.POST.get('task_name','')
        task=request.POST.get('app_task_name','')
        enabled=request.POST.get('enabled','')
        interval=request.POST.get('Interval','')
        crontab=request.POST.get('Crontab','')
        args=request.POST.get('list_arguments','')
        kwargs=request.POST.get('keyword_arguments','')
        if interval=='-1' or interval=='':
            interval_id=''
        else:
            interval_id=interval
        if crontab=='-1' or crontab=='':
            crontab_id=''
        else:
            crontab_id=crontab
        if task_id:
            PeriodicTask.objects.filter(id=task_id).update(name=name,task=task,enabled=enabled,interval_id=interval_id,crontab_id=crontab_id,args=args,kwargs=kwargs)
        else:#新增
            PeriodicTask.objects.create(name=name, task=task, enabled=enabled,interval_id=interval_id, crontab_id=crontab_id, args=args,kwargs=kwargs)
    return redirect(reverse('task_manage'))

def interval_detail(request):
    task_id=request.GET.get('task_id','')
    return render(request,'interval_detail.html',{'task_id':task_id})
def interval_save(request):
    task_id = request.GET.get('task_id', '')
    action = request.GET.get('parentaction', '')
    every=request.POST.get('every','')
    period=request.POST.get('period','')
    if action=='edit':
        IntervalSchedule.objects.get_or_create(every=every,period=period)
    return redirect('/task_detail/?action=%s&task_id=%s'%(action,task_id))
def crontab_detail(request):
    task_id = request.GET.get('task_id', '')
    return render(request, 'crontab_detail.html',{'task_id':task_id})
def crontab_save(request):
    task_id = request.GET.get('task_id', '')
    action = request.GET.get('parentaction', '')
    minute = request.POST.get('minute', '')
    hour = request.POST.get('hour', '')
    day_of_week=request.POST.get('day_of_week', '')
    day_of_month=request.POST.get('day_of_month', '')
    month_of_year=request.POST.get('month_of_year', '')
    if action=='edit':
        CrontabSchedule.objects.get_or_create(minute=minute, hour=hour,day_of_week=day_of_week,day_of_month=day_of_month,month_of_year=month_of_year)
    return redirect('/task_detail/?action=%s&task_id=%s' % (action, task_id))