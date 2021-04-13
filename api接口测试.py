import requests
import tkinter
import threading
def starte():
    ip=eip.get()
    a = ea.get()
    b = eb.get()
    c = ec.get()
    d = ed.get()
    headers = {
        'User-Agent': a,
        'Cookie': b,
        'Host': c,
        'Referer': d,

    }
    response = requests.get(ip, headers=headers)
    # print(response.content.decode('utf-8'))
    text.insert(tkinter.INSERT,response.content.decode('utf-8'))
def startserver():
    s = threading.Thread(target=starte)
    s.start()
win=tkinter.Tk()
win.title('api接口')
win.geometry('1000x700+200+20')
labelip=tkinter.Label(win,text='url').grid(row=0,column=0)
labea=tkinter.Label(win,text='User-Agent').grid(row=5,column=0)
labeb=tkinter.Label(win,text='Cookie').grid(row=10,column=0)
labec=tkinter.Label(win,text='Host').grid(row=15,column=0)
labed=tkinter.Label(win,text='Referer').grid(row=20,column=0)
eip=tkinter.Variable()
entryip=tkinter.Entry(win , width=80,textvar=eip).grid(row=0,column=10)
ea=tkinter.Variable()
entryipa=tkinter.Entry(win , width=80,textvar=ea).grid(row=5,column=10)
eb=tkinter.Variable()
entryipb=tkinter.Entry(win , width=80,textvar=eb).grid(row=10,column=10)
ec=tkinter.Variable()
entryc=tkinter.Entry(win , width=80,textvar=ec).grid(row=15,column=10)
ed=tkinter.Variable()
entryd=tkinter.Entry(win , width=80,textvar=ed).grid(row=20,column=10)
text=tkinter.Text(win,width=120,height=100)
text.grid(row=30,column=10)

button=tkinter.Button(win,text='启动',command=startserver).grid(row=25,column=10)
win.mainloop()
# a=input('输入接口:User-Agent')
# b=input('输入接口:Cookie')
# c=input('输入接口:Host')
# d=input('输入接口:Referer')
# a=ea
# b=eb
# c=ec
# d=ed
# headers={
#     'User-Agent':a,
#     'Cookie':b,
#     'Host':c,
#     'Referer':d,
#
#     }
# response=requests.get('https://www.baidu.com/s?ie=UTF-8&wd=李白',headers=headers)
# print(response.content.decode('utf-8'))
