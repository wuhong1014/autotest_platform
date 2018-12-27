from django.db import models

# Create your models here.
class Set(models.Model):
    setname=models.CharField('名称',max_length=64)
    setvalue=models.CharField('设置值',max_length=200)

    class Meta:
        verbose_name='系统配置'
        verbose_name_plural='系统配置'
        db_table='sys_set'
    def __str__(self):
        return self.setname