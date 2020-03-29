# from selenium import webdriver
#
# #driver = webdriver.Chrome(r"D:\drivers\chromedriver.exe")
# driver = webdriver.Remote()

from selenium.webdriver import Remote,DesiredCapabilities
driver = Remote(desired_capabilities = DesiredCapabilities.CHROME.copy())
driver.get("https://www.baidu.com")

driver.quit()