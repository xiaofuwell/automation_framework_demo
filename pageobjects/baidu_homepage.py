#coding = utf-8
#FileName:baidu_homepage.py

from framework.base_page import BasePage

class HomePage(BasePage):
    input_box = "id=>kw"
    search_subit_btn = "css_selector=>#su"
    new_link = "name=>tj_trnews"

    def input_search(self,text):
        return self.input_send(self.input_box,text)
    def send_submit_btn(self):
        return self.click(self.search_subit_btn)

    def click_news(self):
        self.click(self.new_link)
        self.sleep(3)