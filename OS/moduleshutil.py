import shutil
#############主要用于高级的文件操作#####################
#将文件内容拷贝到另一个文件中，可以部分内容
# shutil.copyfileobj(open("blackbird", "r", encoding="utf-8"),
#                    open("copyobjblackbird.txt", "w+", encoding="utf-8"),
#                    length=1024)

#复制文件，只需要写上文件名就行，文件可以不存在
# shutil.copyfile("blackbird", "copyblackbird.txt")

#拷贝文件权限，文件必须存在
# shutil.copymode("blackbird", "newbird.txt")

#拷贝文件权限和内容，文件可以不存在
# shutil.copy("blackbird", "newbird1.txt")

#拷贝文件和状态信息，文件可以不存在
# shutil.copy2("blackbird", "newbird1.txt")

#创建压缩包并返回文件路径
# dir = shutil.make_archive("newbird.txt", "zip")
# print(dir)

import zipfile
#创建zip文件
# z = zipfile.ZipFile("test.zip", "w")
# z.write("newbird.txt")
# z.close()
# print("---------creat---------")
#解压zip文件
# z = zipfile.ZipFile("test.zip", "r")
# z.extractall()
# z.close()

import  tarfile
#创建tar压缩包
# tar = tarfile.open("test.tar", "w")
# tar.add("newbird.txt")
# tar.close()
#解压ar压缩包
# tar = tarfile.open("test.tar", "r")
# tar.extractall()
# tar.close()