import socket
import threading
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('192.168.0.100',8080))
server.listen(5)


def run(ck):
    data = clientSocket.recv(1024)
    print('收到数据' + data.decode('utf-8'))
    sendData = input('返回给客户端的:')
    clientSocket.send(sendData.encode('utf-8'))



count=0

while True:

    '''data = clientSocket.recv(1024)
    print('收到数据' + data.decode('utf-8'))
    sendData = input('返回给客户端的:')
     clientSocket.send(sendData.encode('utf-8')'''
    clientSocket, clientAddress = server.accept()
    t = threading.Thread(target=run, args=(clientSocket,))
    t.start()


