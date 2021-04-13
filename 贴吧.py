name=input('请输入贴吧名称:')
from urllib import request
from urllib import parse
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
date={
      'kw':name,
      'fr':'search',
      'ie':'utf-8'
      }
date_str=parse.urlencode(date)
url='https://tieba.baidu.com/f?'
new_url=url+date_str
r=request.Request(url=new_url,headers=headers)
content=request.urlopen(r).read().decode('utf-8')
file_name='%s.html'%name
print(file_name)


