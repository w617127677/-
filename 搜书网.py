import requests
from lxml import etree
search=input('查找书名:')
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
response=requests.get('https://www.99csw.com/book/search.php?q={}'.format(search),headers=headers)
# with open('搜书网.txt','wb')as f:
#     f.write(response.content)
# print(response.text.encode('ISO-8859-1').decode('utf-8'))
content=response.content
html=etree.HTML(content)
a=html.xpath('//div[@id="right"]/ul/li')
c=0
new_url=[]
for i in a:
    c=c+1
    name=i.xpath('./h2/a/@title')
    url=i.xpath('./h2/a/@href')
    new_url.append(url[0])
    print('{}'.format(c),name[0],url[0])
number=int(input('请输入你要寻找的序号:'))
new_url='https://www.99csw.com'+new_url[number-1]
print(new_url)
new_response=requests.get(new_url,headers=headers)
book_content=new_response.content
book_html=etree.HTML(book_content)
book=book_html.xpath('//dl[@id="dir"]/dd')
for g in book:
    book_url=g.xpath('./a/@href')
    print(book_url)
