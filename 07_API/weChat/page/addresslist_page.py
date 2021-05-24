from appium.webdriver.common.mobileby import MobileBy

from app.WeChat.weChat.page.base_page import BasePage
from app.WeChat.weChat.page.menber_invite_menu import MemberInviteMenu


class AddressList(BasePage):

    def add_menber(self) -> MemberInviteMenu:
        self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()

        return MemberInviteMenu(self._driver)
