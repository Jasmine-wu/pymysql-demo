import inspect
import json

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver

from app2.page.wrapper import handle_black


class BasePage:
    _driver: WebDriver = None
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value: str = None):

        element: WebElement

        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)

        return element

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text

    def steps(self, path):

        func_name = inspect.stack()[1].function
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)[func_name]
        content = json.dumps(steps)

        for key, value in self._params.items():
            content = content.replace("${" + key + "}", value)
        steps = json.loads(content)

        for step in steps:

            if "action" not in step.keys():
                self.find(step["by"], step["locator"])

            else:

                action = step["action"]
                if action == "len>0":
                    elements = self.finds(step["by"], step["locator"])
                    return len(elements) > 0

                elif action == "click":
                    self.find(step["by"], step["locator"]).click()

                elif action == "send":
                    self.find(step["by"], step["locator"]).send_keys(step["value"])

    def screenshot(self, filename):
        self._driver.save_screenshot(filename)
