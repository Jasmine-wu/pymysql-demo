from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

"""
    方法-：用uiautoomator查看渲染后的元素,用MobileBy.ACCESSIBILITY_ID定位，但这种方式不兼容
    方法二：切换上来，其后所有的定位方式和selenium一样

"""


class TestHybridApp():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",

            "noReset": "true",

            # 不指定路径，就会去appium自带的默认的路径下找存在的
            "chromedriverExecutable": "./driver/测试/",
            # "dontStopAppOnReset": "true",
            "skipDeviceInitialization": "true"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hybridApp(self):
        l_trade = (By.XPATH, "//*[@text='交易']")

        # 在native app调用self.driver.window_handles就会报错
        # print("----------window1",self.driver.window_handles)

        print("----------context1",self.driver.contexts)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(l_trade))
        self.driver.find_element(*l_trade).click()

        print("----------context2",self.driver.contexts)



        # print("=================1",self.driver.page_source)
         # 这个应用webview的调试模式没打开
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # print("----------context3",self.driver.contexts)
        # print("----------window3",self.driver.window_handles)



        # print("=================2",self.driver.page_source)

        # l_kiahu = (By.XPATH, "//*[@text='A股开户']")
        #
        # WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(l_kiahu))
        # self.driver.find_element(*l_kiahu).click()
        #
        # sleep(5)
        # 用uiautomatorviewer查看可以看出交易page是webview页面，但是这里打印出来的结果却是['NATIVE_APP']，只有native

