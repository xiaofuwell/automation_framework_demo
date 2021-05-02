#coding = utf-8
#FileName:iselement_exits.py

from framework.logger import Logger

mylog = Logger(logger="iselement_exist").getlog()

def is_elements_exist(driver,element):
    try:
        driver.find_element(element)
        print("---6666666666666--------")
        return True
    except Exception as e:
        print("----777777777-------")
        mylog.error("元素不存在")
        return False

