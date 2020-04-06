import os
import sys

# print("当前目录",os.getcwd())
# print("当前目录",os.path.abspath("./"))
#删除文件
#os.remove("testfile2")
#更改文件名
#os.rename("城市之光", "light of city")

print("最大的int值", sys.maxsize)
print("系统平台", sys.platform, os.name)

#sys.stdout.write("input :") #输出到stdout

val = sys.stdin.readline()
print(val)