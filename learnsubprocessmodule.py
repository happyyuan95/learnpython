import subprocess
import configparser
import  shelve
import time

#执行shell命令并返回状态
#ret = subprocess.call(["ls", "-la"], shell=True)
# ret = subprocess.call(["ls", "-l"], shell=True)
# print(ret)

#文件需要不存在，执行代码会自动生成该文件
d = shelve.open("testfile.txt")

# name = ["lijian", 'mcheng', "huahua"]
# d["d1"] = name
#
# info = {"name":"lijian", "age":45}
# d["d2"] = info
#
# d["date"] = time.time()
#
# d.close()

print(d.get("d1"))
print(d.get("d2"))
print(d.get("date"))

d.close()