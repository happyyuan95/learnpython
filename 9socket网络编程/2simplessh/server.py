import socket
import os

server = socket.socket()
server.bind(('localhost', 8888))

server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:", addr)

    while True:
        print("waitting for conn....")
        data = conn.recv(1024)
        if not data:
            print("客户端断开")
            break
        print("执行指令：", data)
        cmd_res = os.popen(data.decode()).read()  #接收的为字符串返回值也是
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no output'
        #受到中文字符影响，一个中文字符为3字节，所以需要encode下
        conn.send( str(len(cmd_res.encode("utf-8"))).encode("utf-8") )  #先发大小给客户端
        conn.send(cmd_res.encode("utf-8"))
        print("--send done--")

server.close()