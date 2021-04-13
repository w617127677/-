import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')  #利用warnings模块来忽略匹配的警告
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('DEAL-1304#邯郸市#20200601#原始案例清洗-1.xlsx')
df = df.dropna(subset=['挂牌单价'])
print(df.columns)

# print(sns.distplot(df['挂牌单价']))
# # 建筑面积
# # 挂牌单价
# # 房屋类型
# # 总楼层
# var = '总楼层'
# data = pd.concat([df['挂牌单价'].astype('int64'), df[var]], axis=1)
# # plt.scatter(x=data['挂牌单价'],y=data['总楼层'])
# # plt.show()
# data.plot.scatter(x=var, y='挂牌单价')
# plt.show()
df1 = df[['建筑面积','挂牌总价','挂牌单价','总楼层']]
df1 = df1.dropna()
sns.distplot(df['挂牌单价'].astype('int64'))
plt.show()
# corrmat = df1.corr()
#
#
#
# sns.set()
# cols = ['建筑面积','挂牌总价','挂牌单价','总楼层']
# sns.pairplot(df1[cols], size = 5,)
# plt.show()