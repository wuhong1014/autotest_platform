#coding:utf-8
from autotest.celery import app
from script.case.modulename.flowapi.flowdemo import FlowDemo
import unittest
from django.conf import settings
from script.common import HTMLTestRunner
from script.common.readmysql import Mysql
from script.common.getconf import ConfInfo
import os,time,logging
from script.common.sendEmail import send_email
logger=logging.getLogger(__name__)
@app.task
def demo_test():
    logger.info('demo_test start........')
    suite=unittest.TestLoader().loadTestsFromTestCase(FlowDemo)
    label = time.strftime('%Y%m%d%H%M%S', time.localtime())
    path = settings.BASE_DIR + os.sep + 'result'
    filename=os.path.join(path,"flowapi_flowdemo_report_%s.html"%label)
    #写入报告
    with open(filename,'wb+') as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='demo report',description='test by HTMLTestRunner',verbosity=2)
        runner.run(suite)
    time.sleep(3)
    #存放报告地址，便于下载
    logger.info('保存报告地址。。。')
    name = 'demo_test'
    report_name = os.path.basename(filename)
    type = 'api'
    sql = "insert into report(name,path,type,create_time,update_time) values ( '%s' , '%s' , '%s' , now() , now())" % (name, report_name, type)
    conffile_name=settings.BASE_DIR+os.sep+'script/conf/conf.ini'
    option = ['host', 'port', 'user', 'password', 'db']
    db_conf=ConfInfo(conffile_name)
    mysqlconf = db_conf.get_conf('database', option)
    mysqlconf['port'] = int(mysqlconf['port'])
    mysql=Mysql(**mysqlconf)
    mysql.modify(sql)
    mysql.conn.close()
    logger.info('报告地址成功。。。')
    # #发邮件
    # to='870226460@qq.com'#可以发给多人，用逗号隔开
    # op=['mail_host','mail_port','mail_user','mail_pass']
    # mailconf=db_conf.get_conf('mail_conf',op)
    # att=filename
    # subject='你财富后台自动化测试报告--%s'%type
    # send_email(mailconf=mailconf,sender=mailconf['mail_user'],receivers=to,subject=subject,att=att)
    # logger.info('demo_test end.........')
if __name__=='__main__':
    for i in app.tasks.items():
        print (i[0])