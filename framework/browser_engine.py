#coding = 'uft-8'

import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

mylog = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    print("1")
    # dir1 = os.path.dirname(os.path.abspath('.'))  #注意相对路径的获取方法
    # print(dir1)
    dir = os.path.dirname(os.getcwd())
    # print(dir)
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'
    ie_driver_path = '/tools/IEDriverServer.exe'

    def __init__(self,driver):
        print("2")
        self.driver = driver

    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path,encoding='UTF-8')

        browser = config.get("browserType","browserName")
        mylog.info("你已选择了【%s】浏览器"%browser)
        url = config.get("testServer","URL")
        mylog.info("你已选择测试地址【%s】"%url)

        if browser == "Firefox":
            #driver = webdriver.Firefox(self.firefox_driver_path)
            driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
            #driver = webdriver.Firefox(r'D:\python-project\automation_framework_demo\tools\geckodriver.exe')
            #driver = webdriver.Firefox()
            mylog.info("打开火狐浏览器")

        elif browser =="Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            mylog.info("打开谷歌浏览器")
        elif browser == "IE":
            #driver = webdriver.Ie(self.ie_driver_path)
            driver = webdriver.Ie()
            #driver = webdriver.Ie(executable_path=self.ie_driver_path)
            mylog.info("打开IE浏览器")

        driver.get(url)
        mylog.info("打开url地址【%s】"%url)
        driver.maximize_window()
        mylog.info("浏览器窗口最大化")
        driver.implicitly_wait(10)
        mylog.info("智能等待10秒 implicity_wait()")
        return driver
    def quit_browser(self):
        mylog.info("现在退出和关闭浏览器")
        self.driver.quit()
