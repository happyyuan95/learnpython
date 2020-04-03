import logging

#logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别
#level设置级别，只有比debug级别高的可以打印
# logging.basicConfig(filename="log.txt",
#                     level=logging.DEBUG,
#                     format="%(asctime)s %(message)s")
# logging.debug("this is debug msg")
# logging.info("this is info msg")
# logging.warning("this is a warning msg")
# logging.critical("this is critical msg")

'''
logger提供了应用程序可以直接使用的接口 - 每个程序在输出信息之前都要获得一个Logger；
handler将(logger创建的)日志记录发送到合适的目的输出；
filter提供了细度设备来决定输出哪条日志记录；
formatter决定日志记录的最终输出格式。
'''
#获得一个logger
logger = logging.getLogger("test-log")
#设置级别
logger.setLevel(logging.DEBUG)

#StreamHandler类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
#创建一个fileHandler，将日志输出到文件，必须指定文件名
fh = logging.FileHandler("aa.log")
fh.setLevel(logging.DEBUG)
#创建一个formater用于指定格式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#给sh和fh添加formatter
sh.setFormatter(formatter)
fh.setFormatter(formatter)
#给sh和fh添加到logger -- 添加handler
logger.addHandler(sh)
logger.addHandler(fh)