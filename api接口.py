import requests
url=input('输入url:')
a=input('输入接口:User-Agent:')
b=input('输入接口:Cookie:')
c=input('输入接口:Host:')
d=input('输入接口:Referer:')

headers={
    'User-Agent':a,
    'Cookie':b,
    'Host':c,
    'Referer':d,

    }
response=requests.get(url,headers=headers)
print(response.text.encode().decode('utf-8'))