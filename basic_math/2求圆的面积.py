import math
r=input("请输入半径：")  #input的数据为字符串str类型
print(r,type(r))
r=eval(r)  #字符串转换为数值
print(r,type(r)) #类型转换为int
s = r * r * math.pi
print("圆的面积：",s)
