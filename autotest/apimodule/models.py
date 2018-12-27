from django.db import models

# Create your models here.
class Module(models.Model):
    modulename=models.CharField('模块名称',max_length=64,unique=True)
    moduledesc=models.CharField('模块描述',max_length=200)
    moduler=models.CharField('模块负责人',max_length=200)
    isexec=models.BooleanField('是否执行')
    create_time=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name='模块管理'
        verbose_name_plural='模块管理'
        db_table='api_module'
    def __str__(self):
        return self.modulename