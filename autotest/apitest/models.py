from django.db import models
from apimodule.models import Module
# Create your models here.
class Apitest(models.Model):#接口流程表
    apitestmodule=models.ForeignKey(Module,verbose_name='功能模块',on_delete=models.CASCADE,)
    apitestid=models.CharField('流程用例ID',max_length=20,unique=True)
    apitestname=models.CharField('流程用例名称',max_length=256)
    apitestdesc=models.CharField('流程用例描述',max_length=512)
    apitestparamsvalue=models.CharField('参数',max_length=1000)
    apitestfunc=models.CharField('函数',max_length=20,null=True)
    apitester=models.CharField('测试负责人',max_length=16)
    apitestresult=models.CharField('预期结果',max_length=20)
    apitestexec=models.BooleanField('是否执行')
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    update_time=models.DateTimeField('更新时间',auto_now=True)

    class Meta:
        db_table = 'api_test'
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'
    def __str__(self):
        return self.apitestname




class Apis(models.Model):
    apimodule=models.ForeignKey(Module,verbose_name='功能模块',on_delete=models.CASCADE)
    apino = models.CharField('用例编号', max_length=100, unique=True)
    apiname = models.CharField('接口名称', max_length=100)
    apiurl = models.CharField('url地址', max_length=100)
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    apimethod = models.CharField('请求方法', max_length=200, default='get', choices=REQUEST_METHOD)
    apiheaders=models.CharField('headers',max_length=200,)
    apiparamvalue = models.CharField('请求参数和值', max_length=1000)
    apifunc=models.CharField('函数',max_length=20)
    apiresult = models.CharField('预期结果', max_length=200)
    apiexec = models.BooleanField('是否执行')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'single_api_test'
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一场景接口'
    def __str__(self):
        return self.apiname