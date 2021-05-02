#coding = utf-8
#Filename:desk_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re
from pykeyboard import PyKeyboard



class Desk(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://128.64.214.11/Citrix/XDWeb/auth/login.aspx"
        self.verificationErrors = []
        self.accepit_next_alert = True
        # self.k1 = PyKeyboard()



    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_id("skipWizardLink").click()
        time.sleep(2)
        name = self.driver.find_element_by_name('user')
        name.send_keys('17898077.zh')
        password = self.driver.find_element_by_name('password')
        password.send_keys('zwq1257P')
        time.sleep(2)
        driver.find_element_by_id('btnLogin').click()
        time.sleep(2)

        driver.find_element_by_id('desktopSpinner_idCitrix.MPS.Desktop.FTXKFarm.FTXK_0020_0024S6-6').click()

        time.sleep(5)
        # 默认在取消按钮上，先切换到保存文件上

        k =PyKeyboard()

        print("-111111--")

        # 默认在取消按钮上，先切换到保存文件上
        k.press_key(k.tab_key)  # 按住tab键盘
        k.release_key(k.tab_key)  # 释放tab键盘
        time.sleep(5)
        print("-2222222--")
        k.press_key(k.tab_key)  # 按住tab键盘
        k.release_key(k.tab_key)  # 释放tab键盘
        time.sleep(5)
        # 按回车键下载
        print("-3333--")

        k.press_key(k.enter_key)  # 按住enter键
        k.release_key(k.enter_key)  # 释放enter键

        print("444444444444444444444")
        # time.sleep(5)
        # 发送tab
        # k1.tab_key(k.tab_key)
        # time.sleep(5)
        # self.k1.tab_key()

        time.sleep(1000)


        # id="feedbackArea"  class="feedbackStyleError"  火狐提示：FTXK Win7云桌面 当前不可用。请尝试重新连接，如果问题仍然存在，请与系统管理员联系。
        #谷歌提示：   IE提示：
        #<div class="delayedImageNone" id="desktopSpinner_idCitrix.MPS.Desktop.FTXKFarm.FTXK_0020_0024S6-6"><!-- --></div>  class="desktopScreen"
        #driver.find_element_by_class_name('delayedImageNone').click()
        #driver.close()<div class="delayedImageNone" id="desktopSpinner_idCitrix.MPS.Desktop.FTXKFarm.FTXK_0020_0024S6-6"><!-- --></div>
        #FTXK Win7云桌面 当前不可用。请尝试重新连接，如果问题仍然存在，请与系统管理员联系
        #正在启动 FTXK Win7云桌面，请稍候。可能需要几分钟时间。 class="feedbackStyleInfo" FTXK Win7云桌面 已就绪。请再次单击图标启动。 id= feedbackArea  class="feedbackStyleInfo"

#http://128.64.214.11/Citrix/XDWeb/site/launcher.aspx?CTX_Application=Citrix.MPS.Desktop.FTXKFarm.FTXK%20%24S6-6&CTX_Token=775665E93396FEA36AFD3E2584859A86&LaunchId=1612248697773
#http://128.64.214.11/Citrix/XDWeb/site/launch.ica?CTX_Application=Citrix.MPS.Desktop.FTXKFarm.FTXK%20%24S6-6&CTX_AppFriendlyNameURLENcoded=FTXK%20Win7%e4%ba%91%e6%a1%8c%e9%9d%a2&CTX_Token=775665E93396FEA36AFD3E2584859A86&LaunchId=1612248697773



    def tearDown(self):

        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()





