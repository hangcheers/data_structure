import numpy as np
import pandas as pd

obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
# sort
print(obj.sort_index())
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
print(frame.sort_index(axis=1))

obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())  # 缺失值(np.nan)会排在后面

frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
print(df.sum())
print(df.sum(axis='columns'))  # 计算的时候，NA会被排除
print(df.describe())  # describe 能产生多维的汇总数据

obj = pd.Series(['a', 'a', 'b', 'c'] * 2)
print(obj)
print('\n')
print(obj.describe())

string_data = pd.Series(['arrdvark', 'artichoke', np.nan, 'avocado'])
string_data[0] = None
print(string_data.isnull())

# nan (not available）要么是数据不存在，要么是存在但是不能被检测到
# 做缺失值的数据分析 我们要去确定：是否是数据收集的问题，或者是缺失值带来潜在的偏见

print(string_data.dropna())

data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],
                     [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
print(data)
cleaned = data.dropna(how='all')
print(cleaned)
# 如果删除列，设置axis = 1
cleaned_2 = data.dropna(how='all', axis=1)

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = np.nan
df.iloc[:2, 2] = np.nan
# df.fillna(0)
print(np.round(df.fillna(0), 2))  # fillna 来对缺失值做填补
print('\n')
df.fillna({1: 0.5, 2: 0})
print(df)  # 传入dict 对不同的列用不同的值进行替换

df.fillna({1: 0.5, 2: 0}, inplace=True)  # inplace直接改变原有的数据
print('\n')
print(df)

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = np.nan
df.iloc[4:, 2] = np.nan
print(df.fillna(method='ffill', limit=2))

# 数据清洗就是在Loading, clearing, transforming, rearranging

# 删除重复的值
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4],
                     'v1': np.arange(7)})
print(data.duplicated())  # 返回一个boolean series，根据前一行来判断这一行有没有重复
a = data.drop_duplicates()
print(a)
print(data.drop_duplicates(['k1']))  # duplicate & drop_duplicate 默认保留第一次观测到的数值组合

data2 = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                               'Pastrami', 'corned beef', 'Bacon',
                               'pastrami', 'honey ham', 'nova lox'],
                      'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}
lowercased = data2['food'].str.lower()  # 统一str
data2['animal'] = lowercased.map(meat_to_animal)
print(data2)

# 使用map 用于element-wise转换或者其他一些数据清洗操作
new_data2 = data2['food'].map(lambda x: meat_to_animal[x.lower()])
print(new_data2)

# replace values
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data.replace([-999, -1000], [np.nan, 0], inplace=True)
print(data)

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
data.index.map(lambda x: x[:4].upper())
data.rename(index=str.title, columns=str.upper, inplace=True)
print(data)

# 连续型数据离散化
age = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(age, bins)
print(cats)
print('\n')
print(cats.codes)  # ages label
print(cats.categories)
print(pd.value_counts(cats))  # pandas.cut 后bin的数量

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
cats2 = pd.cut(age, bins, labels=group_names)
print(cats2)

data = np.random.rand(100)
print(pd.cut(data, 4, precision=2))  # precision = 2 表示精确到小数点后两位
b = pd.qcut(data, 4, precision=2)  # qcut是按百分比来切的，可以得到等量的bins
print(pd.value_counts(b))
# cut和qcut等离散函数对于量化和群聚分析很有用
