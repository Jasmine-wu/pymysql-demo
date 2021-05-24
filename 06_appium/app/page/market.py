from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from app.page.base_page import BasePage
from app.page.search import Search


class Market(BasePage):

    def goto_search(self):

        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self._driver.implicitly_wait(10)
        return Search(self._driver)
