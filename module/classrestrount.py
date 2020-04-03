class Restrount:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.num = 0    #设置属性的默认值

    def decribe_restrount(self):
        print("the restrount is "+self.name.title())
        print("the type is "+self.type)

    def open_restrount(self):
        print("the restrount is open as usual")

    def set_num(self,num):
        self.num = num
        print("the restrount has %d people" %self.num )

    def increment_num(self,num):
        self.num += num
        print("the restrount had served %d people" %self.num)

# rest = Restrount("bigking","quickly food")
# rest.decribe_restrount()
# rest.open_restrount()
# rest.set_num(10)
# rest.increment_num(20)

class Icecream(Restrount):
    def __init__(self,flavors):
        self.flavors = flavors
    def showicecream(self):
        print("the icecream is "+self.flavors)

# icecreamstand = Icecream("sweet")
# icecreamstand.showicecream()