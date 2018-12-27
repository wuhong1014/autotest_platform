"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from apimodule import module_views
from apitest import apitest_views
from set import set_views
from report import report_views
from autotask import task_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login,name='login'),
    url(r'^home/',views.home,name='home'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^left/',views.left,name='left'),
    url(r'^top/',views.top,name='top'),
    url(r'^welcome/',views.welcome,name='welcome'),

    url(r'^module_manage/',module_views.module_manage,name='module_manage'),
    url(r'^module_detail/' ,module_views.module_detail,name='module_detail'),
    url(r'^module_del/',module_views.module_del,name='module_del'),
    url(r'^module_save/',module_views.module_save,name='module_save'),

    url(r'^apitest_manage/',apitest_views.apitest_manage,name='apitest_manage'),
    url(r'^apitest_detail/',apitest_views.apitest_detail,name='apitest_detail'),
    url(r'^apitest_del/',apitest_views.apitest_del,name='apitest_del'),
    url(r'^apitest_save/',apitest_views.apitest_save,name='apitest_save'),

    url(r'^apis_manage/',apitest_views.apis_manage,name='apis_manage'),
    url(r'^apis_detail/',apitest_views.apis_detail,name='apis_detail'),
    url(r'^apis_del/',apitest_views.apis_del,name='apis_del'),
    url(r'^apis_save/',apitest_views.apis_save,name='apis_save'),

    url(r'^set_manage/',set_views.set_manage,name='set_manage'),
    url(r'^set_detail/',set_views.set_detail,name='set_detail'),
    url(r'^set_del/',set_views.set_del,name='set_del'),
    url(r'^set_save/',set_views.set_save,name='set_save'),
    url(r'^user/',set_views.set_user,name='set_user'),

    url(r'^task_manage/',task_views.task_manage,name='task_manage'),
    url(r'^task_detail/',task_views.task_detail,name='task_detail'),
    url(r'^task_del/',task_views.task_del,name='task_del'),
    url(r'^task_save/',task_views.task_save,name='task_save'),
    url(r'^interval_detail/',task_views.interval_detail,name='interval_detail'),
    url(r'^crontab_detail/',task_views.crontab_detail,name='crontab_detail'),
    url(r'^interval_save/',task_views.interval_save,name='interval_save'),
    url(r'^crontab_save/',task_views.crontab_save,name='crontab_save'),

    url(r'^report_manage/(\w+)/',report_views.report_manage,name='report_manage'),
    url(r'^report_del/',report_views.report_del,name='report_del'),
    url(r'^report_download/',report_views.report_download,name='report_download'),



]
