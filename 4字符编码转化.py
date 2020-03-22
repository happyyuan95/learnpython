#首先decode转化为Unicode
#再使用encode转化为gbk
#python3中encode转换编码同时还转变为bytes

import sys
print(sys.getdefaultencoding())

s="李健何时营业"
# s_go_gbk = s.encode("gbk")
# print(s_go_gbk,type(s_go_gbk))
#
# s_unicode = s_go_gbk.decode()
# print(s_unicode,type(s_unicode))

print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))