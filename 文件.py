import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
df = pd.read_excel('商业统计表.xlsx',sheet_name='Sheet1')
df['名称2'] = df['名称'].str.extract(r'([\D+]+[\D+])', expand=True)
df2 = df['名称2'].str.replace('-','')
df['名称2'] = df['名称2'].str.replace('-','')
print(df['名称2'].head(100))
df.to_csv('商业统计表2.csv',encoding='gbk')
df2.to_csv('1.csv',encoding='gbk')