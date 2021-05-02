#coding = utf-8

import unittest
import os.path
import sys
import testsuits
import HTMLTestRunner
import time

from testsuits.test_search01 import BaiduSearch
# from testsuits.test_search02 import BaiduSearch02
# from testsuits.test_get_page_title import GetPageTitle
# from testsuits.test_nba_news_view import  ViewNBAList

"""
方法一
addTest(测试类的类名（‘测试函数名称，就是test开头的函数’）)，
"""
# suit = unittest.TestSuite()
# suit.addTest(BaiduSearch02('test_baidu_search2'))
# suit.addTest(BaiduSearch02('test_baidu_search'))
# suit.addTest(GetPageTitle('test_get_title'))
# suit.addTest(ViewNBAList('test_view_nbalist'))

"""
方法二
unittest.makeSuite（类名称）
suit = unittest.TestSuite( unittest.makeSuite(BaiduSearch02))
"""
# a1 = unittest.makeSuite(BaiduSearch02)
# a2 = unittest.makeSuite(GetPageTitle)

"""
方法三： discover()
"""
path=os.path.dirname(os.path.abspath('.'))
print("1-222222222222222222---"+path)

#qqtest = path=os.path.dirname(os.path.abspath('.'))+'/testsuits'

path=os.path.dirname(os.path.abspath('.'))
pathdir=path+'\\testsuits'

# pathdir = os.path.join(os.getcwd(), "")
# print("2----"+pathdir)

# print("3----"+os.path.abspath(pathdir))
# print(sys.path)
# print(os.path.isdir(pathdir))
# if os.path.abspath(pathdir) in sys.path:
#     print("455555")

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")



#unittest.defaultTestLoader.discover(pathdir)

suite = unittest.defaultTestLoader.discover(pathdir,pattern ="test*.py",top_level_dir = None)
testunit=unittest.TestSuite()
for test_suite in suite:
    for meizhu in test_suite:
        testunit.addTests(meizhu)
    print(testunit)

if __name__ == "__main__":
    print("========================【TestRunner.py】main方法开始执行=============================")
    #执行测试用例，配合方法一
    # runner = unittest.TextTestRunner()
    # runner.run(suite)


    # 执行测试用例，配合方法二
    # runner = unittest.TextTestRunner()
    # runner.run(unittest.TestSuite(a1))
    # runner.run(unittest.TestSuite(a2))

    #执行测试用例，配合方法三
    # runner = unittest.TextTestResult()
    # runner.run(suite)


    #unittest.main()

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    runner.run(suite)
    fp.close()