from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://cdn1.python3.vip/files/selenium/test2.html")
#radio button
element = driver.find_element_by_css_selector('#s_radio input[checked=checked]')
print("当前选中的是：" + element.get_attribute('value'))

driver.find_element_by_css_selector('[value="小江老师"]').click()

#checkbox
elements = driver.find_elements_by_css_selector('#s_checkbox input[checked=checked]')
for e in elements:
    e.click()

element = driver.find_element_by_css_selector('#s_checkbox input[value="小雷老师"]').click()

#单选下拉框
select = Select(driver.find_element_by_id("ss_single"))  #创建select对象
select.select_by_visible_text('小江老师') #通过select对象选中

#多选下拉框
select = Select(driver.find_element_by_id('ss_multi'))
#取消勾选之前已经选中的
select.deselect_all()
#选中你用勾选的
select.select_by_visible_text('小雷老师')
select.select_by_visible_text('小凯老师')

driver.quit()