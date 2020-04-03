import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_case(self):
        a = "li jian live concert"
        b = "li jian hh"
        #判断b是否在a中，不在则返回错误信息
        self.assertIn(b,a,msg = "b is not in a ")

    def tearDown(self):
        print("test finished")

if __name__ == "__main__":
    unittest.main()