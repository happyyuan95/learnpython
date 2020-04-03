'''
用于序列化的两个模块

json，用于字符串 和 python数据类型间进行转换 https://www.runoob.com/python3/python3-json.html
pickle，用于python特有的类型 和 python的数据类型间进行转换
Json模块提供了四个功能：dumps、dump、loads、load  https://www.cnblogs.com/machangwei-8/p/10724781.html
pickle模块提供了四个功能：dumps、dump、loads、load

序列化：将python的值转换为json格式的字符串。
反序列化：将json格式的字符串转换成python的数据类型
'''

import json

#dumps可以序列化大部分数据类型：整型、浮点型、bool、字符串、字典、元组、列表等
# data = {"name":"mcheng", "from":"henna"}
# #将数据转化为json格式的str字符串
# json_str = json.dumps(data)
# print(json_str, type(json_str))
#
# str2 = '["abc", 123]'  #（）或者其他特殊符号，导致json无法识别
# print(type(str2))
# jsontopy_str = json.loads(str2)
# print(jsontopy_str, type(jsontopy_str))

# data = {"name":"程梦园", "from":"河南"}
# print(data, type(data))
# json_str = json.dumps(data)
# print(json_str, type(json_str))
# json_str = json.dumps(data, ensure_ascii=False)  #显示中文需要将ensure_ascii=False
# print(json_str, type(json_str))

# data = {"name":"mcheng", "from":"henna"}
# file = open("jsontest.txt", "w", encoding="utf-8")
# #将内容序列化并写入文件
# # json.dump(data, file)
# # file.close()
# #将文件中的内容反序列化
# file = open("jsontest.txt", "r", encoding="utf-8")
# data = json.load(file)
# file.close()
# print(data, type(data))

import pickle
# data = {"name":"mcheng", "from":"henna"}
# #返回字节bytes形式的数据
# p_str = pickle.dumps(data)
# print(p_str, type(p_str))
# #bytes形式为python可读
# p_bak = pickle.loads(p_str)
# print(p_bak, type(p_bak))

#序列化的数据都是二进制形式的，则读写文件需要加上b
# file = open("pickletest.txt", "wb")
# pickle.dump(data,file)
# file.close()
#
# file = open("pickletest.txt", "rb")
# data = pickle.load(file)
# print(data, type(data))

#Shelve是对象持久化保存方法，将对象保存到文件里面，缺省（即默认）的数据存储文件是二进制的
#https://www.cnblogs.com/sui776265233/p/9225164.html
import shelve
s = shelve.open("shelvetest.db")
s["abc"] = {"int":10, "float":2.3, "string":"hello"}
s["k"] = {1,2,3}
s.close()