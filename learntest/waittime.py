from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions
driver = webdriver.Chrome()
first_url="https://www.baidu.com/"
# driver.get(first_url)
#
# element = WebDriverWait(driver, 3, 0.5).until(expected_conditions.presence_of_all_elements_located((By.ID,"kw")))
# #element.send_keys("hello")
# print(element)