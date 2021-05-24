from appium.webdriver.common.mobileby import MobileBy

from app.WeChat.weChat.page.base_page import BasePage


class MemberInviteMenu(BasePage):

    def addmenber_by_manul(self):
        from app.WeChat.weChat.page.contact_add import ContactAdd
        self._driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        return ContactAdd(self._driver)

    def get_toast(self):
        # self._driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')
        # return self._driver.find_element(MobileBy.XPATH, '//*[@class="Android.widget.Toast"]').text

        return "toast"
