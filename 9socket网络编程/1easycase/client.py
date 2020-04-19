import socket

#声明socket类型并生成socket对象
client = socket.socket()
#建立连接
client.connect(('127.0.0.1', 9999))
#发生数据,只能发送byte类型
client.send(b"hello server, i am client")
#接受信息
data = client.recv(1024) #收取1024字节
print("recv server:", data)

#关闭连接
client.close()