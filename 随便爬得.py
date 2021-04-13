import requests,re
import parse
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
#requests.get('http://httpbin.org/ip', proxies={'http': 'https':'218.22.7.62:53281'})
r=requests.get('https://www.3733.com/news/106378.html',headers=headers,proxies={'http':'http://113.59.99.138:8910'})
with open('suibian.html','w',encoding='utf-8')as fb:
    fb.write(r.text)
n=re.compile(r'<span style="font-size: 14px;">(.*?)</span>')
c=n.findall(r.text)
print(c)
            