#1.列表的[]改成（）组成生成器，通过next()访问
# L = [x*x for x in range(10)]
# print("L=",L)
# g = (x*x for x in range(10))
# print("g=",g) #打印的为生成器的地址
# print("next(g)=", next(g))  #要打印出所有，则要多次调用next(g)
# for n in g:
#     print(n)

def fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        #print(b)
        yield b  
        a,b = b,a+b
        # t = (b, a+b)
        # a = t[0]
        # b = t[1]
        n += 1
fib(10)