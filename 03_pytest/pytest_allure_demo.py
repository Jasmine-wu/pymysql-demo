import pytest
import allure
from selenium import webdriver
import time
from time import sleep


@allure.feature("百度搜索")
class TestSearch():
    @allure.story("百度搜索")
    @pytest.mark.parametrize("test_data", ["unittest", "pytest", "allure"])
    def test_baidu_search(self, test_data):
        with allure.step("打开网页"):
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("http://www.baidu.com")
            sleep(2)

        with allure.step("输入搜索框，百度一下", ):
            driver.find_element_by_id("kw").send_keys(test_data)
            sleep(2)
            driver.find_element_by_id("su").click()
            sleep(3)

        with allure.step("截屏"):
            file_name = "./Source/{}.png".format(time.strftime("%Y%m%d%H%M%S", time.localtime()))
            # print(file_name)
            driver.save_screenshot(file_name)
            allure.attach.file(file_name, "百度搜索{}截屏图片".format(test_data), attachment_type=allure.attachment_type.PNG)

        with allure.step('关闭游览器'):
            # driver.close()
            driver.quit()


"""
 pytest pytest_allure_demo.py --alluredir ./report/3
 allure serve ./report/3
"""
