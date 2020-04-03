from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "http://172.16.8.56/"
driver.get(url)

driver.find_element_by_id("username").clear()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("admin")
driver.find_element_by_id("logonButton").click()

time.sleep(0.5)
print(driver.title)
#切换到默认主界面的html
driver.switch_to.default_content()
#切换到名称为title_top的frame
driver.switch_to.frame("title_top")
#定位到title_top中的logout button
driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[1]/td[4]/form/input").click()
# topname = "title_top"
# driver.switch_to.frame(driver.find_element(By.NAME,topname))