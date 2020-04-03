from selenium import webdriver
import  time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)  #隐式等待3s
driver.get("https://www.baidu.com")

search_windows = driver.current_window_handle  #获得当前窗口的句柄

driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()

all_handles = driver.window_handles  #获得所有窗口的句柄

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print("you are in register window")
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("12345")
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("123456")
        driver.find_element_by_id("TANGRAM__PSP_4__password").clear()
        driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("123456")
        time.sleep(3)


for handle in all_handles:
    if handle == search_windows:
        driver.switch_to.window(handle)
        print("return to search window")
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_link_text("新闻").click()
        WebDriverWait(driver,3,0.5).until(EC.title_contains("百度新闻"))