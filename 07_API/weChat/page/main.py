from appium.webdriver.common.mobileby import MobileBy

from app.WeChat.weChat.page.addresslist_page import AddressList
from app.WeChat.weChat.page.base_page import BasePage

"""
1、_xxx     不能用于’from module import *’ 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。
2、__xxx    双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了。连子类也不可以
"""


class Main(BasePage):

    def goto_message(self):
        pass

    def goto_addresslist(self) -> AddressList:
        self._driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        return AddressList(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
