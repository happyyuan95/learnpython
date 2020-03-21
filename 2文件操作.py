# data = open("城市之光",encoding="utf-8").read()
# print(data)

#打开文件，返回文件句柄,默认以只读形式打开
# r文件只读 w文件只写会创建新文件 a追加
#f = open("城市之光",'r',encoding="utf-8")
#读取文件内容
#print(f.readline())  #只读取一行文件
#print(f.readlines()) #读取文件内容，返回列表，每行为一个元素
#读取一个文件，不打印第十行
# i=0
# for line in f:  #每次只读取一行的内容，效率更高
#     if i==9:
#         print("----------9---------")
#         i += 1
#         continue
#     i+=1
#     print(line)

# data = f.read()  #读取后光标定位在最后面，致使第二次读取时没有内容
# print("----read----\n",data)

# f = open("testfile","w",encoding="utf-8")  #此时文件不可读
# f.write("when we are hungry,\n")
# f.close()
#
# f = open("testfile","a",encoding="utf-8") #a追加，文件不可读
# f.write("love will keep us alive\n")
# #f.read()
# f.close()
#
# f = open("testfile","a",encoding="utf-8")
# f.write("I was standing all alone against the world outside \n")
# f.close()
#创建并打开新文件，文件存在则报错
#f = open("testfile","x",encoding="utf-8")

#f = open("城市之光",encoding="utf-8")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())  #获取光标位置，以字符个数定位
# f.seek(0)  #回到指定位置
# print("seek=0",f.readline())
# f.seek(40)  #回到指定位置
# print("seek=40",f.readline())
# print("encoding:",f.encoding)

#写文件有缓存的机制，写入内容暂时放在缓存中，使用flush强制刷新
#print(f.flush())

#进度条
# import sys
# import time
# for i in range(10):
#     sys.stdout.write("#")
#     sys.stdout.flush()  #缓冲强制刷新
#     time.sleep(0.1)
#
# f = open("testfile","a",encoding="utf-8")
# f.seek(5)  #seek在这里没有作用
# f.truncate(20)  #从头开始截断文件，只保留20个字符

#读写方式打开，新写入内容在文件末尾
f = open("testfile","r+",encoding="utf-8")
print(f.readline())
print(f.tell())
f.write("i was standing\n")
f.close()

#写读方式打开文件，先创建新文件再写入 --不常用
print("---------w+---------")
f = open("testfile","w+",encoding="utf-8")
print(f.tell())
f.write("love will keep us alive\n")
f.write("wonderful night\n")
f.write("black bird\n")
print(f.tell())
#f.seek(50)   #会覆盖内容，不建议使用
f.write("one night in beijing\n")
f.close()

print("---------a+---------")
f = open("testfile","a+",encoding="utf-8")  #追加读写
print(f.tell())
f.write("you looks wonderful\n")
f.write("lost and found\n")
f.write("missing you")
f.close()

f = open("testfile","wb")  #追加读写
print(f.tell())
f.write(("you looks wonderful\n").encode()) #将字符串转为二进制

f.close()