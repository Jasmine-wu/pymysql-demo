from appium.webdriver.common.mobileby import MobileBy

from app2.page.base_page import BasePage
from app2.page.market import Market


class Main(BasePage):
    # def goto_search(self):
    #     # self.find(MobileBy.ID, "tv_search").click()
    #     self.steps("../step/main.yaml")

    def goto_market(self):
        # 用text定位是不稳固的，比如刷新出来的内容里也出现了text的内容
        self.steps("../step/test_main.yaml")

        return Market(self._driver)
