# coding=utf-8
import pandas as pd
import pymysql
db = pymysql.connect(host='localhost', user='root', password='zxc123456', port=3306,db='taobao',charset='utf8')
cursor = db.cursor()
sql = 'INSERT INTO too(ALI_ID,省份,城市,行政区,标的物类型,标的物名称,拍卖次数,竞价周期,延时周期,保证金,优先购买权人,变卖预缴款,变卖价,变卖周期,监督单位,成交时间,交易类型,报名人数,出价次数,是否限购,抵押物名称,评估价格,信用,当前价格,延时次数,处置单位,结束时间,成交价格,初始价格,itemURL,经度,纬度,市场价格,加价幅度,sellOff,起拍价格,开始时间,支持贷款,围观人数,交易状态,采集时间) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
df1 = pd.read_csv('7.csv',encoding='gbk')
df = df1.astype(object).where(pd.notnull(df1), None)
a1 = df['ALI_ID'].values.tolist()
a2 = df['省份'].values.tolist()
a3 = df['城市'].values.tolist()
a4 = df['行政区'].values.tolist()
a5 = df['标的物类型'].values.tolist()
a6 = df['标的物名称'].values.tolist()
a7 = df['拍卖次数'].values.tolist()
a8 = df['竞价周期'].values.tolist()
a9 = df['延时周期'].values.tolist()
a10 = df['保证金'].values.tolist()
a11 = df['优先购买权人'].values.tolist()
a12 = df['变卖预缴款'].values.tolist()
a13 =  df['变卖价'].values.tolist()
a14 = df['变卖周期'].values.tolist()
a15 = df['监督单位'].values.tolist()
a16 = df['成交时间'].values.tolist()
a17 = df['交易类型'].values.tolist()
a18 = df['报名人数'].values.tolist()
a19 = df['出价次数'].values.tolist()
a20 = df['是否限购'].values.tolist()
a21 = df['抵押物名称'].values.tolist()
a22 = df['评估价格'].values.tolist()
a23 = df['信用'].values.tolist()
a24 = df['当前价格'].values.tolist()
a25 = df['延时次数'].values.tolist()
a26 = df['处置单位'].values.tolist()
a27 = df['结束时间'].values.tolist()
a28 = df['成交价格'].values.tolist()
a29 = df['初始价格'].values.tolist()
a30 = df['itemURL'].values.tolist()
a31 = df['经度'].values.tolist()
a32 = df['纬度'].values.tolist()
a33 = df['市场价格'].values.tolist()
a34 = df['加价幅度'].values.tolist()
a35 = df['sellOff'].values.tolist()
a36 = df['起拍价格'].values.tolist()
a37 = df['开始时间'].values.tolist()
a38 = df['支持贷款'].values.tolist()
a39 = df['围观人数'].values.tolist()
a40 = df['交易状态'].values.tolist()
a41 = df['采集时间'].values.tolist()

for i in range(len(a1)):

    cursor.execute(sql,(a1[i], a2[i], a3[i], a4[i], a5[i], a6[i], a7[i], a8[i], a9[i], a10[i], a11[i], a12[i], a13[i],a14[i],a15[i],
     a16[i],a17[i],a18[i], a19[i],a20[i], a21[i], a22[i], a23[i], a24[i], a25[i], a26[i], a27[i], a28[i],
     a29[i],a30[i],a31[i],a32[i],a33[i],a34[i],a35[i],
                        a36[i],a37[i],a38[i],
                        a39[i],a40[i],
                        a41[i]))
    # cursor.execute(sql, (a1[i],a2[i],a3[i],a4[i],a5[i],a6[i],a7[i],a8[i],a9[i],a10[i],a11[i],a12[i],a13[i],a14[i],a15[i],a16[i],a17[i],a18[i],a19[i],a19[i],a20[i],a21[i],a22[i],a23[i],a24[i],a25[i],a26[i],a27[i],a28[i],a29[i],a30[i],a31[i],a32[i],a33[i],a34[i],a35[i],a36[i],a37[i],a38[i],a39[i],a40[i],a41[i]))
db.commit()
