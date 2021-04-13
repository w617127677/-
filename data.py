import pymysql

db = pymysql.connect(host='localhost', user='root', password='zxc123456', port=3306,db='taobao')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS taooo ( ALI_ID VARCHAR(255) , ' \
      '省份 VARCHAR(255),城市 VARCHAR(255),行政区 VARCHAR(255),标的物类型 VARCHAR(255),标的物名称 VARCHAR(255),拍卖次数 VARCHAR(255),竞价周期 VARCHAR(255),延时周期 VARCHAR(255),保证金 VARCHAR(255),优先购买权人 VARCHAR(255),变卖预缴款 VARCHAR(255),变卖价 VARCHAR(255),变卖周期 VARCHAR(255),监督单位 VARCHAR(255),成交时间 VARCHAR(255),交易类型 VARCHAR(255),报名人数 VARCHAR(255),出价次数 VARCHAR(255),是否限购 VARCHAR(255),抵押物名称 VARCHAR(255),评估价格 VARCHAR(255),信用 VARCHAR(255),当前价格 VARCHAR(255),延时次数 VARCHAR(255),处置单位 VARCHAR(255),结束时间 VARCHAR(255),成交价格 VARCHAR(255),初始价格 VARCHAR(255),itemURL VARCHAR(255),经度 VARCHAR(255),纬度 VARCHAR(255),市场价格 VARCHAR(255),加价幅度 VARCHAR(255),sellOff VARCHAR(255),起拍价格 VARCHAR(255),开始时间 VARCHAR(255),支持贷款 VARCHAR(255),围观人数 VARCHAR(255),交易状态 VARCHAR(255),采集时间 VARCHAR(255))'
# {"ALI_ID":a1,"省份":'广东',"城市":"深圳","行政区":"罗湖","标的物类型":"住宅用房","标的物名称":a2,"拍卖次数":a3,"竞价周期":a4,"延时周期":a5,"保证金":a6,"优先购买权人":a7,
#                     "变卖预缴款":"","变卖价":"","变卖周期":'',"监督单位":'',"成交时间":a10,"交易类型":"拍卖","报名人数":a11,
#                     '出价次数':a12,'是否限购':a13,'抵押物名称':a2,"评估价格":a14,"信用":a15,'当前价格':a16,'延时次数':a17,'处置单位':a18,'结束时间':a19,"成交价格":a20,"初始价格":a21,'itemURL':a22,'经度':a23,
#                     "纬度":a24,"市场价格":a25,"加价幅度":a26,"sellOff":a27,"起拍价格":a28,"开始时间":a29,"支持贷款":a30,
#                     "围观人数":a31,"交易状态":a32,"采集时间":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#                     }
cursor.execute(sql)
db.close()