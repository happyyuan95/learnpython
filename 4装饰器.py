#对于已经实现功能的函数，不改变调用方式，不改变其中的代码，增加新的功能
user_status = False
def login(func):

    def inner(*args, **kwargs):  #定义内层函数，传入任意参数
        _username = "mcheng"
        _password = "123"
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("password:")
            if username==_username and password==_password:
                print("welcom login")
                user_status = True
            else:
                print("login failed,quit")
        else:
            func()
    return inner  #返回内层函数的地址

def home():
    print("home page")

@login        #迭代器
def usa():
    print("usa")

def japan():
    print("japan")

@login
def beijing():
    print("beijing")

home()
usa()
japan()
beijing()