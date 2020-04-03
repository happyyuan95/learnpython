import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from learntest.logonweb import  logon

driver = webdriver.Chrome()
url = "http://172.16.8.226/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

logon(driver)

#切换到默认主界面的html
driver.switch_to.default_content()

#切换到名称为title_top的frame
driver.switch_to.frame("title_top")
print("move to top,to click reboot button")
element = driver.find_element(By.XPATH,'/html/body/table[2]/tbody/tr/td[7]/a')
print(element.text)
element.click()
driver.implicitly_wait(5)

#切换到main frame
driver.switch_to.default_content()
driver.switch_to.frame("main")
WebDriverWait(driver,3,0.5).until(EC.presence_of_all_elements_located((By.ID,"XSTR_LBL_REBOOT_PHONE")))
print("move to main")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/table/tbody/tr[2]/td/input").click()
WebDriverWait(driver,3,0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"box_btn")))
print("move to reboot page")

driver.find_element_by_xpath('//*[@id="dFrame"]/div/div[2]/div/input[1]').click()
print("rebooting...")

time.sleep(60)

driver.quit()