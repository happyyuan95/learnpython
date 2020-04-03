import easygui as g

#消息弹窗
#g.msgbox("learn python everyday")
#双向选择，choices只能有两个选项，返回True/False
#g.ccbox(msg = "learn easygui", title = "learn py",choices=("i'm happy","i'm angry"))
#多项选择，choices可以有多个选项，返回选择文本字符串
#ret = g.buttonbox(msg="learn easygui",title="py",choices=("happy","unhappy","upset","angry"))
#可选下拉框-单选,choices可以是列表、元组等内容，选择确认后返回文本内容，否则为none
#ret = g.choicebox(msg="do you like it?",title="study",choices=("yes","no","i don't know"))
#可选下拉框-多选
#ret = g.multchoicebox(msg="what is the weather today?",title="weather",choices=("sunny","rainy","cloudy","froggy"))
#文本输入框,strip=True默认去掉字符串后的空格。default默认文本，返回值为输入字符串内容
#ret = g.enterbox(msg="what is the weather today?",title="weather",strip=True,default="sunny")
#文本框只能输入范围内的整数，lowerbound最小值，upperbound最大值，返回输入数字，没输入返回none
#ret = g.integerbox(msg="how much is it?",title="price",lowerbound=1,upperbound=100)
#多个输入框，fields和values都用列表形式，ret为输入内容的列表
# fileds = ["test phone ip","test phone num","interval"]
# ret = g.multenterbox(msg="test options",title="test",fields=fileds,values=[])
#输入密码框，将密码加密显示，返回输入的字符串
# ret = g.passwordbox(msg="password",title="logon",default="aaa")
#将最后一个输入框显示为密码形式，将输入的内容作为列表返回
# ret = g.multpasswordbox(msg="input msg",title="logon",fields=("username","password"))
# print(ret)
#选择打开文件夹，返回文件夹路径
#ret = g.diropenbox(msg="choose to open",title="choose file")
#选择打开文件
ret = g.fileopenbox(msg="open file",title="choose file",filetypes=["*.txt"])
print(ret)