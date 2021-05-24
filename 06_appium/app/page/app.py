
import yaml
from appium import webdriver
from app.page.base_page import BasePage
from app.page.main import Main
import os

class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".common.MainActivity"

    def start(self):
        if self._driver is None:

            caps = dict()
            caps["platformName"] = "android"
            # caps["udid"] = yaml.safe_load(open("../configuration.yaml"))["android2"]["udid"]
            caps["platformVersion"] = yaml.safe_load(open("../configuration.yaml"))["android2"]["platformVersion"]

            # caps["udid"] = yaml.safe_load(open("../configuration.yaml"))["android1"]["udid"]
            # caps["platformVersion"] = yaml.safe_load(open("../configuration.yaml"))["android1"]["platformVersion"]

            caps["udid"] = os.getenv("udid")

            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            caps["skipDeviceInitialization"] = True
            caps["skipServerInstallation"] = True
            # caps["newCommandTimeout"]= "100"


            """
                最好每个测试用例运行都重启，这样测试用例之间互相独立，不影响，也不会受到back操作的其他影响。
            """

            # self._driver = webdriver.Remote("http://192.168.1.6:4723/wd/hub", caps)
            self._driver = webdriver.Remote("http://192.168.1.6:4444/wd/hub", caps)
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
