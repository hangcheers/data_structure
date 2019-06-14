import numpy as np
import pandas as pd

obj = pd.Series([4, 7, -5, 3])
print(obj)  # 左边表示Index 右边表示对应的value  index - value
print(obj.values)
print(obj.index)

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
# 根据index来选择索引
print(obj2['a'])
print(obj2[obj2 > 3])

# series dict
sdata = {'Ohio': 3500, 'Texas': 7100, 'Oregon': 1600, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
states = ['Utah', 'Ohio', 'Oregon', 'Texas']  # 可以指定列在dataframe中的顺序
obj3 = pd.Series(sdata, index=states)
obj3.name = 'population'
obj3.index.name = 'state'
print(obj3)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}  # dict形式来构建dataframe

frame = pd.DataFrame(data)
print(frame)
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))
print(frame.columns)
print(frame.year)
# frame.column 对应的是DataFrame中具体的某一列
# 对于行要用， frame.loc[]
print(frame.loc[3])

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
frame2['debt'] = np.arange(6.)  # 可以把list或者array赋值给dataframe的column
print(frame2)
print('\n')
obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj)
index = obj.index
print(index[1:])

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
# 在创建object时，可以遵循一个新的index
# 调用reindex，如果没有index相对应的数据，会引入缺失数据
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
# 在reindex的时候，如果需要修改值「method」
frame = pd.DataFrame(np.arange(9).reshape(3, 3),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
states = ['Texas', 'Ohio', 'California']
print('\n')
print(frame2.reindex(columns=states))
print(frame2.loc[['a', 'b', 'c', 'd'], states])
print('\n')
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj.drop(['c', 'd']))

data = pd.DataFrame(np.arange(16).reshape(4, 4),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.drop(['Colorado']))
print(data.drop('two', axis='columns'))

# index, selection, filtering
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[2:4])
# row
print(obj[['b', 'a', 'c']])
print(obj[obj < 2])
print(obj['b':'c'])

data = pd.DataFrame(np.arange(16).reshape(4, 4),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data[:2])
print(data[data['three'] > 5])

# selection with loc and iloc
# loc  ---- label
# iloc ---- integer
# 使用loc(for label)或ilco(for integers)
print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[1, [1, 2]])

# 不同index的object的算数计算
# 如果两个dataframe的index各不相同，最后得到的index是两个index的合集
# 此外 数据对齐（data alignment）同时发生在行和列上
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])

df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1)
print(df2)
print(df1 + df2)

df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1 - df2)

# 缺失值填充
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))
df2.loc[1, 'b'] = np.NAN
print(df1)
print('\n')
print(df2)
print('\n')
# print(df1.add(df2,fill_value = 0))
print(df1.reindex(columns=df2.columns, fill_value=0))

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame - series)
series2 = pd.Series(range(3), index=list('def'))
print(frame + series2)

# 把一个作用在一维数组上的函数，应用在一行或者一列上。
f = lambda x: x.max() - x.min()
print('\n')
print(frame)
print('\n')
print(frame.apply(f))  # apply 返回的是一个含有多个值的series
# axis 的参数是用来匹配轴的
print(frame.apply(f, axis='columns'))  # axis = 'columns' 函数被应用在每一行上
series3 = frame['d']
print(frame.sub(series3, axis='index'))  # 匹配dataframe的row index

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

f = lambda x: x.max() - x.min()
print(frame.apply(f))
print(frame.apply(f,axis='columns'))
format = lambda x: '%.2f' %x
print(frame.applymap(format)) # 格式化浮点数
print('\n')
print(frame['e'].map(format))
