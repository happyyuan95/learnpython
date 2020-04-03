#导入一个类或者多个类
# from module.classrestrount import Restrount,Icecream
#
# myrestrount = Restrount("yuan","chineses")
# myrestrount.decribe_restrount()
#
# myice = Icecream("sweet")
# myice.showicecream()

#导入整个模块，模块钟有多个类
import module.classrestrount
myrestrount = module.classrestrount.Restrount("yuan","chineses")
myrestrount.decribe_restrount()
myice = module.classrestrount.Icecream("sweet")
myice.showicecream()