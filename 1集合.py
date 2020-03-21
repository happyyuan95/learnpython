list_1=[1,4,5,7,3,6,7,9]
#集合是无序的，可以排除重复
list_1 = set(list_1)
print(list_1,type(list_1))

list_2=set([2,6,0,66,22,8,4])
print(list_1,list_2)

print("----------关系运算---------")
#求两个集合的交集
print("交集：",list_1.intersection(list_2))
print(list_1 & list_2)
#判断是否有交集，没有交集则true
print(list_1.isdisjoint(list_2))
#求两个集合的并集
print("并集：",list_1.union(list_2))
print(list_1 | list_2)
#求两个集合的差集
print("差集：",list_1.difference(list_2)) #取出list1里有的list2中没有的
print(list_1 - list_2)
#判断list1是否是list2的子集
print(list_1.issubset(list_2))
#判断list1是否是list2的父集
print(list_1.issuperset(list_2))
#对称差集
print("对称差集：",list_1.symmetric_difference(list_2)) #取出两个集合中都没有的
print(list_1 ^ list_2)

print("-----增-----")
list_1.add(99)
print(list_1)
list_1.update([33,44,55,66])
print(list_1)
print("-----删-----")
print("随机删除pop",list_1.pop()) #随机删除元素返回删除的数据
print("删除指定元素remove：")
list_1.remove(33)  #删除不存在的元素会报错，没有返回值
print(list_1)
list_1.discard(444) #删除不存在的元素不会报错，没有返回值
print("删除指定元素remove:",list_1)