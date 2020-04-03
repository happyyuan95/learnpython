from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from learntest.logonweb import  logon

driver = webdriver.Chrome()
url = "http://172.16.8.226/"
driver.get(url)
driver.maximize_window()

logon(driver)

#切换到默认主界面的html
driver.switch_to.default_content()

#切换到名称为title_top的frame
driver.switch_to.frame("title_top")
print("move to top")
#定位并点击configuration按钮
driver.find_element(By.XPATH,"/html/body/table[2]/tbody/tr/td[3]/a").click()
print("after click configurations")

#切换frame到main，切换之前要先切换到主文档
driver.switch_to.default_content()
driver.switch_to.frame("main")
WebDriverWait(driver,3,0.5).until(EC.presence_of_all_elements_located((By.ID,"XSTR_LBL_CFG_EXP")))
print("move to main")

driver.find_element(By.NAME,"CONFIG").send_keys(r"C:\Users\mayn\PycharmProjects\learnbybili\learntest\config.txt")

driver.find_element(By.CSS_SELECTOR,"[value='Import']").click()
