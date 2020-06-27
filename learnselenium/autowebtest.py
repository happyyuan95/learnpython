from selenium import webdriver

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
#放置在默认的驱动地址，就无需指定
driver = webdriver.Chrome()

# driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("歌手李健")
# driver.find_element_by_id("su").click()

driver.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# elements = driver.find_elements_by_class_name("plantee") #返回值为一个列表
# #找不到则返回空列表，不抛出异常
# for element in elements:
#     print(element.text)  #获取文本内容
#
# element = driver.find_element_by_class_name("plant")  #一个类中有多个元素，返回第一个元素
# #找不到则抛出异常
# print(element.text)
elemet = driver.find_element_by_css_selector(".plant")


# elements = driver.find_elements_by_tag_name("span")
# for e in elements:
#     print(e.text)
#
# element = driver.find_element_by_id('container')
elemet = driver.find_element_by_css_selector("span")

# # 限制 选择元素的范围是 id 为 container 元素的内部。
# spans = element.find_elements_by_tag_name('span')
# for span in spans:
#     print(span.text)

#隐式等待，指定最大等待时间
#如果找不到元素， 每隔 半秒钟 再去界面上查看一次， 直到找到该元素， 或者 过了10秒 最大时长
# driver.implicitly_wait(10)
# element = driver.find_element_by_id("3")
# # print(element.get_attribute("outerHTML"))  #获取一个div中的全部内容
# print(element.get_attribute("innerHTML"))  #获取一个div中的内部内容
# elemet = driver.find_element_by_css_selector("#inner11")
# print(elemet.text)

#若只有一个元素有这个属性则可以不进行赋值
element = driver.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')

driver.quit()