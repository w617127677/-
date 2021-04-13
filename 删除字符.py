# s = '\tabc\t123\tisk'
# a=s.replace('\t', '')
# print(a)
f=open('小说.txt','r',encoding='utf-8')
c=f.read()

a=c.replace('</p><p>', '')
b=a.replace('<p>', '')
d=b.replace('</p>', '')
e=d.replace('/n','')
print(type(e))
fc=open("小说66.txt","w",encoding='utf-8')
fc.write(e)
