from selenium import webdriver
import time

driver = webdriver.Chrome()
first_url="https://www.baidu.com/"
driver.get(first_url)

second_url="http://news.baidu.com/"
driver.get(second_url)

#返回上一界面
driver.back()
time.sleep(2)
#前进到新闻界面
driver.forward()
time.sleep(2)
#刷新页面
driver.refresh()

#driver.set_window_size(800,800)
#driver.maximize_window()