from  learnunittest.calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def SetUp(self):
        print("测试开始")

    def test_add(self):
        sum = Count(2,3)
        #使用断言判断add的值与5是否相当
        self.assertEqual(sum.add(),5)

    def test_add2(self):
        sum = Count(33,22)
        #判断sum的值与53不相等时fail并报错msg信息
        self.assertEqual(sum.add(), 53, msg = "sum is not equal to 55")

    def tearDown(self):
        print("测试结束")

#__name__ == __main__时表示模块可以直接使用
if __name__ == '__main__':
    #创建测试用例集
    suite = unittest.TestSuite()
    #向测试用例集中添加测试用例
    suite.addTest(TestCount("test_add2"))

 #执行测试
runner = unittest.TextTestRunner()
runner.run(suite)