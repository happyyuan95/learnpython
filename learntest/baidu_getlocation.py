import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

#使用id定位，id应唯一
# driver.find_element_by_id("kw").send_keys("selenium")
#driver.find_element(By.ID,"kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
#driver.find_element(By.ID,"su").click()

#使用name定位，name可能没有或者不唯一
# driver.find_element_by_name("wd").send_keys("python")
# driver.find_element_by_id("su").click()
# driver.find_element(By.NAME,"wd").send_keys("python")
# driver.find_element(By.ID,"su").click()

#使用class name定位
# driver.find_element_by_class_name("s_ipt").send_keys("武汉")
# driver.find_element_by_id("su").click()
# driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("python")
# driver.find_element(By.ID,"su").click()

#通过tag名称来定位，但是太多都一样了，一般不用
# driver.find_element_by_tag_name("input").send_keys("李健")

#通过标签文本信息定位
# driver.find_element_by_link_text("新闻").click()
# driver.find_element(By.LINK_TEXT,"新闻").click()

#通过部分标签文本信息定位
# driver.find_element_by_link_text("新闻").click()
# # time.sleep(3)
# # driver.find_element_by_partial_link_text("三大焦点").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"新").click()

#通过绝对路径定位
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/div/form/span[1]/input").send_keys("fanvil")
# driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/form/span[1]/input").send_keys("fanvil")

#通过元素属性定位
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("c")

#通过层级与属性结合定位
# driver.find_element_by_xpath("//*[@id='form']/span[1]/input").send_keys("城市之光")

#通过CSS  .class选择器定位.选择class=s_ipt的所有元素
#driver.find_element_by_css_selector(".s_ipt").send_keys("hello")
#通过CSS  #id选择器定位.选择id=kw的所有元素
#driver.find_element_by_css_selector("#kw").send_keys("python")
#使用标签名定位--标签名太多重复，不好定位
# driver.find_element_by_css_selector("input").send_keys("python")
#通过父子关系定位，选择父元素为span的所有input元素
#driver.find_element_by_css_selector("span>input").send_keys("python")
#通过属性名定位，[attribute=value]
#driver.find_element_by_css_selector("[name=wd]").send_keys("fanvil")

driver.find_element(By.CSS_SELECTOR,"[name=wd]").send_keys("fanvil")
driver.quit()