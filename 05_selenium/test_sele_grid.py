import pytest
import os


from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

def test_grid():

    hub_url ="127.0.0:4444/wd/hub"

    # cap配置了node节点的一些信息，比如脚本分发到node节点哪个浏览器上
    # DesiredCapabilities.CHROME.copy() 这里copy的浏览器要和配置文件nodeConfig里的对应起来
    cap = DesiredCapabilities.CHROME.copy()
    for i in range(1,5):
        drvier = Remote(hub_url, cap)
        drvier.get("http://www.baidu.com")