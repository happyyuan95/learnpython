class Dog:

    def __init__(self,name,age):
        #初始化name和age,name和age可以供类中所有的函数使用
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+ " is sitting here and his is "+self.age+" years old")

    def rollover(self):
        print(self.name.title() + " can roll over")

mydog = Dog("lulu","8")
mydog.sit()
mydog.rollover()