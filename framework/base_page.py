#coding = utf-8
#FileName:base_page.py
#date:2018-10-28
#author:zhongyinfu

import time
import os.path
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger

#创建日志对象
logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self,driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info("点击当前浏览器页面的【前进】按钮")
    def back(self):
        self.driver.back()
        logger.info("点击当前浏览器页面的【后退】按钮")
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待%d 秒"%seconds)
    #点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭当前浏览器并退出")
        except NameError as e:
            logger.error("关闭浏览器失败：%s"%e)

    #保存图片
    def get_windows_img(self):
        """
        在这里直接把file_path的路径写死，直接保存到我们的项目根目录的一个文件夹screen_shots下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.'))+'/screen_shots/'
        rqtime = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        screen_name = file_path + rqtime + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("已经获取图片并保存到了screen_shots")
        except NameError as e:
            logger.error("截图失败%s"%(e))


    def find_element(self,selector):
        """
        这个地方使用了=>来切割字符串，请看页面的定位元素的方法
        submit_btn = "id=>su"
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \'%s\'sucessful by %s via value:%s"%(element.text,selector_by,selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementExcetion:%s"%e)
                self.get_windows_img()
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partialz_link_text(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info(("Had find the element \'%s\'sucessful by %s via value:%s"%(element.text,selector_by,selector_value)))
            except NoSuchElementException as e:
                logger.error("NosuchElementException:%s"%e)
                self.get_windows_img()
        elif selector_by == 's' or selector_by == 'css_selector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("css_selector 定位成功")
            except NoSuchElementException as e:
                logger.error("NosuchElementException:%s"%e)
                self.get_windows_img()
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element
    #输入
    def input_send(self,selector,text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had input_send \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()
    #清空输入框内容
    def clear(self,selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()
    #点击元素
    def click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \'%s\' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
            self.get_windows_img()
    #获取标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)