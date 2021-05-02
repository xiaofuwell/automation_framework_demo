#coding = utf-8

from framework.base_page import BasePage

class NewsHomePage(BasePage):
    sports_links = "link_text=>体育"

    def click_sports(self):
        self.click(self.sports_links)
        self.sleep(3)
