import socket
import threading
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))

'''def run(ck):
    data = input('给服务器发送的数据:')
    client.send(data.encode('utf-8'))
    info = client.recv(1024).decode('utf-8')
    print('服务器说:', info)'''


while True:
    data = input('给服务器发送的数据:')
    client.send(data.encode('utf-8'))
    info = client.recv(1024).decode('utf-8')
    print('服务器说:', info)