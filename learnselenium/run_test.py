import unittest

from HtmlTestRunner import HTMLTestRunner

test_dir = r"E:\learnpython\learnpython\learnselenium"
suit = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__ == "__main__":
    # 生成html测试报告
    fp = open(r"E:\learnpython\learnpython\learnselenium\result.html", "w+")
    runner = HTMLTestRunner(stream=fp,
                            report_title="百度搜索测试报告",
                            descriptions="运行环境:win7 chorm浏览器"
                            )
    runner.run(suit)
    fp.close()