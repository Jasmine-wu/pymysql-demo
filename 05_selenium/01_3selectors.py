from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.implicitly_wait(10)
url = 'file:///Users/neil/Downloads/课堂素材/注册A.html'
# url = 'file:///Users/neil/Downloads/课堂素材/drop.html'

# url =r'file:///Users/neil/Downloads/%E8%AF%BE%E5%A0%82%E7%B4%A0%E6%9D%90/%E6%B3%A8%E5%86%8CA.html'
driver.get(url)
# driver.find_element_by_xpath('//*[@id="passwordA"]').send_keys('123466')
# driver.find_element_by_xpath('//input[0]').send_keys('admin')
# print(driver.find_element_by_xpath('//input'))


#
# 1).使用CSS定位方式中id选择器定位用户名输入框，并输入:admin
# driver.find_element_by_css_selector('#userA').send_keys('admin')


# 2).使用CSS定位方式中属性选择器定位密码输入框，并输入:123456
# driver.find_element_by_css_selector('[type="password"]').send_keys('123')

# 3).使用CSS定位方式中class选择器定位电话号码输入框，并输入:18600000000
# driver.find_element_by_css_selector('.telA').send_keys('123245555')

# 4).使用CSS定位方式中元素选择器定位注册按钮，并点击


# driver.find_element_by_css_selector('p>input#emailA').send_keys('123.qq.com')
# print(driver.find_element_by_css_selector('span').text)

# driver.find_element_by_partial_link_text('访问 新浪').click()

# inputs = driver.find_elements_by_tag_name('input')
# print('%d is total count of input '%len(inputs))
# print('the type of inputs is ',type(inputs))
#
# for input in inputs:
#     input.send_keys('admin')


# driver.find_element()
# userA = driver.find_element(By.ID, 'userA')
# print(userA)

# 1).通过脚本执行输入用户名:admin;密码:123456;电话号码:18611111111;电子邮件:123@qq.com
# 2).间隔3秒，修改电话号码为:18600000000
# 3).间隔3秒，点击‘注册’按钮
# 4).间隔3秒，关闭浏览器
# 5).元素定位方法不限

# driver.find_element_by_css_selector('#userA').send_keys('admin')
# driver.find_element_by_css_selector('#passwordA').send_keys('123456')
# driver.find_element_by_css_selector('#telA').send_keys('18611111111')
# driver.find_element_by_css_selector('#emailA').send_keys('123@qq.com ')
# sleep(3)
# driver.find_element_by_css_selector('#telA').clear()
# driver.find_element_by_css_selector('#telA').send_keys('18600000000')
# sleep(3)
# driver.find_element_by_css_selector('[type="submitA"]').click()

# driver.find_element_by_css_selector('#telA')
# 需求:使用‘注册A.html’页面，完成以下操作:
# 1).获取用户名输入框的大小
# print("size of username input is:",driver.find_element_by_css_selector('#userA').size)

# # 2).获取页面上第一个超链接的文本内容
# elements= driver.find_elements(By.CSS_SELECTOR, 'p>a')
# print('获取页面上第一个超链接的文本内容:', elements[0].text)
#
# # 3).获取页面上第一个超链接的地址
# print('获取页面上第一个超链接的地址:', elements[0].get_attribute('href'))
#
#
# # 4).判断页面中的span标签是否可见
#
# print('判断页面中的span标签是否可见:',driver.find_element_by_css_selector('span').is_displayed())
# # 5).判断页面中取消按钮是否可用
# print('判断页面中取消按钮是否可用:',driver.find_element_by_css_selector('#cancelA').is_enabled())
#
# # 6).判断页面中'旅游'对应的复选框是否为选中的状态
# print('判断页面中"旅游"对应的复选框是否为选中的状态:',driver.find_element_by_css_selector('#lyA').is_selected())


# 需求: 打开注册页面A，在用户名文本框上点击鼠标右键


# driver.find_element_by_css_selector('#passwordA').send_keys('123456')
# driver.find_element_by_css_selector('#telA').send_keys('18611111111')
# driver.find_element_by_css_selector('#emailA').send_keys('123@qq.com ')

#


# driver.find_element_by_css_selector('button').click()
# action = ActionChains(driver)
# # action.context_click(driver.find_element_by_css_selector('#userA')).perform()
# driver.find_element_by_css_selector('#userA').send_keys('admin')
# sleep(3)
# action.double_click(driver.find_element_by_css_selector('#userA')).perform()


# action.context_click(driver.find_element_by_css_selector('#userA')).perform()
# driver.find_element_by_css_selector('#userA')
# actions.
# 需求:打开‘drag.html’页面，把红色方框拖拽到蓝色方框上
# source = driver.find_element_by_css_selector('#div1')
# target = driver.find_element_by_css_selector('#div2')
# action.drag_and_drop(source,target).perform()

# 需求: 打开注册页面A，模拟鼠标悬停在‘注册’按钮上





# username = driver.find_element_by_id("userA").send_keys("admin")

# password = driver.find_element_by_id("passwordA")

# driver.find_element_by_class_name('emailA').send_keys('123@qq.com')

# password.send_keys("123")
# tel = driver.find_element_by_id("tel")
# tel.send_keys('12345777')
# email = driver.find_element_by_id("emailA")

# email.send_keys('232qq.com')


# 需求:打开注册A页面，完成以下操作
# 1). 输入用户名:admin1，暂停2秒，删除1
# 2). 全选用户名:admin，暂停2秒
# 3). 复制用户名:admin，暂停2秒
# 4). 粘贴到密码框

driver.find_element_by_id('userA').send_keys('admin11')
driver.implicitly_wait(10)


# # sleep(2)
# driver.find_element_by_id('userA').send_keys(Keys.BACK_SPACE)
# driver.find_element_by_id('userA').send_keys(Keys.CONTROL,'a')
# # sleep(2)
# driver.find_element_by_id('userA').send_keys(Keys.CONTROL,'x')
# # sleep(2)
# driver.find_element_by_id('passwordA').send_keys(Keys.CONTROL,'v')
# # print('%s'% driver.find_element_by_id('passwordA').text)


# # 定位用户名
# element = driver.find_element_by_id("userA")
# # 输入用户名
# element.send_keys("admin1")
# # 删除1
# element.send_keys(Keys.BACK_SPACE)
# # 全选
# element.send_keys(Keys.CONTROL, 'a')
# # 复制
# element.send_keys(Keys.CONTROL, 'c')
# #粘贴
# driver.find_element_by_id('passwordA').send_keys(Keys.CONTROL, 'v')
# sleep(5)


driver.quit()

# selenum共八种定位方式
