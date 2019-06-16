from datetime import datetime

import numpy as np
import pandas as pd
from pandas.tseries.offsets import Day, MonthEnd

price = pd.read_pickle('/Users/helena/Downloads/yahoo_price.pkl')
volume = pd.read_pickle('/Users/helena/Downloads/yahoo_volume.pkl')
print(price.head())
print('\n')
print(volume.head())
returns = price.pct_change()  # pct_change 用来计算同columns两个相邻的数字之间的变化率
print('\n')
print(returns.tail())
# correlation and covariance
print(returns['MSFT'].corr(returns['IBM']))
print(returns['MSFT'].cov(returns['IBM']))
print(returns.corr())
print(returns.cov())
print('\n')
print(returns.corrwith(returns.IBM))

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
uniques.sort()
print(uniques)
a = pd.value_counts(obj.values, sort=True)
print(a)

# isin 向量化集合成员关系检查
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])

# Index.get_indexer 返回index array 返回的是在非重复的values中对应的索引值
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
print(pd.Index(unique_vals).get_indexer(to_match))

data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
print(data)
result = data.apply(pd.value_counts)
print(result)

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
print(ts)
print(ts.index)
print(ts[::2])

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
                          '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)
print(dup_ts)
print(dup_ts.index.is_unique)
# 多个数据在同一时间戳的情况
grouped = dup_ts.groupby(level=0)  # 聚合那些有重复时间戳的数据
grouped.mean()
grouped.count()

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
         datetime(2011, 1, 7), datetime(2011, 1, 8),
         datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)
resampler = ts.resample('D')  # 'D' daily frequency
print(resampler)
print('\n')
print(pd.date_range('2000-01-01', '2000-12-01', freq='BM'))  # Business end of Month

nor_date = pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True)
print(nor_date)

# 频度前加一个整数，就能作为乘法器
print(pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4H'))

rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')  # WOM week of month
print(list(rng))

ts = pd.Series(np.random.randn(4),
               index=pd.date_range('1/1/2000', periods=4, freq='M'))

ts = pd.Series(np.random.randn(4),
               index=pd.date_range('1/1/2000', periods=4, freq='M'))
print(ts.shift(2))
print(ts.shift(-2))
# shift 计算序列的百分比变化
print(ts.shift(2, freq='M'))
print(ts.shift(3, freq='D'))
now = datetime(2011, 11, 17)
print(now + 3 * Day())
print(now + MonthEnd())

offset = MonthEnd()
print(now)
print(offset.rollback(now))

ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))
print(ts)
print(ts.groupby(offset.rollforward).mean())

values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
print(pd.unique(values))
print(pd.value_counts(values))

values2 = pd.Series([0, 1, 0, 0] * 2)
print(values2)
dim = pd.Series(['apple', 'orange'])
print(dim.take(values2))  # categorical/ dictionary-encoded

# categorical 用来保存着int类型的数据
fruits = ['apple', 'orange', 'apple', 'apple'] * 2
N = len(fruits)
df = pd.DataFrame({'fruit': fruits,
                   'basket_id': np.arange(N),
                   'count': np.random.randint(3, 15, size=N),
                   'weight': np.random.uniform(0, 4, size=N)},
                  columns=['basket_id', 'fruit', 'count', 'weight'])
print(df)

# convert string to the category
fruits_cat = df['fruit'].astype('category')
print(fruits_cat)
c = fruits_cat.values
print(type(c))
print('\n')
print(c.categories)
print(c.codes)

df['fruit'] = df['fruit'].astype('category')
print(df.fruit)

my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])
print(my_categories)

# categorical encoded data
categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]
my_cats_2 = pd.Categorical.from_codes(codes, categories)
print(my_cats_2)
order_cat = pd.Categorical.from_codes(codes, categories, ordered=True)
print(order_cat)
print(my_cats_2.as_ordered())

np.random.seed(12345)
draws = np.random.randn(1000)
print(draws[:5])
bins = pd.qcut(draws, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print(bins)
print(bins.codes[:10])
bins = pd.Series(bins, name='quartile')
result = (pd.Series(draws).groupby(bins).agg(['count', 'min', 'max']).reset_index())
print(result)

s = pd.Series(['a', 'b', 'c', 'd'] * 2)
cat_s = s.astype('category')
print(cat_s)
print(cat_s.cat.codes)
print(cat_s.cat.categories)
actual_categories = ['a', 'b', 'c', 'd', 'e']
cat_s2 = cat_s.cat.set_categories(actual_categories)  # 实际的类别超过了当前观测到的四个类别
print(cat_s2)
print(cat_s2.value_counts())
cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
print(cat_s3)

print(cat_s3.cat.remove_unused_categories())

cat_s = pd.Series(['a', 'b', 'c', 'd'] * 2, dtype='category')
print(pd.get_dummies(cat_s))
