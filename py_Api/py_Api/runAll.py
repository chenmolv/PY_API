import unittest
import parameterized
import HTMLTestRunner
from commonClass.readConfig import readConfig
import os
str1=readConfig.getValue('testCaseName','model')
report_path = os.path.join(os.getcwd(), "relust")
data=str1.split(",")
class test(unittest.TestCase):
 @parameterized.parameterized.expand(data)
 def testRun(self,modelName):
        suite=unittest.TestSuite()
        path=os.path.join(os.getcwd(),'testCase\\'+str(modelName)+'')
        all_cases = unittest.defaultTestLoader.discover(path, 'test_*.py')
        report_abspath = os.path.join(report_path, "result.html")
        fp = open(report_abspath, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u'自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')
        runner.run(all_cases)
if __name__ == '__main__':
    unittest.main()



