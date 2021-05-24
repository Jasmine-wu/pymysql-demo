"""
    封装page的公共方法

"""
from appium.webdriver.webdriver import WebDriver

"""
    注意：是from appium.webdriver.webdriver import WebDriver
    WebDriver
    不是：from appium import webdriver
    webdriver

"""
class BasePage:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver
