num = 3
print(type(num))
num = str(num)  #整型转换为字符串
print(type(num))

num=4.4
num = int(num)  #实数转换为整数
print(type(num),num)

#eval,字符串转化为数字
#num = input("pls input a num:")
#num = eval(num)
#print(type(num),num)

#round实现四舍五入
num = 10.66
num = round(num)
print(num)