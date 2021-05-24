import yaml
from appium import webdriver
from app2.page.base_page import BasePage
from app2.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".common.MainActivity"

    def start(self):
        if self._driver is None:

            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "hh"
            caps["udid"] = yaml.safe_load(open("../configuration.yaml"))["caps"]["udid"]

            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["skipDeviceInitialization"] = True
            caps["skipServerInstallation"] = True

            """
                最好每个测试用例运行都重启，这样测试用例之间互相独立，不影响，也不会受到back操作的其他影响。
            """

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package, self._activity)

        self._driver.implicitly_wait(15)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
