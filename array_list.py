import numpy as np
import pandas as pd

# numpy部分基础操作
a = np.array([i for i in range(10)])
print(a)
print("\nnumber of dim", a.ndim)
print("\nshape", a.shape)
print("\nsize", a.size)

b = np.arange(10, 22, 2).reshape(2, 3)
print("\nb", b)
print("\nsum", np.sum(b))
print("\nsum", np.sum(b, axis=0))  # axis = 0 是纵向求和
print("\nmin", np.min(b, axis=0))
print("\nmax", np.max(b, axis=0))
print("\nflatten", b.flatten())

for row in b:
    print(row)

for column in b.T:
    print(column)
print('\n')
# numpy array 合并
A = np.array([4, 1, 2])
B = np.array([5, 2, 3])
print(np.vstack((A, B)))  # 纵向合并
print('\n')
print(np.hstack((A, B)))  # 横向合并
# numpy array 分割
C = np.arange(12).reshape(3, 4)
print("\nC", C)
print(np.split(C, 2, axis=1))  # 纵向分割
print(np.split(C, 3, axis=0))  # 横向分割
print(np.array_split(C, 3, axis=1))  # 不等量分割

# pandas部分基础操作

s = pd.Series([1, 3, 6, np.NAN, 44])
print(s)

df1 = pd.DataFrame(np.arange(12).reshape(3, 4))
print("\n")
print(df1)
df2 = pd.DataFrame({'A': 1, 'B': pd.Timestamp('20190527'),
                    'C': pd.Series([1, 2, 3, 4], dtype='float32'),
                    'D': pd.Categorical(["test", "train", "test", "train"])})
print("\n")
print(df2)
print(df2.dtypes)
print(df2.columns)
print(df2.values)
print(df2.sort_index(axis=1, ascending=True))  # 对序列索引排序
print(df2.sort_values(by='C', ascending=False))  # 对数据值排序

dates = pd.date_range('20190525', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)
print("\n")
print(df[0:2])  # [A:B]区间是[A,B）
print("\n")
print(df['a'])  # select the df
print("\n")
print(df.loc['20190528'])  # 根据标签名字来选择某一行对数据loc
print(df.loc[:, ['a', 'b']])
print("\n")
print(df.iloc[2:5, 1:3])
print(df[df.a > 10])  # 通过约束条件选择当前数据
# 同样也可以根据索引或标签确定需要修改对值对位置
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
df.iloc[2, 3] = np.nan
print("\n")
print(df)
df_noNan = df.dropna(axis=0, how='any')  # 直接去掉含有nan的行或列
print("\n")
print(df_noNan)
df_fillNan = df.fillna(value=-1)  # 将含有nan的地方替换位-1
print("\n")
print(df_fillNan)

# pandas 进行数据合并
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)), columns=['a', 'b', 'c', 'd'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a', 'b', 'c', 'd'])

res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # ignore_index表示重置index, axis = 0表示纵向合并
print(res)
print("\n")
res1 = pd.concat([df1, df2], axis=1)
print(res1)
df4 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['b', 'c', 'd', 'e'])
res2 = pd.concat([df1, df4], axis=0, join='outer', sort=False)
print("\n")
print(res2)

# pandas 进行数据添加 将S1合并到表格中并重置index
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res4 = df1.append(s1, ignore_index=True)
print("\n")
print(res4)
