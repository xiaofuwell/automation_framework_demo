#coding = utf-8
#FileName:test_search02.py
#date:2018-10-29
#author:zhongyinfu

import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class BaiduSearch02(unittest.TestCase):

    # def setUp(self):
    #     browser = BrowserEngine(self)
    #     self.driver = browser.open_browser(self)
    # def tearDown(self):
    #     #self.driver.close()
    #     HomePage(self.driver).quit_browser()

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        #HomePage(cls.driver).quit_browser()
        cls.driver.close()
    def test_baidu_search1(self):
        """
        一定是test开头，把测试逻辑代码封装到一个test开头的方法里面
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.input_search("selenium2")
        homepage.send_submit_btn()
        homepage.sleep(4)
        homepage.get_windows_img()
        try:
            assert 'selenium' in homepage.get_page_title()
            print('[test_baidu_search1]Test Pass')
        except Exception as e:
            print('[test_baidu_search1]Test Fail.', format(e))

    def test_baidu_search2(self):
        homepage = HomePage(self.driver)
        homepage.input_search("python")
        homepage.send_submit_btn()
        homepage.sleep(4)
        homepage.get_windows_img()
        try:
            assert 'python' in homepage.get_page_title()
            print("[test_baidu_search2]Test Pass")
        except Exception as e:
            print("[test_baidu_search2]Test Fail")



if __name__ == '__main__':
    unittest.main()