import requests
from lxml import etree
import re
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'

}
response=requests.get('http://www.xbiquge.la//14/14930/24287805.html',headers=headers)
# with open ('笔趣阁1.txt','w',encoding='utf-8') as f:
#     f.write(response.text.encode('ISO-8859-1').decode('utf-8'))
# print(response.text.encode('ISO-8859-1').decode('utf-8'))
content=response.content.decode('utf-8')
html=etree.HTML(content)
chater=html.xpath('//div[@class="content_read"]/div/div[2]/h1/text()')
chater_content=html.xpath('//div[@id="content"]/text()')
with open ('笔趣阁2.txt','w',encoding='utf-8') as f:

    f.write(chater[0]+'\n')
    for i in chater_content:
        f.write(i)

# chater_content=html.xpath('//div[@id="content"]/text()')
# re.sub('','',chater_content[0])
# for i in chater_content:
#
#     print(i)



