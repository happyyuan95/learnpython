from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.implicitly_wait(3)  #隐式等待3s
driver.get("https://www.baidu.com")
driver.maximize_window()

link = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(link).perform()  #悬停操作

driver.find_element_by_link_text("搜索设置").click()

#要确保该元素可见，否则会报错
driver.find_element_by_class_name("prefpanelgo").click()
driver.implicitly_wait(3)

# alert = driver.switch_to.alert
# alert.accept()

alert = Alert(driver)
print(alert.text)