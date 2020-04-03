import random

#浮点数
print("生成随机实数(0,1)：",random.random())
print("生成1.2~1.9之间随机浮点数", random.uniform(1.2, 1.9))

#字符
print("字符串中选取一个元素", random.choice("mcheng"))
print("生成指定数量的字符,并将字符存放在列表中", random.sample("today is a little busy", 6))

#整数
print("生成3~5的随机整数",random.randint(3,5))
print("生成1~10间隔为3的随机整数", random.randrange(1, 10, 3))

#打乱顺序
items = [1,2,3,4,5,6,7,8,9,0]
print("打乱顺序:",random.shuffle(items))