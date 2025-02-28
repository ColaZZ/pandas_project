import pandas as pd

df = pd.read_csv('qunar_free_trip.csv')
df.head()

# 按出发地、目的地分组查看价格均值
mean = df['价格'].groupby([df['出发地'], df['目的地']]).mean()

# 读取线路总数
df_ = pd.read_csv('qunar_free_trip.csv')

# 按出发地、目的地分组生成价格均值汇总表
df1 = df['价格'].groupby([df['出发地'], df['目的地']], as_index=False).mean()

# 将价格均值汇总表和线路总数表合并
pd.merge(df1, df_).head(10)

# 查看出发地vs目的地vs平均价格的数据透视表
df2 = pd.pivot_table(df, values=['价格'], index=['出发地'], columns=['目的地'])
df2.head(8)

# 从杭州出发的目的地vs去程方式vs平均价格的数据透视表
df3 = pd.pivot_table(df[df['出发地']=='杭州'], values=['价格'], index=['出发地', '目的地'], columns=['去程方式'])


