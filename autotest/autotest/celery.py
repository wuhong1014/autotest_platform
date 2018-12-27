from __future__ import absolute_import
import  os
import django
from celery import Celery
from django.conf import settings
'''定时任务的配置文件'''
# 单独脚本调用Django内容时，需配置脚本的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autotest.settings')
django.setup('autotest')

app=Celery('autotest')
#  在settings中写配置
app.config_from_object('django.conf:settings')
# 到Django各个app下，自动发现tasks.py 任务脚本
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

if __name__=='__main__':
    pass