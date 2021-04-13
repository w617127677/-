import requests,re
import ssl#ssl免验证
ssl._create_default_https_context = ssl._create_unverified_context#ssl免验证
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
#requests.get('http://httpbin.org/ip', proxies={'http': 'https':'218.22.7.62:53281'})
r=requests.get('http://book.zongheng.com/showchapter/926124.html',headers=headers)
with open('冬元歌目录.html','w',encoding='utf-8')as fb:
    fb.write(r.text)
pattern=re.compile(r'<li class=" col-4">([\d\D]*?)</li>')
dd_list=pattern.findall(r.text)
f=open("小说目录.txt","w",encoding='utf-8')
for i in dd_list:
    
    a=re.compile(r'href="(.*?)" target="_blank"')
    b=a.findall(i)
    print(type(b))
    for a in b:
        f.write(a)
        f.write('\n')
    
    
    
    
    
    
    

f.close()
    