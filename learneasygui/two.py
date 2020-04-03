import easygui as g
import sys

file = open(".\config", "r+", encoding="utf-8")
fieldValues = file.read().splitlines() #将读取的文件的每一行加入到列表中

msg = "pls input the configurations"
title = "setup"
fieldNames = ["*被测话机ip：","用户名：","密码：","*辅助话机ip","用户名：","密码：","*辅助话机号码：",
              "通话时长(s)：","通话间隔(s)："]
message = []  #存储对话框填写的信息
message = g.multenterbox(msg, title, fieldNames, fieldValues)
print(message)
if message:
    file.seek(0) #定位到文件开头
    for msg in message :
        file.write(msg)    #文件存在则将内容写入文件
        file.write("\n")
    file.close()
else:
    file.close()
    sys.exit(0)