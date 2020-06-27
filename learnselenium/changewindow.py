from selenium import webdriver


wd = webdriver.Chrome()
wd.implicitly_wait(10)

wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')

# 点击打开新窗口的链接
link = wd.find_element_by_tag_name("a")
link.click()

# wd.title属性是当前窗口的标题栏 文本
print(wd.title)
mainwindow = wd.current_window_handle

for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '微软 Bing 搜索 - 国内版' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

wd.switch_to.window(handle)
wd.find_element_by_id("sb_form_q").send_keys("python\n")

wd.switch_to.window(mainwindow)
wd.find_element_by_id("outerbutton").click()