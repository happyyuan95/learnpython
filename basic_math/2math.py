num1=100
num2=7
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)  #除法运算，得实数
print(num1//num2) #向下取整，得整数
print(num1%num2)  #取余运算，得整数
print(num1**3)   # ** 表示次方

#科学计数法
num3=1.5e3 #1.5 * 10^3
print(num3)
num3=1.5e-3 #1.5 / 10^3
print(num3)

#运算顺序,与小学学得一样
a=10
a += 1
print(a) #11
a -= 2
print(a)  #9
a *= 2
print(a)  #18
a /= 3
print(a)  #6.0
a //= 4
print(a)  #有一个是实数则得实数
a %= 5
print(a)
a **= 3
print(a)
