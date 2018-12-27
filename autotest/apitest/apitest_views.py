from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from apimodule.models import Module
from .models import Apitest,Apis
import logging,json
logger=logging.getLogger(__name__)

# Create your views here.
#流程接口页面
@login_required(login_url='/login/')
def apitest_manage(request):
    username=request.session.get('user','')
    search_apitestname = request.GET.get('apitestname', '')
    apitest_search_result = Apitest.objects.filter(apitestname__icontains=search_apitestname).order_by('-id')
    paginator=Paginator(apitest_search_result,10)
    currentPage=int(request.GET.get('page',1))
    try:
        apitest_list=paginator.page(currentPage)
    except Exception:
        apitest_list=paginator.page(1)
    return render(request,'apitest_manage.html',{'user':username,'apitests':apitest_list,'currentPage':currentPage,'search_apitestname':search_apitestname})


#单一接口页面
@login_required(login_url='/login/')
def apis_manage(request):
    username=request.session.get('user','')
    search_apiname = request.GET.get('apiname', '')
    api_search_result = Apis.objects.filter(apiname__icontains=search_apiname).order_by('-id')
    paginator = Paginator(api_search_result, 10)
    currentPage = int(request.GET.get('page', 1))
    try:
        apis_list = paginator.page(currentPage)
    except Exception:
        apis_list = paginator.page(1)
    return render(request,'apis_manage.html',{'user':username,'apis':apis_list,'search_apiname':search_apiname,'currentPage':currentPage})

#新增|编辑页面
def apitest_detail(request):
    username = request.session.get('user', '')
    action = request.GET.get('action', '')
    modules  = Module.objects.all()
    apitests=None
    params=None
    apitest_id=''
    methods = ['get', 'post', 'put', 'delete', 'patch']
    if action == 'add':
        pass
    elif action == 'edit':
        apitest_id = request.GET.get('apitest_id', '')
        apitests=Apitest.objects.filter(id=apitest_id)
        params=None if not  apitests[0].apitestparamsvalue else json.loads(apitests[0].apitestparamsvalue.replace('\'','\"'))
    return render(request, 'apitest_detail.html',{'modules': modules,'apitests':apitests, 'user': username, 'methods': methods,'apitest_id':apitest_id,'params':params})

def apitest_del(request):
    apitest_id=request.GET.get('apitest_id','')
    apitest=Apitest.objects.filter(id=apitest_id)
    apitest.delete()
    return redirect(reverse('apitest_manage'))
def apitest_save(request):
    apitest_id=request.GET.get('apitest_id','')
    if request.POST:
        apitestid = request.POST.get('apitestid', '')
        module_id = request.POST.get('apitestmodule', '')
        apitestname = request.POST.get('apitestname', '')
        apitestdesc = request.POST.get('apitestdesc', '')
        apitester = request.POST.get('apitester', '')
        apitestresult = request.POST.get('apitestresult', '')
        apitestexec=request.POST.get('apitestexec','')
        apitestfunc=request.POST.get('apitestfunc','')
        apiparamvalue = {}#为空的话就是{}
        keys = request.POST.getlist('key')
        values = request.POST.getlist('value')
        if keys and values:
            apiparamvalue = json.dumps(dict(map(lambda key, value: (key, value), keys, values))).replace('\'', '\"')
        if not apitest_id:
            Apitest.objects.create(apitestid=apitestid, apitestexec=apitestexec, apitestname=apitestname,
                                   apitestdesc=apitestdesc, apitester=apitester, apitestresult=apitestresult,
                                   apitestmodule_id=module_id,apitestparamsvalue=apiparamvalue,apitestfunc=apitestfunc)
        else:
            Apitest.objects.filter(id=apitest_id).update(apitestid=apitestid, apitestexec=apitestexec,
                                                         apitestname=apitestname, apitestdesc=apitestdesc,
                                                         apitester=apitester, apitestresult=apitestresult,
                                                         apitestmodule_id=module_id,apitestparamsvalue=apiparamvalue,apitestfunc=apitestfunc)
    return redirect(reverse('apitest_manage'))

#新增|编辑页面
def apis_detail(request):
    username = request.session.get('user', '')
    action = request.GET.get('action', '')
    modules = Module.objects.all()
    methods = ['get', 'post', 'put', 'delete', 'patch']
    apis=None
    api_id=''
    params=None
    if action == 'add':
        pass
    elif action == 'edit':
        api_id = request.GET.get('api_id', '')
        apis = Apis.objects.filter(id=api_id)
        params=None if not apis[0].apiparamvalue else json.loads(apis[0].apiparamvalue.replace('\'','\"'))
    return render(request, 'apis_detail.html',
                  {'modules': modules, 'apis': apis,  'user': username,
                   'methods': methods,'api_id':api_id ,'params':params})

def apis_del(request):
    api_id = request.GET.get('api_id', '')
    apis = Apis.objects.filter(id=api_id)
    apis.delete()
    return redirect(reverse('apis_manage'))
def apis_save(request):
    def is_dictjson(param):
        '''判断是字典格式的json返回True，不是json返回False'''
        if isinstance(param,str):#先判断是不是字符串
            try:
                res=json.loads(param)
            except Exception:
                return False
            return isinstance(res,dict)
        else:
            return False
    api_id = request.GET.get('api_id', '')
    if request.POST:
        apino = request.POST.get('apino', '')
        module_id = request.POST.get('module', '')
        apiname = request.POST.get('apiname', '')
        apimethod = request.POST.get('apimethod', '')
        apiheaders=request.POST.get('headers', '')
        apiurl = request.POST.get('apiurl', '')
        apiresult = request.POST.get('apiresult', '')
        apiexec = request.POST.get('apiexec', '')
        apiparamvalue = {}
        apifunc = request.POST.get('apifunc', '')
        keys=request.POST.getlist('key')
        values=request.POST.getlist('value')
        if keys and values:
            apiparamvalue=json.dumps(dict(map(lambda key,value:(key,value),keys,values))).replace('\'','\"')
        if not is_dictjson(apiheaders.replace("\'","\"")):
            apiheaders={}#不是字典或者为空就是{}
        else:
            apiheaders=apiheaders.replace("\'","\"")
        if not api_id:
            Apis.objects.create(apino=apino, apimodule_id=module_id,apiname=apiname,apimethod=apimethod,apiheaders=apiheaders,apiurl=apiurl,apiparamvalue=apiparamvalue,apiresult=apiresult,apiexec=apiexec,apifunc=apifunc)
        else:
            Apis.objects.filter(id=api_id).update(apino=apino, apimodule_id=module_id,apiname=apiname,apimethod=apimethod,apiheaders=apiheaders,apiurl=apiurl,apiparamvalue=apiparamvalue,apiresult=apiresult,apiexec=apiexec,apifunc=apifunc)
    return redirect(reverse('apis_manage'))