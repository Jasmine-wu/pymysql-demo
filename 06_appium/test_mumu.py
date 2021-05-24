from appium import webdriver
from time import sleep
import pytest
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from hamcrest import *
from hamcrest import greater_than

"""
    技术点：
        - 用例参数化
        - 显示等待WebDriverWait的两种表达方式
        - 断言框架hamcrest
        - MobileBy
        - 获取元素属性和方法
        - 类型转换
        - 高级定位技巧：xpath子节点定位父节点
        - 高级定位技巧：uiautomator
        - setuo_class的使用

"""


class Test_XueQiu():

    def setup_class(self):
        disired_caps = {

            "platformName": "android",
            "platformVersion": "6.0",

            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",

            # 启动app是否重置设置，比如弹框和登陆，false每次启动都会要重新登陆，重点隐私条款等。
            "noReset": "true",

            # 每次启动app都会从app停止的地方开始，需要跟back()联合使用，测试用例执行完回到测试用例执行最开的地方
            "dontStopAppOnReset": "true",

            # 跳过安装，权限设置等等操作
            # 当测试用例庞大，效果更好
            "skipDeviceInitialization": "true",
            "skipServerInstallation": "true"


            # 如果想键盘输入中文，要把这两个都设置为true
            # "unicodeKeyboard": "true",
            # "resetKeyboard": "true"

        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", disired_caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def setup(self):
        pass

    def teardown(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='取消']").click()


    @pytest.mark.parametrize("search_name, code, expect_price", (
            ('阿里巴巴', '09988', 220),
            ('搜狗', 'SOGO', 8)

    ))
    def test_search(self, search_name, code, expect_price):
        search_locator = (MobileBy.ID, "com.xueqiu.android:id/tv_search")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(search_locator))
        self.driver.find_element(*search_locator).click()

        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(search_name).click()

        element_click = self.driver.find_element(MobileBy.XPATH, "//*[@text='{}']/../..".format(code))

        # 获取属性，可查看appium-automator2源码
        if element_click.get_attribute("clickable"):
            element_click.click()

        """
        MobileBy: 比By增加了移动端的东西
        from appium.webdriver.common.mobileby import MobileBy
        
        WebDriverWait：
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions
        
        传入一个定位器locator：visibility_of_element_located(locator)
        presence_of_element_located 只能判断该元素在dom树中
        
        """
        # 找到代码09988这只股票的价格
        # 使用Xpath，通过父节点定位子元素
        locator = (
        MobileBy.XPATH, "//*[@text='{}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']".format(code))

        # 方法1：
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # element_price = self.driver.find_element(*locator)

        # 方法2：
        element_price = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))

        # 在expect_price 上下浮动10%
        assert_that(float(element_price.text), close_to(expect_price, expect_price * 0.1))



    @pytest.mark.skip
    def test_touchAction(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        #  touchChain
        """
            屏幕适配
        """
        price = self.driver.find_element_by_xpath(
            "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text

        window_rec = self.driver.get_window_rect()

        window_width = window_rec["width"]
        window_height = window_rec["height"]

        x_start = int(window_width / 2)
        y_start = int(window_height * 4 / 5)
        y_end = int(window_height * 1 / 5)

        if price.is_displayed():
            action = TouchAction(self.driver)
            #  手势滑动
            """
            wait(200) 暂停200ms
            """
            action.press(x=x_start, y=y_start).wait(200).move_to(x=x_start, y=y_end).release().perform()
            # 滑动手势密码
            # action.press(x=100, y=500).wait(200).move_to(x=200, y=500).wait(200).move_to(x=xx,y=xx).release().perform()
