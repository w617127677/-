name=input('输入:')
from urllib import parse
from urllib import request
import re
import json

headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
url='https://fanyi.baidu.com/sug'
date={
      'kw':name
      }
date_str=parse.urlencode(date)
r=request.Request(url=url,headers=headers,data=bytes(date_str,encoding='utf-8'))
content=request.urlopen(r).read().decode('utf-8')
print(type(content),content)
obj=json.loads(content)#将str字符串转换为字典
print(type(obj),obj)

s=json.dumps(obj)
print(type(s),s)#将字典转换为字符串

f=open('file.txt',"w")
for i in range(len(obj)):
    f.write(content)    
f.close()

