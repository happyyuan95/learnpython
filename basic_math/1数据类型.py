#变量：在程序中可以通过赋值更改的数，地址赋值可以改变数据类型
#常量：不能进行赋值的数据
#标识符：只能由数字、字母、下划线组成，数字不能开头，严格区分大小写
#关键字：编译器自带，不能设置为变量的名字
a=10  #a是一个变量，a是一个标识符，用于区别其他变量
print(a)
a=12
A=140
print(A)
print(a)
print(type(a))  #type()可以读取数据类型
print(id(a))   #id()查看内存地址
a = "type"  #"" 字符串类型
print(a)
#打印所有的关键字
import keyword
print(keyword.kwlist)  #输入字符串

#import os
#mystr = input("pls input your command:")  #输入字符串
#os.system(mystr)

#相同数值是同一个地址
num1 = 3
num2 = 3
print(id(num1), id(num2))  #print打印多个数据可以用逗号分隔
num1 = 8  #改变了赋值的地址
print(id(num1), id(num2))


#整数int:可以自适应数据长度，实数float，布尔bool，字符串str，复数complex
date=1+2j
print(type(date))

#del 删除变量，删除后不能引用
del date
#print(date)

#连续赋值
num1=num2=10
print(num1,num2)
#交互对称赋值，必须左右对称赋值
num1,num2=1,2
print(num1,num2)

num=10
print(num)
num = None  #区分num是否被人使用
print(num,type(num)) #NoneType
