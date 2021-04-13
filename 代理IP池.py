import requests
from lxml import etree
import time 
import json
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

g=[]
p=[]
c={}
for  page in range(1,100):
    response=requests.get('https://www.kuaidaili.com/free/inha/{}/'.format(page),headers=headers)
    time.sleep(1)
    content=response.content
    html=etree.HTML(content)
    a=html.xpath('//tbody/tr')
    
    for i in a:
        
        ip=i.xpath('./td[1]/text()')
        post=i.xpath('./td[2]/text()')
        ppt=i.xpath('./td[4]/text()')
        # print(ppt[0])
        
        c['http']= 'http://'+ip[0]+':'+post[0]
        # print(c)
        # req=requests.get('http://huayu.zongheng.com/',headers=headers,proxies=c,timeout=1)
        # print(req.status_code)
            
        
        # c[ppt[0]]=ip[0]+':'+post[0]
        
        
        p.append(c)
  
        
   
# print(type(headers))
#         # canus
# print(type(p))
  
# # print(p)
# f=open('高质量ip.txt','w',encoding='utf-8')
# canuse=[]

    # print(proxy)
#     cause='{''}'.format(p[proxy])
#     print(cause)
ll=[]
for proxy in p:
    try:
        
        req=requests.get('http://www.zongheng.com/',headers=headers,proxies=proxy,timeout=3)
        ll.append(proxy)
        print(proxy)
    except Exception as e:
        print(e)
        
    
    # print(p[])
   
#     print(dict(proxy))  
# ret=json.loads(p)
# print(type(ret))
    # print(proxy)
    # req=requests.get('https://www.baidu.com/',headers=headers,proxies=proxy,timeout=0.1)
    # print(req.status_code)
    # if req.status_code==200:
        
    #     # print(p)     
    #     print(proxy)
    
    

