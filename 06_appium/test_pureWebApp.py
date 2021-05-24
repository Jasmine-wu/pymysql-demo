from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebApp():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "browserName": "Browser",
            "noReset": "true"

            # 不指定路径，就会去appium自带的默认的路径下找存在的
            # "chromedriverExecutable": "./driver/测试/"
            # "dontStopAppOnReset": "true",
            # "skipDeviceInitialization": "true"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_web(self):
        # 点击输入
        # 输入"appium"
        # 点击搜索
        self.driver.get("https://www.baidu.com")

        # 注意，这里不要mobileid了
        search_locator = (By.ID, "kw")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).send_keys("appium")

        locator = (By.ID, "su")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

        self.driver.find_element(*locator).click()



