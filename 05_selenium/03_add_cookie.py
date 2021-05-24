from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select



# url = 'file:///Users/neil/Downloads/课堂素材/注册A.html'
# url = 'file:///Users/neil/Downloads/课堂素材/drop.html'

url = 'https://www.baidu.com'

# 需求:使用‘注册A.html’页面，完成对城市的下拉框的操作 1).选择‘广州’
# 2).暂停2秒，选择‘上海’
# 3).暂停2秒，选择‘北京’
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
# driver.implicitly_wait(10)

driver.get(url)

driver.add_cookie({'name':'BDUSS','value':'ZmZEp1bDhxS3cybi1wSlNldzRQOXJ-LW1hQ2Zab2JaRDM3aGxJZkF0cTJoV0ZnRVFBQUFBJCQAAAAAAAAAAAEAAABnbtWGtcO9sbDtvcXKrwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALb4OWC2-DlgaD'})

sleep(2)
driver.refresh()

print(driver.get_cookies())
sleep(5)


# select = Select(driver.find_element_by_tag_name('select'))
# select.select_by_index(2)
# sleep(2)
# select.select_by_index(1)
# sleep(2)
# select.select_by_index(0)
#
# driver.find_element_by_css_selector('#alerta').click()
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()


# driver.quit()