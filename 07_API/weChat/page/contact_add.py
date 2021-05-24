from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import TouchActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.WeChat.weChat.page.base_page import BasePage




class ContactAdd(BasePage):

    def input_username(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys(
            "zhang")

        return self

    def set_gender(self):
        self._driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@class="android.widget.ImageView"]').click()
        self._driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()

        return self

    def input_phonenumber(self):
        self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fwi').send_keys("15074893770")

        return self

    def click_save(self):
        # 局部导入
        from app.WeChat.weChat.page.menber_invite_menu import MemberInviteMenu

        action = TouchActions(self._driver)
        # element_phone = self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/fwi')
        # action.scroll_from_element(element_phone, 0, 10000)
        action.scroll(0,100000)
        action.perform()

        self._driver.find_element(MobileBy.ID, 'com.tencent.wework:id/aj_').click()

        # save_locator = (MobileBy.XPATH, '//*[@text="保存"]')
        # WebDriverWait(self._driver, 40).until(expected_conditions.element_to_be_clickable(save_locator))
        # self._driver.find_element(*save_locator).click()
        return MemberInviteMenu(self._driver)
