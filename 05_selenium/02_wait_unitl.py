from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
url = 'file:///Users/neil/Downloads/课堂素材/注册A.html'
# url = 'file:///Users/neil/Downloads/课堂素材/drop.html'
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# driver = webdriver.firefox()

driver.get(url)

# driver.find_element_by_id('userAq').send_keys('admin1')
element = WebDriverWait(driver,10,1).until(lambda x: x.find_element_by_id("user888"))
element.send_keys("134")
# sleep(2)
# driver.find_element_by_id('userA').send_keys(Keys.BACK_SPACE)
# sleep(2)
#
# driver.find_element_by_id('userA').send_keys(Keys.CONTROL,'a')
# sleep(2)
# driver.find_element_by_id('userA').send_keys(Keys.CONTROL,'c')
# sleep(2)
# driver.find_element_by_id('passwordA').send_keys(Keys.CONTROL,'v')
#
# sleep(5)
driver.quit()
