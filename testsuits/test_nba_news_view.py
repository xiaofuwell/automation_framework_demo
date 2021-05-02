#coding = uft-8
#FileName:test_nba_news_view.py

from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.news_sport_home import NewSportsHome
from framework.browser_engine import BrowserEngine
import unittest
import time
import os.path

class ViewNBAList(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
    def tearDown(self):
        self.driver.quit()

    def test_view_nbalist(self):
        homepage = HomePage(self.driver)

        #homepage.click_news()
        #self.driver.find_element_by_name("tj_trnews").click()

        #配合第2种方法使用
        #nowtwindow= self.driver.current_window_handle

        self.driver.find_element_by_link_text("新闻").click()

        windowslisttest= self.driver.window_handles
        time.sleep(3)



        #第1种切换到当前页面的方法
        self.driver.switch_to.window(windowslisttest[-1])
        '''
        第2种切换页面的方法，适合2个窗口时使用

        for tt in windowslisttest:
            if tt != nowtwindow:
                self.driver.switch_to_window(tt)
                break
        '''
        print(self.driver.current_window_handle)

        #使用封装的方法
        # newshome = NewsHomePage(self.driver)
        # newshome.click_sports()

        #直接使用，不使用封装的方法
        self.driver.find_element_by_link_text("体育").click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(4)

        sportshome = NewSportsHome(self.driver)
        # sportshome.click_nba_link()
        self.driver.find_element_by_link_text("NBA赛程表").click()
        time.sleep(5)
        sportshome.get_windows_img()

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        print(windows)
        #切换当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])

        self.driver.current_window_handle
        time.sleep(4)
        #封装后的截图方法
        sportshome.get_windows_img()

        '''
        直接使用自动封装方法
        file_path = os.path.dirname(os.path.abspath('.'))+'/screen_shots/'
        rqtime = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        screen_name = file_path + rqtime + '.png'
        self.driver.get_screenshot_as_file(screen_name)
        '''




if __name__ == "__main__":
    unittest.main()