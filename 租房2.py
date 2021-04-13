import requests,re
import ssl#ssl免验证
ssl._create_default_https_context = ssl._create_unverified_context#ssl免验证
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
#requests.get('http://httpbin.org/ip', proxies={'http': 'https':'218.22.7.62:53281'})
r=requests.get('https://sh.58.com/zufang/?PGTID=0d300008-0000-26bf-a292-96527f115c92&ClickID=2',headers=headers,proxies={'http':'http://113.59.99.138:8910'})
with open('租房.html','w',encoding='utf-8')as fb:
    fb.write(r.text)
pattern=re.compile(r'<li([\d\D]*?)</li>')
dd_list=pattern.findall(r.text)

for dd in dd_list:
    ti=re.compile(r'target="_blank"([\d\D]*?)</a>')
    a=ti.findall(dd)
    print(a)
   
    
