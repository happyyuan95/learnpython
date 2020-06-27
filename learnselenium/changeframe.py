import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://cdn1.python3.vip/files/selenium/sample2.html")

driver.switch_to.frame("frame1")

elements = driver.find_elements_by_class_name("animal")
for e in elements:
    print(e.text)

driver.switch_to.default_content()
driver.find_element_by_id("outerbutton").click()

time.sleep(5)
driver.quit()