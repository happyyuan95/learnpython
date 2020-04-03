from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def logon(driver):
    # driver = webdriver.Chrome()
    #
    # url = "http://172.16.8.56/"
    # driver.get(url)

    #输入用户名和密码
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("admin")

    #勾选checkbox
    # checkbox = driver.find_element_by_xpath("//*[@id='saveLanguage']")
    # checkbox.click()
    #点击登陆按钮
    driver.find_element_by_id("logonButton").click()
    #显示等待页面title为VoIP
    WebDriverWait(driver,3,0.5).until(EC.title_is("VoIP"))
    #time.sleep(0.5)
    print(driver.title)
