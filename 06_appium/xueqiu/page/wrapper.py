import allure
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
import logging


def handle_black(func):
    # 设置为info级别以后，会打印info及info级别以上的日志
    logging.basicConfig(level=logging.INFO)

    # 维护一个弹框黑名单
    def wrapper(*args, **kwargs):

        from app2.page.base_page import BasePage

        _black_list = [

            # (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='确定']"),
            (By.XPATH, "//*[@text='下次再说']"),
        ]
        _max_num = 3
        _error_num = 0

        # 3.6以后的新特性，类型提示，只是一个注解
        instance: BasePage = args[0]

        try:
            # list 和 dic是不能直接和str拼接的, 用repr转成字符串
            # 数组切割
            logging.info("run " + func.__name__ + "\n args: \n" + repr(args[1:]), "\n kwargs: \n" + repr(args))

            element = func(*args, **kwargs)
            # error清零
            _error_num = 0
            # 隐式等待回复正常
            instance._driver.implicitly_wait(10)
            return element

        except Exception as e:

            # 发生异常时截屏
            # 结合allure,图便保存在allure中而不在本地
            instance.screenshot("temp.png")
            with open("temp.png", "rb") as f:
                image_content = f.read()
            allure.attach(image_content, attachment_type=allure.attachment_type.PNG)

            # 发生异常时打印日志
            logging.error("element not found, handle black list")


            instance._driver.implicitly_wait(1)

            if _error_num > _max_num:
                raise e
            _error_num += 1

            for black in _black_list:
                elements = instance.finds(*black)
                if len(elements) > 0:
                    elements[0]: WebElement

                    elements[0].click()
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
