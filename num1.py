import matplotlib.pyplot as plt
import numpy as np

data = [6, 7.5, 8, 0, 1]
arr1 = np.array(data)
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.dtype)

arr = np.array([i + 1 for i in range(5)])
print(arr)
print(arr.dtype)
float_arr = arr.astype(np.float64)  # astype 是用来进行类型转化的
print(float_arr.dtype)

numeric_string = np.array(['1.25', '-9.5', '4'], dtype=np.string_)
print(numeric_string)

arry = np.arange(10)
arry[5:8] = 12
print(arry)

arr_slice = arry[5:8]
print(arr_slice)
# 改变arr_slice 会改变原有array对应的元素
# numpy  array 的切片后的结果只是一个view，用来代表原有array对应的元素，而不是新创建了一个array
arr_slice[1] = 0
print(arry)

arry_2 = np.array([[1, 2, 3], [4, 5, 6]])
# 在二维数组里，单一的索引指代的是一维数组
print(arry_2[0])
arry_3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  # 2 x 2 x 3
print(arry_3)
print(arry_3[0])  # 1 x 2 x 3
old_values = arry_3[0].copy()
arry_3[0] = 42
print(old_values)
print(arry_3)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(names)
data = np.random.randn(7, 4)
print(data)

print(names == 'Bob')
print(data[names == 'Bob'])

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print(arr)

# 按一定的顺序选出几行，可以用整数list或者整数ndarray来指定顺序
print(arr[[4, 3, 0]])

arr = np.arange(15).reshape((3, 5))
print(arr.T)
print(np.dot(arr, arr.T))

a = np.random.randn(3)
b = np.random.randn(3)
print(a)
print('\n')
print(b)
print(np.maximum(a, b))

m, n = (5, 3)
x = np.linspace(0, 1, 5)
y = np.linspace(0, 1, 3)
X, Y = np.meshgrid(x, y)
# zip 将可迭代的对象作为参数，将对象中对应的元素打包成元组，返回
# 用zip可以得到网格平面上坐标点的数据
z = [i for i in zip(X.flat, Y.flat)]
print(z)

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()

# numpy where ( x if condition else y )
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
z = [i for i in zip(xarr, yarr)]
print(z)
# np.where 在数据分析中就是基于一个数组，产生一个新的数组值
result = np.where(cond, xarr, yarr)
print(result)

arr = np.random.randn(3, 3)
print(arr)
result2 = np.where(arr > 0, 2, arr)  # set only positive value to 2
print(result2)

arr = np.random.randn(100)
print((arr > 0).sum())  # number of positive values

bools = np.array([False, False, True])
print(bools.any())  # 只要有一个true就返回true
print(bools.all())  # 检测数组都是true 才返回true

# arr.sort 直接调用数组sort的方法会改变原有数组的顺序
# np.sort 会产生一个新的排序结果

arr = np.random.randn(2, 3)
print(arr)
arr.sort()
print(arr)

# 计算分位数的方法是先给数组排序，然后选择某个排名的值
large_arr = np.random.randn(100)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])

ints = np.array([3, 3, 3, 2, 2, 1, 4, 4])
print(np.unique(ints))  # np.unique 能返回排好序且不重复的值

X = np.round(np.random.randn(2, 5), 3)  # np.round 可以控制小数点后的位数
X.sort()
print(X)
