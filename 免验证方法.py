from urllib import request
import re
import ssl#ssl免验证

proxy_handler =request.ProxyHandler({'https':'58.247.127.145:53281'})
opener= request.build_opener(proxy_handler)
ssl._create_default_https_context = ssl._create_unverified_context#ssl免验证

r= opener.open('http://www.maoyan.com')

content=r.read().decode('utf-8')
with open('lai.html','w',encoding='utf-8')as fb:
    fb.write(content)
    print(content)
pattern=re.compile(r'<dd>([\d\D]*?)</dd>')
dd_list=pattern.findall(content)
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
    print(a[0],b[0],c[0],six)
#requests.get(url=url,headers=headers,verify=False)request免验证
#requests.get('http://httpbin.org/ip', proxies={'http': '121.193.143.249:80'})
#proxy_handler = urllib.request.ProxyHandler({'http': 'http://121.193.143.249:80/'})
#opener = urllib.request.build_opener(proxy_handler)
#r = opener.open('http://httpbin.org/ip')
#print(r.read())