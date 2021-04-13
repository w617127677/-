import requests
from lxml import etree
import re
from selenium import webdriver
a=input('输入寻找的小说或者作者名:')
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

}
#
data={
'searchkey': a
}
response=requests.post('http://www.xbiquge.la/modules/article/waps.php',headers=headers,data=data)
# with open ('笔趣阁.txt','w',encoding='utf-8') as f:
#     f.write(response.text.encode('ISO-8859-1').decode('utf-8'))
# print(response.text.encode('ISO-8859-1').decode('utf-8'))
content=response.content.decode('utf-8')
html=etree.HTML(content)
one=html.xpath('//div[@id="main"]/div/form/table//tr[not(@align="center")]')
d=0
new_url=[]
xiaoshuo=[]
for i in one:
    d=d+1
    name=i.xpath('./td[1]/a/text()')
    url=i.xpath('./td[1]/a/@href')
    new_url.append(url[0])
    xiaoshuo.append(name[0])
    print('{}.'.format(d),name[0])
q=int(input('请选择你要搜索的序号:'))

geturl=requests.get(new_url[q-1],headers=headers)
# with open ('笔趣阁.txt','w',encoding='utf-8') as f:
#     f.write(geturl.text.encode('ISO-8859-1').decode('utf-8'))
content1=geturl.content.decode('utf-8')
html1=etree.HTML(content1)
a1=html1.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a')
# print(a1)
for qq in a1:
    book_name=qq.xpath('./text()')
    book_url=qq.xpath('./@href')
    # with open('{}.txt'.format(xiaoshuo[new_url[q-1]]),'a',encoding='utf-8')as fb:
    #     fb.write()
    bookurl='http://www.xbiquge.la/'+book_url[0]
    print(book_name[0],'下载成功')
    # print(book_name[0],bookurl)
    response_get=requests.get(bookurl,headers=headers)
    content_url = response_get.content.decode('utf-8')
    html = etree.HTML(content_url)
    chater = html.xpath('//div[@class="content_read"]/div/div[2]/h1/text()')
    chater_content = html.xpath('//div[@id="content"]/text()')


    with open('{}.txt'.format(xiaoshuo[q-1]), 'a', encoding='utf-8') as fb:



        for i in chater_content:
            fb.write(i)
print('下载完成')





