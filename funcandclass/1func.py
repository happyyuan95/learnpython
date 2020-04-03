# def city_country(city_name, city_local) :
#     ret = city_name + "," + city_local
#     return ret
# print(city_country("beijing","china"))

# magic_name_list = ["li","jian","hua","mao"]
# def show_magic(namelist) :
#     for name in namelist:
#         print("his name is:",name)
# show_magic(magic_name_list)
#
# def make_great(namelist):
#     great_name_list=[]
#     while namelist:
#         i=0
#         great_name = "the great "+namelist.pop()
#         great_name_list.append(great_name)
#     return great_name_list
# name_great = make_great(magic_name_list)
# print(name_great)

# def favorite_pets(*pets) :
#     for pet in pets:
#         print("your favorite pet is ",pet)
# favorite_pets("puppy","kitten","parrot")

def make_food(type,where,**foods):
    food_info={}
    food_info["type"]=type
    food_info["where"]=where
    for key,value in foods.items():
        food_info[key]=value
    return food_info
foods=make_food("fruit","china",color="red",name="apple")
print(foods)