#coding:utf-8
import unittest
import ddt
import json
import logging
import os
from script.casescript.flowapi.flowapitest import flowapitest
from script.common.getconf import ConfInfo
from script.common.readmysql import Mysql
from script.common.sendEmail import send_email

logger=logging.getLogger('script')
#获取数据
path=os.path.dirname(os.path.abspath(__file__))
#confPath=os.path.split(os.path.split(os.path.split(path)[0])[0])[0]+'/conf/conf.ini'
confPath=os.path.abspath(os.path.join(path,'../../..'))+'/conf/conf.ini'
db_conf=ConfInfo(confPath)
option = ['host', 'port', 'user', 'password', 'db']
mysqlconf=db_conf.get_conf('database',option)
mysqlconf['port'] = int(mysqlconf['port'])
module_sql="select id from api_module where isexec=1 and modulename='%s'"%('测试模块')
mysql=Mysql(**mysqlconf)
moduleid_res=mysql.query(module_sql)
moduleid='' if not  moduleid_res else moduleid_res[0][0]
test_sql="select apitestid,apitestname,apitestdesc,apitestparamsvalue,apitestresult,apitestfunc from api_test where apitestexec=1 and apitestmodule_id =%s"%(moduleid)
params=mysql.query(test_sql)
mysql.conn.close()
test_test_params=[]
for param in params:
    if param[-1]=='test_test':
        test_test_params.append(param)
@ddt.ddt
class FlowDemo(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data(*test_test_params)
    def test_test(self,data):
        logger.info('用例执行开始，用例编号：%s，用例名称：%s，用例描述：%s，用例参数：%s'%(data[0],data[1],data[2],data[3]))
        dict_data=json.loads(data[3])
        res=flowapitest(**dict_data)
        if res==data[4]:
            pass
        else:
            raise AssertionError('Fail， 预期结果：%s,实际结果：%s'%(str(data[4]),str(res)))
if __name__=='__main__':
    #unittest.main()
    from script.common import HTMLTestRunner
    import time
    suite = unittest.TestLoader().loadTestsFromTestCase(FlowDemo)
    label = time.strftime('%Y%m%d%H%M%S', time.localtime())
    path = 'D:\\autotest\\result'
    filename = os.path.join(path, "%s_report.html" % label)
    with open(filename, 'wb+') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='demo report', description='test by HTMLTestRunner',
                                               verbosity=2)
        runner.run(suite)
    time.sleep(3)
    # 存放报告地址，便于下载
    logger.info('保存报告地址。。。')
    mysql = Mysql(**mysqlconf)
    name = 'demo_test'
    report_name = os.path.basename(filename)
    type = 'api'
    sql = "insert into report(name,path,type,create_time,update_time) values ( '%s' , '%s' , '%s' , now() , now())" % (name, report_name, type)
    mysql.modify(sql)
    mysql.conn.close()
    logger.info('报告地址成功。。。')
    # # 发邮件
    # to = '870226460@qq.com'  # 可以发给多人，用逗号隔开
    # op = ['mail_host', 'mail_port', 'mail_user', 'mail_pass']
    # mailconf = db_conf.get_conf('mail_conf', op)
    # att = filename
    # subject = '你财富后台自动化测试报告--%s' % type
    # send_email(mailconf=mailconf, sender=mailconf['mail_user'], receivers=to, subject=subject, att=att)
    # logger.info('demo_test end.........')
