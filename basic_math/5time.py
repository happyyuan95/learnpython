import time

t1 = time.time()  #计算当前时间距离1970年得ms数
print(t1)
t1 = int(t1)
#t1 /= 1000  #得秒
#print(t1)
t1 /= 3600  #得小时
print(t1)
t1 /= 24  #小时
print(t1)
t1 /= 365 #年
print(t1)
