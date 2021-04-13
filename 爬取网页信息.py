import requests,re
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
#requests.get('http://httpbin.org/ip', proxies={'http': 'https':'218.22.7.62:53281'})
r=requests.get('https://maoyan.com/board',headers=headers,proxies={'http':'http://113.59.99.138:8910'})
with open('66666.html','w',encoding='utf-8')as fb:
    fb.write(r.text)
pattern=re.compile(r'<dd>([\d\D]*?)</dd>')
dd_list=pattern.findall(r.text)
print(dd_list)
for dd in dd_list:
    ti=re.compile(r'<a.*?>(.*?)</a>')
    a=ti.findall(dd)
    zhuyan=re.compile(r'<p class="star">\n(.*?)\n')
    b=zhuyan.findall(dd)
    time=re.compile(r'<p class="releasetime">(.*?)/p>')
    c=time.findall(dd)
    d=re.compile(r'<i class="integer">(.*?)</i>')
    e=d.findall(dd)
    f=re.compile(r'<i class="fraction">(.*?)</i>')
    g=f.findall(dd)
    six=e[0] + g[0]
   
    print(a[0],b[0],six[0])

    


    
    
    #requests.get('http://httpbin.org/ip', proxies={'http': '121.193.143.249:80'})