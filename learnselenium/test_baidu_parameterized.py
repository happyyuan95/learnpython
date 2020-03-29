import  unittest
import time
from selenium import webdriver
from parameterized import parameterized

class Test_baidu(unittest.TestCase):
    """百度搜索测试"""
    @classmethod
    def setUpClass(cls):
        cls.dirver = webdriver.Chrome(r"D:\drivers\chromedriver.exe")
        cls.url = "https://www.baidu.com"
        print("class test start")

    def baidu_search(self,sendkey):
        self.dirver.get(self.url)
        self.dirver.find_element_by_id("kw").send_keys(sendkey)
        self.dirver.find_element_by_id("su").click()
        time.sleep(2)

    # def test_searchkey_unittest(self):
    #     """测试搜索unittest"""
    #     sendkey = "unittest"
    #     self.baidu_search(sendkey)
    #     self.assertEqual(self.dirver.title, sendkey+"_百度搜索")
    #
    # def test_searchkey_selenium(self):
    #     """测试搜索selenium"""
    #     sendkey = "selenium"
    #     self.baidu_search(sendkey)
    #     self.assertEqual(self.dirver.title, sendkey + "_百度搜索")

    @parameterized.expand([
        ("case1", "selenium"),
        ("case2", "unittest"),
        ("case3", "parameterized"),
    ])
    def test_search(self, name, senkey):
        self.baidu_search(senkey)
        self.assertEqual(self.dirver.title, senkey+"_百度搜索")

    @classmethod
    def tearDownClass(cls):
        print("class test finish")
        cls.dirver.quit()


if __name__ == "__main__":
    #unittest.main()
    unittest.main(verbosity=2)