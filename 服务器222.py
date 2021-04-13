import tkinter
import socket
import threading
win=tkinter.Tk()
win.title('客户端')
win.geometry('400x400+200+20')
ck=None
def getinfo():
    while True:
        data = ck.recv(1024)

        text.insert(tkinter.INSERT, data.decode('utf-8'))
def connectserver():
    global  ck
    ipstr = eip.get()
    poststr = eport.get()
    userstr=euser.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipstr, int(poststr)))
    client.send(userstr.encode('utf-8'))
    ck=client
    t=threading.Thread(target=getinfo)
    t.start()
def sendmail():
    friend=efriend.get()
    sendstr1=esend.get()
    sendstr=friend+":"+sendstr1
    ck.send(sendstr.encode('utf-8'))
    text.insert(tkinter.INSERT, '我说:'+sendstr1+'\n')



labelusere=tkinter.Label(win,text='username').grid(row=0,column=0)
labelip=tkinter.Label(win,text='ip').grid(row=1,column=0)
labeport=tkinter.Label(win,text='port').grid(row=2,column=0)
euser=tkinter.Variable()
eip=tkinter.Variable()
eport=tkinter.Variable()
entryuser=tkinter.Entry(win,textvar=euser).grid(row=0,column=1)
entryip=tkinter.Entry(win,textvar=eip).grid(row=1,column=1)
entrypory=tkinter.Entry(win,textvar=eport).grid(row=2,column=1)
button=tkinter.Button(win,text='连接',command=connectserver).grid(row=3,column=0)
text=tkinter.Text(win,width=30,height=10)
text.grid(row=4,column=0)
esend=tkinter.Variable()
entrysend=tkinter.Entry(win,textvariable=esend).grid(row=5,column=0)
efriend=tkinter.Variable()
entryfriend=tkinter.Entry(win,textvariable=efriend).grid(row=6,column=0)
button2=tkinter.Button(win,text='发送',command=sendmail).grid(row=6,column=1)


win.mainloop()
#ip=server.natappfree.cc
#port=36165