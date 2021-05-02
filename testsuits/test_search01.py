#coding = utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):

    # def setUp(self):
    #     """
    #     测试固件的setUp() 的代码，主要是测试的前提准备工作
    #     :return:
    #     """
    #     browser = BrowserEngine(self)
    #     self.driver = browser.open_browser(self)
    # def tearDown(self):
    #     """
    #     测试结束后的操作，这里基本上都是关闭浏览器
    #     :return:
    #     """
    #     self.driver.quit()

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_baidu_search(self):

        homepage = HomePage(self.driver)
        homepage.input_search("selenium1")

        #self.driver.find_element_by_id("kw").send_keys("selenium1")
        time.sleep(1)
        #self.driver.find_element_by_css_selector("#su").click()
        homepage.send_submit_btn()
        time.sleep(2)
        try:
            assert 'selenium' in self.driver.title
            print("Test Pass")
        except Exception as e:
            print("Test Fail",format(e))

    if __name__ == '__main__':
        unittest.main()