#coding:utf8
import requests
from conf.outputlog import logger
def postReqs(url,data=None,**kwargs):
    '''post请求,返回字符串'''
    try:
        res=[]
        session=requests.Session()
        logger('info','url:'+url+' , params:'+str(data))
        html=session.post(url,data=data,**kwargs)
        if html.status_code==200:
            content=html.content
            cookies=session.cookies.get_dict()
            res.append(content)
            res.append(cookies)
            logger('info','reponse:'+str(content[:300]))
            return  res
        else:
            info= u'[resources.public.sendrequests.sendreqs.py] post请求响应失败：'+str(html.status_code)
            logger('error',info)
            return False
    except Exception,e:
        info = u'[resources.public.sendrequests.sendreqs.py] post请求异常：'+str(e)
        logger('error',info)
        return False
def getReqs(url,params=None,**kwargs):
    '''get请求，返回字符串'''
    try:
        res=[]
        session=requests.Session()
        logger('info','url:'+url+' , params:'+str(params))
        html=session.get(url,params=params,**kwargs)
        if html.status_code==200:
            content=html.content
            cookies=session.cookies.get_dict()
            res.append(content)
            res.append(cookies)
            logger('info','reponse:'+str(content[:300]))
            return  res
        else:
            info=  u'[resources.public.sendrequests.sendreqs.py] get请求响应失败：'+str(html.status_code)
            logger('error',info)
            return False
    except Exception,e:
        info=  u'[resources.public.sendrequests.sendreqs.py] get请求异常：'+str(e)
        logger('error',info)
        return False