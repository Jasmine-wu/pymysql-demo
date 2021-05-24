from appium import webdriver

from app.WeChat.weChat.page.base_page import BasePage
from app.WeChat.weChat.page.main import Main


class App(BasePage):

    def start(self):
        if self._driver is None:
            desired_caps = {
                "platformName": "android",
                "platformVersion": "6.0",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": True,
                "dontStopAppOnReset": True,
                "skipDeviceInitialization": True,
                "skipServerInstallation": True,
                "newCommandTimeout":"120"
                # "unicodeKeyboard": "true",
                # "resetKeyboard": "true"
            }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        else:
            # 会自动找对应cap的driver
            self._driver.launch_app()
            # self.driver.start_activity()
        self._driver.implicitly_wait(40)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self) -> Main:
        return Main(self._driver)
