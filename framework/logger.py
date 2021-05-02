#coding = utf-8
#date:2018-10-28
#FileName:logger.py
#author:zhongyinfu

import time
import os.path
import logging

class Logger(object):

    def __init__(self,logger):

        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入指定的文件
        """
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler ,用于写入日志文件

        rqtime = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        #print("one:"+log_path)

        lp = os.path.dirname(os.getcwd())
        #print("two:"+lp)
        log_name = log_path + rqtime + '.log'
        print(log_name)
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #创建另一个handler,用于输出到控制台

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__ == "__main__":
    # Logger("test")
    mylog = Logger(logger="BrowserEngine").getlog()
    mylog.debug("打开IE浏览器")
