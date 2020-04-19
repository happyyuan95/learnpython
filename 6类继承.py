'''
1.python2 的经典类是按照深度优先继承，新式类是广度优先继承的
2.Python3经典类和新式类都是统一按照广度优先继承
广度优先：先查找相同层级的类来继承，再查找上一级
深度优先：按照继承顺序来
'''
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating" % self.name)

    def talk(self):
        print("%s is talking" % self.name)

    def sleep(self):
        print("%s is talking" % self.name)

    def introduce(self):
        print("My name is %s and age is %s" % (self.name, str(self.age)))

class Relation(object):
    def makeFriends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))

class Men(People, Relation):
    def __init__(self, name, age, money):  #增加新的参数
        #People.__init__(self, name, age)  #先继承父类的参数
        super(Men, self).__init__(name, age)  #使用super可以避免类名变更, 按照继承顺序执行第一个init
        self.money = money

    def sleep(self):
        #重写父类方法
        People.sleep(self)
        print("man is sleep")

    def MakeMoney(self):
        print("he is making moey %s" % str(self.money))

class Women(People):
    def eat(self):
        #重写父类方法
        People.eat(self)
        print("woman like eating sweet foods")

m = Men("lijian", 45, 100)
# m.introduce()
# m.sleep()
# m.MakeMoney()
w = Women("beibei", 40)
m.makeFriends(w)