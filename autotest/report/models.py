from django.db import models

# Create your models here.

class Report(models.Model):
    name=models.CharField('报告名称',max_length=100)
    types = (('api', 'api'), ('ui', 'ui'), ('app', 'app'), ('other', 'other'))
    type = models.CharField('报告类型', max_length=20, default='api', null=True, choices=types)
    path=models.CharField('报告存放地址',max_length=100)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'report'
        verbose_name = '测试报告'
        verbose_name_plural = '测试报告'

    def __str__(self):
        return self.name