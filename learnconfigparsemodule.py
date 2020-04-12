import configparser

#创建对象
config = configparser.ConfigParser()
# config["Default"] = {"name":"lijian",
#                      "age":"45",
#                      "job":"singer"}
#
# config["company"] = {}
# config["company"]["number"] = "one"
#
# config["location"] = {}
# loc = config["location"]
# loc["province"] = "beijing"
# loc["distinct"] = "chaoyang"
#
# config['Default']['ForwardX11'] = 'yes'  #default下新加配置项
#
# with open("test.cfg", "w") as configfile :
#     config.write(configfile)

print(config.read("test.cfg"))
print(config.sections())