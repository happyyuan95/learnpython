import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('http://cdn1.python3.vip/files/selenium/test4.html')

# ac = ActionChains(driver)
# ac.move_to_element(driver.find_element_by_css_selector('[name="tj_briicon"]')).perform()
# ac.move_to_element(driver.find_elements_by_class_name('weather-icon')).perform()

driver.find_element_by_id('b1').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

driver.find_element_by_id('b2').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
driver.find_element_by_id('b2').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

driver.find_element_by_id('b3').click()
ale = driver.switch_to.alert
ale.send_keys('happy holiday')
ale.accept()