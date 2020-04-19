class Dog(object):

    '''狗 dog puppy'''

    name = "dd"
    def __init__(self, name):
        self.name = name
        self.__hour = None

    @staticmethod  # 把eat方法变为静态方法,无法访问类/实例的任何属性
    def eat(self):
        print("%s is eating" % self.name)

    @classmethod  #把talk变为类方法，只能访问类变量，不能访问实例变量
    def talk(self):
        print("%s is talking" % self.name)

    @property   #把一个方法变成一个静态属性
    def sleep(self):
        print("%s is sleeping -- %s hours" % (self.name, self.__hour))
    @sleep.setter  #对属性进行赋值
    def sleep(self, hour):
        print("%s is sleeping for %s hours" % (self.name, hour))
        self.__hour = hour
    @sleep.deleter
    def sleep(self):  #删除属性
        print("delete sleep")
        del self.__hour

    def __call__(self, *args, **kwargs):
        print("in the __call__")

d = Dog("money")
#d.eat()  #当eat变成静态方法后，再通过实例调用时就不会自动把实例本身当作一个参数传给self了

# 1. 调用时主动传递实例本身给eat方法，即d.eat(d)
# 2. 在eat方法中去掉self参数，但这也意味着，在eat中不能通过self.调用实例中的其它变量了
d.eat(d)

d.talk()
#调用属性
d.sleep
#修改属性值
d.sleep = 8
d.sleep
#删除属性
del d.sleep

#打印类的描述信息
print(d.__doc__)

d() #直接调用__call__
