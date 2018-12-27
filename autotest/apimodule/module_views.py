from django.shortcuts import render,redirect
from django.urls import reverse
from apitest.models import Apis
from .models import Module
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
# Create your views here.
@login_required(login_url='/login/')
def module_manage(request):
    username=request.session.get('user','')
    search_modulename = request.GET.get('modulename', '')
    module_list = Module.objects.filter(modulename__icontains=search_modulename).order_by('-id')
    paginator=Paginator(module_list,10)
    currentPage=int(request.GET.get('page',1))
    try:
        module_list=paginator.page(currentPage)
    except Exception:
        module_list=paginator.page(1)
    return render(request,'module_manage.html',{'user':username,'modules':module_list,"currentPage":currentPage,'search_modulename':search_modulename })
#新增|编辑页面
@login_required(login_url='/login/')
def module_detail(request):
    username=request.session.get('user','')
    action=request.GET.get('action','')
    modules=None
    apis=None
    module_id=''
    methods=['get','post','put','delete','patch']
    if action=='add':
        pass
    elif action=='edit':
        module_id=request.GET.get('module_id','')
        modules=Module.objects.filter(id=module_id)
        apis=Apis.objects.filter(apimodule_id=module_id)
    return render(request,'module_detail.html',{'modules':modules,'apis':apis ,'user':username,'methods':methods,'module_id':module_id})
@login_required(login_url='/login/')
def module_del(request):
    module_id=request.GET.get('module_id','')
    module_del=Module.objects.filter(id=module_id)
    module_del.delete()
    return redirect(reverse('module_manage'))
@login_required(login_url='/login/')
def module_save(request):
    def is_dictjson(param):
        '''判断是字典格式的json返回True，不是json返回False'''
        if isinstance(param,str):#先判断是不是字符串
            try:
                res=json.loads(param,)
            except Exception:
                return False
            return isinstance(res,dict)
        else:
            return False

    module_id  = request.GET.get('module_id', '')
    if request.POST:
        modulename = request.POST.get('modulename', '')
        moduledesc = request.POST.get('moduledesc', '')
        moduler=request.POST.get('moduler','')
        isexec=request.POST.get('isexec','')
        print(isexec)
        apinos=request.POST.getlist('apino')
        apinames=request.POST.getlist('apiname')
        apifuncs=request.POST.getlist('apifunc')
        apiheaders=request.POST.getlist('apiheaders')
        apiurls=request.POST.getlist('apiurl')
        apimethods = request.POST.getlist('apimethod')
        apiparamvalues = request.POST.getlist('apiparamvalue')
        apiresults = request.POST.getlist('apiresult')
        apiexecs = request.POST.getlist('apiexec')
        apiids=request.POST.getlist('apiid')
        apis=map(lambda apino,apiname,apiheader,apiurl,apimethod,apiparamvalue,apiresult,apiexec ,apifunc,apiid:(apino,apiname,apiheader,apiurl,apimethod,apiparamvalue,apiresult,apiexec,apifunc,apiid),apinos,apinames,apiheaders,apiurls,apimethods,apiparamvalues,apiresults,apiexecs,apifuncs,apiids)
        if not module_id:
            Module.objects.create(modulename=modulename, moduledesc=moduledesc,moduler=moduler,isexec=isexec)
            module=Module.objects.filter(modulename=modulename)
            for api in apis:
                param={}
                headers={}
                if is_dictjson(api[5].replace("\'","\"")):
                    param=api[5].replace("\'","\"")
                if is_dictjson(api[2].replace("\'","\"")):
                    headers=api[2].replace("\'","\"")
                if api[0]:
                    Apis.objects.create(apino=api[0],apiname=api[1],apiheaders=headers,apiurl=api[3],apimethod=api[4],apiparamvalue=param,apiresult=api[6],apiexec=api[7],apifunc=api[8],apimodule_id=module[0].id)
        else:
            Module.objects.filter(id=module_id).update(modulename=modulename, moduledesc=moduledesc,moduler=moduler,isexec=isexec)
            apis_for_module = Apis.objects.filter(apimodule_id=module_id)
            if not apiids:
                Apis.objects.filter(apimodule_id=module_id).delete()

            for api in apis:
                param = {}
                headers={}

                if is_dictjson(api[2].replace("\'","\"")):
                    headers=api[2].replace("\'","\"")
                if is_dictjson(api[5].replace("\'","\"")):
                    param = api[5].replace("\'","\"")
                if not api[-1] and api[0]:

                    Apis.objects.create(apino=api[0],apiname=api[1],apiheaders=headers,apiurl=api[3],apimethod=api[4],apiparamvalue=param,apiresult=api[6],apiexec=api[7],apifunc=api[8],apimodule_id=module_id)
                elif  api[-1] and api[0]:
                    for apisfor in apis_for_module:
                        if str(api[-1])==str(apisfor.id):
                            Apis.objects.filter(id=apisfor.id).update(apino=api[0],apiname=api[1],apiheaders=headers,apiurl=api[3],apimethod=api[4],apiparamvalue=param,apiresult=api[6],apiexec=api[7],apifunc=api[8],apimodule_id=module_id)
                        if str(apisfor.id) not in apiids:
                            Apis.objects.filter(id=apisfor.id).delete()
    return redirect(reverse('module_manage'))