import time
#print(time.clock())  #返回处理器时间，被废弃
print("与utc时间差（h）：",time.altzone/3600)
print("返回时间格式 星期 月 日 时:分:秒 年：",time.asctime())
print("以struct_time形式返回时间信息：",time.localtime())
#日期字符串转换为时间戳
string_struct = time.strptime("2020/3/31", "%Y/%m/%d")
print("将日期时间字符串转化为struct",string_struct)
string_struct2 = time.mktime(string_struct)
print("将struct时间转化为时间戳",string_struct2)
#时间戳转换为字符串
print("字符串时间：",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

import datetime
print("打印当前时间：", datetime.datetime.now())
print("时间戳转化为日期", datetime.datetime.fromtimestamp(time.time()))
#时间加减
print("当前时间+3天", datetime.datetime.now() + datetime.timedelta(3))
print("当前时间-3天", datetime.datetime.now() + datetime.timedelta(-3))
print("当前时间+2 hours", datetime.datetime.now() + datetime.timedelta(hours = 2))
print("当前时间+40 minutes", datetime.datetime.now() + datetime.timedelta(minutes = 40))
now = datetime.datetime.now()
print(now.replace("替换当前时间为指定值",minute=9, hour=8, second=55))