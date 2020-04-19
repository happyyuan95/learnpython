import socket

server = socket.socket()

#绑定要监听的ip和端口
server.bind(('127.0.0.1', 9999))
#监听
server.listen()

print("wait accept...........")
#等待连接
#返回conn连接的标记，addr对方地址
conn, addr = server.accept()
print(conn, addr)


print("wait recv-----------")
#接受客户端数据
recv = conn.recv(1024)
print("recv client:", recv)

#发送数据给客户端
conn.send(b"hello client, welcom!")

server.close()