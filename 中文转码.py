name=input('请输入百度名称：')
from urllib import parse
from urllib import request
import ssl
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
url='https://www.so.com/s?'
date={
      'q':name,
      'src':'srp',
      'fr':'hao_360so_a1004_b_cube',
      'psid':'f367ca7e55c95cdb7636de676938f235'
      }
ssl._create_default_https_context=ssl._create_unverified_context#ssl免验证
date_str=parse.urlencode(date)
new_url=url+date_str
r=request.Request(url=new_url,headers=headers)
content=request.urlopen(r).read().decode('utf-8')
file_name='%s.html'%name
print(file_name)
