import unittest
import parameterized
import HtmlTestRunner
from commonClass.readExcel import doExcel
from commonClass.Logclass import lgtest
from commonClass.Http import http

data = doExcel.getData('666', 'listHomeworkDesc')

class MyTest(unittest.TestCase):
  @classmethod
  def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('***********************本次接口测试开始***********************')
  @classmethod
  def tearDownClass(self):
      # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
      print('***********************本次接口测试结束***********************\n\n\n')

  @parameterized.parameterized.expand(data)
  def test1(self, caseName, db,sql, url, params, Except):
        res=http.testHttp( caseName, db,sql, url, params, Except)
        if  Except=="1":
            self.assertEquals(1,1)
            lgtest.info("预期与结果相同，测试通过！")
        else:
            self.assertIn(Except,res.text,msg="预期与结果不一致，测试失败！")
            lgtest.error("预期与结果不一致，测试失败！")

if __name__ == '__main__':
    unittest.main()