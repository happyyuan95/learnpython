#
# def func1(x,y) :
#     "test function1"
#     sum = x+y
#     return sum
#
# value=func1(3,7)
# print(value)

#参数组
#参数不固定时形参加一个*，将参数存在一个元组中
# def test(*args):
#     print(args)
#
# test(1,2,3,4,5)
# test(*[1,2,3,4])

#参数为字典
# def test(**args):
#      print(args)
#      print(args["name"])
# test(name = "lijian",age = 45) #会以键值对的方式处理
# test(**{"name":"huahua","age":30}) #可以直接传字典

# def test(name, **kwargs):
#     print(name)
#     print(kwargs)
#
# test("周深",lake = "贝加尔湖畔",local="俄罗斯")


#递归
#陷入死循环，会报错
# def cal(n):
#     print(n)
#     return cal(n/2)
# cal(10)

# def cal(n):
#     print(n)
#     if int(n/2)==0:
#         return
#     return cal(int(n/2))
# cal(10)

def add(a,b, f):
    return f(a)+f(b)
print(add(3,-5,abs))
