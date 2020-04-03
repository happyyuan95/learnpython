import unittest

from learnunittest.judgeprime import is_prime

class Test(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_case(self):
        #判断是否为真，不为真则返回msg信息
        self.assertTrue(is_prime(6),msg = "the num is not a prime")

    def tearDown(self):
        print("test finished")

if __name__ == "__main__":
    unittest.main()