#coding = utf-8

from framework.base_page import BasePage

class NewSportsHome(BasePage):

    nba_link = "link_text=>NBA赛程表"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(3)