from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Test_UiAutomator1():

    def setup(self):
        disired_caps = {

            "platformName": "android",
            "platformVersion": "6.0",

            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",

            "noReset": "true",

            # "dontStopAppOnReset": "true",
            # "skipDeviceInitialization": "true",
            # "unicodeKeyboard": "true",
            # "resetKeyboard": "true"

        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", disired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        print("quit now==================")
        self.driver.quit()

    def test_uiAutomator1(self):
        """
         文档： https://developer.android.com/reference/androidx/test/uiautomator/UiSelector
            - 多属性连用查找， 语法：用.连接

        """

        # 'new UiSelector().text("我的")' 必须是单引号

        print("===============1",self.driver.context)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        login_locator = (MobileBy.XPATH, '//*[@text="登陆雪球"]')
        print("===============2",self.driver.context)


        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(login_locator))
        self.driver.find_element(*login_locator)

        # WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(login_locator))
        # self.driver.find_element(*login_locator).click()

        # 账号密码登陆 这个元素死也找不到，咋办？
        #
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().text("账号密码登陆").className("android.widget.TextView")')

        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("登陆雪球")').click()
        # print(self.driver.page_source())
        # print(self.driver.page_source)

    def test_uiautomator_scroll(self):

        self.driver.find_elements_by_android_uiautomator(
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("老柏树也有春天").'
            'instance(0));').click()
        sleep(5)
