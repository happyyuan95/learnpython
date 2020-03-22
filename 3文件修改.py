import sys
f = open("testfile","r",encoding="utf-8")
f_new = open("testfile2","w",encoding="utf-8")

#修改文件中的内容，需要打开一个文件再写入另一个文件
for line in f :
    if "繁华" in line :
        line = line.replace("繁华","prosperous")  #字符串的替换操作
    f_new.write(line)
f.close()
f_new.close()

#从命令行输入，传参数修改文件内容
# find_str = sys.argv[1]  #参数不存在时会报错
# replace_str = sys.argv[2]
# for line in f:
#     if find_str in line:
#         line = line.replace(find_str,replace_str)
#     f_new.write(line)
f.close()
f_new.close()

#with语句
#with open() as f:  可以自动关闭文件
# with open("testfile","r",encoding="utf-8") as f:
#     for line in f:
#         print(line)

#with open(file1) as obj1,open(file2) as obj2:  打开多个文件
with open("testfile","r",encoding="utf-8") as f1, \
    open("testfile2","r",encoding="utf-8") as f2:
    for line in f2:
        print("file2---",line)
