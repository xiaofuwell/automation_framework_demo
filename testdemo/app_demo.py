#coding=utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1' #4.4.2
desired_caps['deviceName'] = '8fad77e2' #8fad77e2  127.0.0.1:62001  com.tencent.mm/.ui.LauncherUI  com.yunbao.browser/org.chromium.android_webview.services.VariationsSeedServer
desired_caps['appPackage'] = 'com.boqianyi.havefun'
desired_caps['appActivity'] = 'com.kuwan.live.ui.splash.SplashActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(20)

#点击连麦
# lm = driver.find_element_by_id("com.boqianyi.havefun:id/tab_plaza_text")
# lm.click()
print("-----------------")
print(driver.get_window_size())


time.sleep(5)
print("-----3333333333------------")
#后台休息10秒

driver.background_app(10)

time.sleep(10)

driver.quit()