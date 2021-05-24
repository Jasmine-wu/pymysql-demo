from appium import webdriver
"""
    打印 page_source ,可以看到toast在里面
        # toast必须使用xpath来找
        # 只有一个toast的时候可以用class来找
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # 通过toast文本来找
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'toast文本部分内容')]").text
"""


