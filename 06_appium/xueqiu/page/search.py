from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from app2.page.base_page import BasePage


class Search(BasePage):
    def search(self, company, code):
        self._params["company"] = company
        self._params["code"] = code

        # xpath慢，但是web,android,ios都适用

        self.steps("../step/test_search.yaml")
        if self.is_choose():
            self.reset()
        self.add()

    def add(self):
        self.steps("../step/test_search.yaml")

    def is_choose(self):
        return self.steps("../step/test_search.yaml")

    def reset(self):
        self.steps("../step/test_search.yaml")

    def get_toast_text(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text
