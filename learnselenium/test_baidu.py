import  unittest
import time
from selenium import webdriver
from HtmlTestRunner import  HTMLTestRunner

class Test_baidu(unittest.TestCase):
    """百度搜索测试"""
    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Chrome(r"D:\drivers\chromedriver.exe")
        cls.url = "https://www.baidu.com"
        print("class test start")

    # def setUp(self):
    #     self.dirver=webdriver.Chrome(r"D:\drivers\chromedriver.exe")
    #     self.url = "https://www.baidu.com"
    #     print("test case start")

    def baidu_search(self,sendkey):
        self.dirver.get(self.url)
        self.dirver.find_element_by_id("kw").send_keys(sendkey)
        self.dirver.find_element_by_id("su").click()
        time.sleep(2)

    def test_searchkey_unittest(self):
        """测试搜索unittest"""
        sendkey = "unittest"
        self.baidu_search(sendkey)
        self.assertEqual(self.dirver.title, sendkey+"_百度搜索")

    def test_searchkey_selenium(self):
        """测试搜索selenium"""
        sendkey = "selenium"
        self.baidu_search(sendkey)
        self.assertEqual(self.dirver.title, sendkey + "_百度搜索")

    # def test_searchkey_unittest(self):
    #     self.dirver.get(self.url)
    #     self.dirver.find_element_by_id("kw").send_keys("unittest")
    #     self.dirver.find_element_by_id("su").click()
    #     time.sleep(2)
    #     title = self.dirver.title
    #     self.assertEqual(title, "unittest_百度搜索")
    #
    # def test_searchkey_selenium(self):
    #     self.dirver.get(self.url)
    #     self.dirver.find_element_by_id("kw").send_keys("selenium")
    #     self.dirver.find_element_by_id("su").click()
    #     time.sleep(2)
    #     title = self.dirver.title
    #     self.assertEqual(title, "selenium_百度搜索")

    # def tearDown(self):
    #     print("test case finish")
    #     self.dirver.quit()

    @classmethod
    def tearDownClass(cls):
        print("class test finish")
        cls.dirver.quit()

if __name__ == "__main__":
    unittest.main()
