# Python数据分析

## Numpy

......

### 1.数组创建

```python
#创建数组的几种方式（常用方式）
import numpy as np
'''
注意：在数组里面存入的数据类型只能是一致的，要么都是整型要么都是字符形等等，
因为这样子规范的话系统在评估和预留内存时就能减少很多浪费从而提高运行和处理效率
'''
#1.使用np.array来创建数组
ex = np.array([1,2,3,4])
print(ex,type(ex))
#注：想知道某个对象的方法如何使用时使用help()函数，例如：
help(np.array) #注意括号不用加

#2.使用np.arange来创建数组
ex = np.arange(5)
print(ex,type(ex))

#3.使用np.random.random来创建一个n行n列的数组
ex = np.random.random((2,2))
print(ex)
ex = np.random.randint(0,9,size=(3,3,)) #输出数值为0-10之间的三行三列的数组
print(ex)

#使用函数来生成特殊的数组
ex = np.zeros((5,2)) #生成一个全是零的五行两列的数组
print(ex)
ex = np.ones((5,2)) #生成一个全是一的五行两列的数组
print(ex)
ex = np.full((5,2),8) #生成一个全是8的五行两列的数组
print(ex)
ex = np.eye(3) #生成一个斜线是一其他元素都是零的三行三列的数组（对称的--只能传一个值，这个值既是行又是列）
print(ex)
```

### 2.数组的数据类型

```python
#数组的数据类型
import numpy as np

'''
因为np数组里面只能存储一种类型的数据，因此可以使用dtype来查看数组的数据类型
'''
ex = np.random.randint((2,3))
print(ex.dtype)

'''
dtype的常见数据类型：

bool:布尔类型，值为True或False  特征码-b

整数类型的八种:特征码-u:无符号整型 i:有符号整型
int8、uint8:有符号和无符号的8位整数
int16、uint16:有符号和无符号的16位整数
int32、uint32:有符号和无符号的32位整数
int64、uint64:有符号和无符号的64位整数

半精度浮点数的三种:特征码-f
float16:半精度浮点数 16位
float32:半精度浮点数 32位
float64:半精度浮点数 64位

复数的两种:特征码-c
complex64:复数，分别用两个32位浮数表示实部和虚部
complex128:复数，分别用两个128位浮数表示实部和虚部

python对象:特征码-O
object_:Python对象

字符串 S,a
sting_:固定长度的字符串类型

unicode_:固定长度的unicode类型 特征码-U

之所以要分的怎么详细，就是因为按需分配内存，减少内存浪费，提高处理效率
'''
#比如，你已经知道你的数字不会超过128时就可以指定int8
ex = np.array([1,2,3,4,5,6],dtype=np.int8)
print(ex)
print(ex.dtype)
#其他类型的自己确定并指定

#使用astype来修改数据类型
uex = ex.astype(np.int64)
print("修改完："+str(uex.dtype))
print("未修改时："+str(ex.dtype))
```

### 3.多维数组

```python
#多维数组及其简单操作
import numpy as np

#通过ndim属性来获得数组的维度
ex1 = np.array([1,2,3])
print(ex1.ndim)
ex2 = np.array([[1,2,3],[4,5,6]])
print(ex2.ndim)
ex3 = np.array([
    [
        [1,2,3],
        [1,2,3]
    ],
    [
        [1,2,3],
        [1,2,3]
    ]
])
print(ex3.ndim)

#通过shape属性来查看数组是几行几列的(输出括号内有几个元素就是几维度的)
print(ex1.shape)
print(ex2.shape)
print(ex3.shape)

#通过reshape来给数组进行维度的修改并赋值给新的对象（注意：这方法不会修改原本的数组）
#例如修改ex3
ex = ex3.reshape((2,6)) #注意ex3原本有十二个数，所以修改时虽然是看自己心情，但是元素个数还是应该一致，即行乘以列=12
print(ex)
#注意：修改成一维需要留意
ex = ex3.reshape((12,)) #转成一维就这样就行，不用写，直接所有元素然后逗号
print(ex)
print(ex.ndim)
ex = ex3.flatten() #更简单的将数多维数组转换成一维数组的方法
print(ex)

#用size来获取这个数组的元素（不管几维度的，就获取全部的元素）
ex = ex3.size
print(ex)

#使用itemsize来获取数组中每一个元素所占的大小，单位是字节
print(ex3.itemsize)
print(ex3.dtype)
```

### 4.数组索引与切片

```python

''#数组索引和切片操作
import numpy as np

#当是一维数组的时候
'''
其索引和切片操作和python列表的是一致的
'''

#当是二维数组当时候
'''
那么在中括号中，给两个值，两个值是通过逗号分隔的，逗号前面是行，后面是列。
如果中括号中只有一个值，那么就是代表是行。
如果是多维数组（这里以二维数组举例），那么行的部分和列的部分，都是遵循一维数组的方式，
可以使用整型，切片，还可以使用中括号的形式，来代表不连续的。
比如，a[[1,2],[3,4]],那么返回的就是(1,3),(2,4)两个值。
'''

#代码展示
ex = np.array([1,2,3,4,5])
print(ex[:])
ex = np.random.randint(0,10,size=(4,4,))
print(ex)
print(ex[0]) #输出第一行
print(ex[0,2]) #输出第一行第三个元素
print(ex[[0,3]]) #输出第一行和第四行 #print(ex[[0,3],[2,3]]) 0,3:第一到第四行，2,3第三到第四列
print(ex[0:3]) #输出第一行到三行 ------ 上面，是指定几行几列，下面这个是切片，左臂右开
print(ex[0:3,1:3]) #输出从一行到第三行和从第二列到第三列的交集
```

### 5.布尔索引

```python
#布尔索引
import numpy as np
'''
当我们想从一个数组里面输出符合特定条件元素时,直接进行条件判断，
会返回一个True and False的数组，
再将这个判断的结果当作原数组索引即可得到满足特定条件的元素。
'''
#根据特定条件输出
ex = np.arange(0,48).reshape(6,8)
print(ex)
print(ex < 20) #返回一个True and False的数组
print(ex[ex < 20]) #再将这个判断的结果当作原数组索引即可得到满足特定条件的元素
'''注意：bool运算的相关符均可用来进行条件判断'''
print(ex[(ex < 20) | (ex > 30)]) #注意：要分别加上括号，否则报错

'''
值修改总结：
根据索引和切片来替换
使用条件索引来替换
使用where函数来实现
'''

#修改数组中的值
ex = np.random.randint(0,10,size=(3,5))
print(ex)
ex[0] = 0 #将数组第一行全部元素替换成0
print(ex)
ex[1] = np.array([1,2,3,4,5]) #将数组第二行替换成我们自定义的数组

#根据布尔条件来进行值的修改
ex = np.arange(0,40).reshape((5,8))
print(ex)
ex[ex < 10] = 1 #将所有小于10的元素均替换成1
print(ex)

#where函数的使用
ex = np.random.randint(0,10,size=(2,5))
res = np.where(ex <= 5)
print(res) #这时会输出符合条件的元素的坐标
res = np.where(ex <= 5,0,1)
print(res) #这样小于等于5的就会被替换为0，其他为1
```

### 6.数组广播机制

```python
#数组广播机制
'''
广播原则：如果两个数组的后缘维度，(即从末尾开始算起的维度)的轴长度相符或其中一方的长度为1（i,j-j,p->两个j相同最终i,p），则认为他们是广播兼容的。广播会在缺失和(或)长度为1的维度上进行
注意：直接+-*的运算运用的均是广播机制的运算，而需要线性代数里面的运算时有相关函数(例如矩阵相乘:利用dot())
'''
import numpy as np

'''
总结：
数组和数字可以直接进行运算
两个shape相同的数组时可以进行运算的
如果两个shape不同的数组，想要进行运算，那么需要看他们是否满足广播原则--在上面
'''

#数组与数的运算
print("数组与数的运算结果：")
ex = np.array([1,2,3,4,5])
print(ex)
ex = ex * 0 #数组广播机制会将数组中的每一个数都乘以0
print(ex)

#数组与数组的计算

#同行同列数组间的运算
print("同形状的数组之间的运算：")
ex1 = np.random.randint(0,10,size=(2,5))
ex2 = np.random.randint(10,20,size=(2,5))
print(ex1)
print(ex2)
print("-"*20)
ex = ex1 + ex2 #同行同列时会将相对应的位置的元素进行相加
print(ex)
print("-"*20)
ex = ex1 - ex2 #同行同列时会将相对应的位置的元素进行相减
print(ex)
print("-"*20)
ex = ex1 * ex2 #同行同列时会将相对应的位置的元素进行相乘
print(ex)

#形状不同时：数组之间不能进行运算

#但，当行数一样，然后列有一个是一时，可以进行运算
print("行同列不同且有一时")
ex1 = np.random.randint(0,5,size=(5,1))
ex2 = np.random.randint(0,5,size=(5,3))
print(ex1)
print(ex2)
print("-"*20)
ex = ex1 + ex2 #这种情况下，只有一列的哪一个数组会和另一个行数一样的数组的每一列进行相加(一列分别与五列分别相加)
print(ex)
print("-"*20)
ex = ex1 - ex2 #这种情况下，只有一列的哪一个数组会和另一个行数一样的数组的每一列进行相减(一列分别与五列分别相减)
print(ex)
print("-"*20)
ex = ex1 * ex2 #相乘时，只有一列的那个数组的第一个元素会和行数相同的那个数组的第一个的元素分别相乘，第二个和第二行的...依此类推
print(ex)

#当列数相同，然后行只有一个时，也可以进行运算
print("列同行不同且有一时")
ex1 = np.random.randint(0,5,size=(1,5))
ex2 = np.random.randint(0,5,size=(5,5))
print(ex1)
print(ex2)
print("-"*20)
ex = ex1 + ex2 #这种情况下，只有一行的那个数组，哪一行会分别与另一个数组的每一行进行相加
print(ex)
print("-"*20)
ex = ex1 - ex2 #这种情况下，只有一行的那个数组，哪一行会分别与另一个数组的每一行进行相减
print(ex)
print("-"*20)
ex = ex1 * ex2 #这种情况下，只有一行的那个数组，哪一行会分别与另一个数组的每一行进行相乘
print(ex)
```

### 7.改变数组形状

```python
#数组形状的操作
import numpy as np

#1.reshape和resize方法：两个方法都是用来修改数组形状的，但有一些不同。
'''
reshape不会修改原数组的，而resize是会修改原数组本身的
'''
ex1 = np.random.randint(0,10,size=(3,4))
print(ex1)
print(ex1.reshape((2,6))) #没改变ex1数组，会返回一个新数组
print(ex1)

ex2 = np.random.randint(10,20,size=(3,4))
print(ex2)
print(ex2.resize((2,6))) #返回None，不返回东西，直接把原数组给改了
print(ex2)

#flatten和ravel方法：两个数组都是将多维度数组转换为一维数组,都不会对原数组造成影响，但有一些不同。
'''
flatten是将数组转换为一维数组后，然后将这个拷贝返回回去，所以后续对这个返回值进行修改不会影响之前的数组
ravel是将数组转换为一维数组后，将这个视图(可理解为引用)返回回去，所以后续对这个返回值进行修改会影响到之前的数组
flatten类似于拷贝原数组，ravel类似于拷贝原数组的指针
'''
ex1 = np.random.randint(0,10,size=(3,4))
print(ex1)
print(ex1.flatten())
ex2 = np.random.randint(0,10,size=(3,4))
print(ex2)
print(ex2.ravel())

#2.不同数组的组合：两个数组进行组合从而形成一个新的数组
'''
其实就是两种情况:将一个横条垂直放到有多个横条的前面或后面，或将一个竖条水平放到有多个竖条的左边或右边(想象成图)
'''
'''
总结：
hstack代表在水平方向上叠加(从左往右)，如果想要叠加成功，那么他们的行必须一致
vstack代表垂垂直方向上叠加(从上到下)，如果想要叠加成功，那么他们的列必须一致
concatenate可以自定义axis参数具体指定在那个方向上叠加，为1时为水平叠加，0时为垂直叠加，如果为None那么最后会转换成一维数组
'''
print("-"*20)
#vstack:将数组按垂直方向进行叠加(需要列数相同)
ex1 = np.random.randint(0,10,size=(2,4))
ex2 = np.random.randint(0,10,size=(1,4))
print(ex1)
print(ex2)
ex = np.vstack([ex1,ex2]) #注意:中括号，拼接时想让那个数组在前面就把其当作第一个参数
print(ex)
#hstack:将数组按水平方向进行叠加(需要行数相同)
print("-"*20)
ex1 = np.random.randint(0,10,size=(5,1))
ex2 = np.random.randint(0,10,size=(5,4))
print(ex1)
print(ex2)
ex = np.hstack([ex1,ex2])
print(ex)
#concatenate(a,b,axis):这个是可以自定义是垂直叠加还是水平叠加(axis=0代表垂直叠加，axis=1代表水平叠加)
print("-"*20)
ex1 = np.random.randint(0,10,size=(2,4))
ex2 = np.random.randint(0,10,size=(1,4))
print(ex1)
print(ex2)
ex = np.concatenate([ex1,ex2],axis=0) #注意:中括号，拼接时想让那个数组在前面就把其当作第一个参数
print(ex)

print("-"*20)
ex1 = np.random.randint(0,10,size=(5,1))
ex2 = np.random.randint(0,10,size=(5,4))
print(ex1)
print(ex2)
ex = np.concatenate([ex1,ex2],axis=1)
print(ex)
#特殊情况：axis=None的话，会将两个数组组合为一维数组

#3.数组的切割:将数组进行拆分(hsplit,vsplit，split)
'''
总结：
hsplit代表竖直的线去切割成多个列(其实就是将水平的数组切割左右)
vsplit代表水平的线去切割成多个行(其实就是将竖直的数据切割上下)
split可以自定义如何切割，axis=1是竖直的线去切割成列，axis=0是水平的线去切割成行
#注意，想自定义切割的列时传入元组指定那些列或行单独切割就行
'''
#hsplit：竖直的线去切割
print("-"*20)
ex1 = np.random.randint(0,10,size=(2,4))
print(ex1)
ex = np.hsplit(ex1,2) #注意需要能整除，能平均拆分
print(ex)

ex1 = np.random.randint(0,10,size=(4,4))
print(ex1)
ex = np.hsplit(ex1,(1,2)) #传入元组，切割出第一列，第二列，剩下的单独成数组，利用元组来更随性的切割
print(ex)

#vsplit：水平的线去切割
print("-"*20)
ex1 = np.random.randint(0,10,size=(4,4))
print(ex1)
ex = np.vsplit(ex1,2) #注意需要能整除，能平均拆分
print(ex)

ex1 = np.random.randint(0,10,size=(4,4))
print(ex1)
ex = np.vsplit(ex1,(1,2)) #传入元组，切割出第一行，第二行，剩下的单独成数组，利用元组来更随性的切割
print(ex)

#split来自定义切割方式，axis=1是竖直线来切割成多个列，axis=0是水平线来切割成多个行
print("-"*20)
ex1 = np.random.randint(0,10,size=(2,4))
print(ex1)
ex = np.split(ex1,2,axis=1)
print(ex)

ex1 = np.random.randint(0,10,size=(4,4))
print(ex1)
ex = np.split(ex1,(1,2),axis=1)
print(ex)

print("-"*20)
ex1 = np.random.randint(0,10,size=(4,4))
print(ex1)
ex = np.split(ex1,2,axis=0)
print(ex)

ex1 = np.random.randint(0,10,size=(4,4))
print(ex1)
ex = np.split(ex1,(1,2),axis=0)
print(ex)

#4.数组的转置和轴对换
#转置
print("-"*20)
ex1 = np.random.randint(0,10,size=(3,4))
ex = ex1.T #将数组进行转置
print(ex)

ex = ex1.transpose()
print(ex)

print(ex1.dot(ex1.T)) #将ex1和转置后的ex1进行矩阵相乘
```

### 8.浅拷贝和深拷贝

```python
#浅拷贝和深拷贝
import numpy as np

'''
总结： 表-->栈区----深-->堆区(内存)
直接赋值:栈区无拷贝，堆区无拷贝
浅拷贝:栈区有拷贝，堆区无拷贝，所以拷贝后的数组被修改原数组也会被修改，因为他俩都指向内存中的同一位置
深拷贝：栈区有拷贝，堆区有拷贝，--> 真正的拷贝，拷贝之后的数组和原数组一毛钱的关系都没了，随意造它...
'''

#注意点:
a = np.arange(12)
b = a
print(b is a) #返回True证明没拷贝，还是栈区中的同一位置

#浅拷贝:指向的其实是没变的(指针)拷贝之后修改，也会修改掉原...
c = a.view() #视图：调用view来浅拷贝
#print(c is a) #False证明不再栈区的同一位置
print(c)
c[0] = 100 #会对原数组进行修改，因为这个浅拷贝是在栈区拷贝一份新的，但是新的和旧的都指向堆区(内存)的那个数组，所以改这俩任意一个均会改变内存中的数组，因为他俩还是指向内存的同一位置
print(a)

#深拷贝:不仅会在栈区拷贝一份，而且还会在内存中也拷贝一份，并且他俩分别指向自己对应的内存中的位置
d = a.copy()
#print(d is a) #False证明不在栈区的同一位置
d[1] = 200
print('d:'+str(d))
print('a:'+str(a)) #结果是d修改来第二个，而a没被修改第二个，证明在堆区(内存)也拷贝了一份

'''
例如前面学的flatten和ravel，ravel返回的就是view，而flatten返回的就是深拷贝，所以view视图以后看到后要知道它是浅拷贝哟！
'''
```

### 9.文件操作

```python
#csv文件操作
import numpy as np

#文件保存
scroes = np.random.randint(0,100,size=(20,2))
#参数依次是文件名，数组，写入文件的格式，分割字符串，默认是空格，header为标题，根据分割符来划分,comments加上之后#就没了
np.savetxt('scroes.csv',scroes,fmt='%d',delimiter=',',header="英语,数学",comments='')

#读取文件
'''
np.loadtxt(fname,dtype=np.float,delimiter=None,unpack=False)
fname-文件名
dtype-数据类型
delimiter-分割字符串，默认是空格
skiprows-跳过前面x行
usecols-读取指定的列，用元组组合
unpack-如果为True，读取出来的数组是转置后的
'''
scroes = np.loadtxt("scroes.csv",dtype=np.int64,delimiter=',',skiprows=1)
print(scroes)

#np独有的存储解决方案（np.save(fname,array),np.load(fname)）
'''
前面的存储和读取最多就二维数组
np独有的存储和读取方案则可以存取多维数组
'''
#存储(有save和savez两种方法，前者后缀为npy，后者为npz，后者经过压缩)
numbers = np.random.randint(0,100,size=(20,2))
np.save("numbers",numbers) #自动加后缀的

#读取
numbers = np.load("numbers.npy")
print(numbers)
```

### 10.NAN和NF

```python
#NAN和INF的认识
import numpy as np

'''
NAN:Not a number,不是一个数字的意思,但是它是属于浮点类型的
INF:Infinity,代表无穷大的意思,也属于浮点类型,一般在分母为零时出现
'''

data = np.random.randint(0,10,size=(3,5))
print(data)
data = data.astype(np.float64)
data[0,1] = np.NAN #将那个元素替换为nan(注意这个nan是浮点数类型)
print(data)
print(data/0) #无穷大的就会变为inf，nan和任何数运算还是为nan

#处理缺失值

#删除缺失值
'''
利用np.isnan()来判断数组中是否有nan
'''
#1.直接删除数组中所有的nan(不推荐，局限性大，而且还会使数组最终变成一维数组，只在某些时候可以使用)
data = np.random.randint(0,10,size=(3,5))
data = data.astype(np.float64)
data[0,1] = np.NAN
print(data[~np.isnan(data)]) #取反符号

#2.删除nan所在的行
data = np.random.randint(0,10,size=(3,5)).astype(np.float)
#将这两个地方设置成nan
data[[0,1],[1,2]] = np.NAN
#获取那些行有nan
lines = np.where(np.isnan(data))[0]
#使用delete方法删除指定的行，axis=0表示删除行，lines表示删除的行号
data1 = np.delete(data,lines,axis=0)


#用其他值进行替换
'''
实例操作
'''
scores = np.loadtxt("nan_scroes.csv",delimiter=',',skiprows=1,dtype=np.str) #为了解决读取空白字符时的报错，先dtype为str
print(scores)
#将空白字符转换为nan
scores[scores == ''] = np.NAN #注意：所有数字都时两位数时被替换进的是na不是nan
print(scores)
#转换为浮点类型（nan为浮点类型，所以能转，不会报错）
scores = scores.astype(np.float)
print(scores)
#将nan替换为零
scores[np.isnan(scores)] = 0
print(scores)
print(sum(scores)) #求每一列总成绩
print(scores.sum())#求全部总成绩
print(scores.sum(axis=1)) #求每一行的总成绩
print(scores.sum(axis=0)) #求每一列的总成绩
```

### 11.迭代数组

```python
#迭代数组
import numpy as np
'''
在numpy中可以使用nditer来灵活访问一个或者多个数组元素
'''
#迭代输出数组元素
ex = np.arange(6).reshape(2,3)
print('原数组是：')
print(ex)
print('迭代输出元素：')
for x in np.nditer(ex):
    print(x,end=',')
print('\n')

#控制遍历顺序
'''
for x in np.nditer(ex,order='F'):Fortran order->列许优先
for x in np.nditer(ex,order='C'):C order->行序优先
'''
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('原始数组是：')
print(a)
print('\n')
print('以 C 风格顺序排序：')
for x in np.nditer(a, order =  'C'):
    print(x, end=", " )
print('\n')
print('以 F 风格顺序排序：')
for x in np.nditer(a, order =  'F'):
    print(x, end=", " )

#修改数组中元素的值
'''
nditer 对象有另一个可选参数 op_flags。 
默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），
为了在遍历数组的同时，实现对数组元素值得修改，
必须指定 read-write 或者 write-only 的模式
'''
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('\n\n原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=2*x
print('修改后的数组是：')
print(a)

#使用外部循环
'''
nditer 类的构造器拥有 flags 参数，它可以接受下列值：
参数	            描述
c_index	        可以跟踪 C 顺序的索引
f_index	        可以跟踪 Fortran 顺序的索引
multi_index	    每次迭代可以跟踪一种索引类型
external_loop	给出的值是具有多个值的一维数组，而不是零维数组
在下面的实例中，迭代器遍历对应于每列，并组合为一维数组
'''
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('原始数组是：')
print(a)
print('\n')
print('修改后的数组是：')
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print (x, end=", " )
print('\n')
#广播迭代
'''
如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。 
假设数组a的维度为3X4，数组b的维度为1X4，则使用以下迭代器（数组b被广播到a的大小）。
'''
a = np.arange(0,60,5)
a = a.reshape(3,4)
print('第一个数组为：')
print(a)
print('\n')
print('第二个数组为：')
b = np.array([1,  2,  3,  4], dtype = int)
print(b)
print('\n')
print('修改后的数组为：')
for x,y in np.nditer([a,b]):
    print("%d:%d"%(x,y), end=", " )
```

### 12.字符串函数

```python
#字符串函数
import numpy as np
'''
函数	描述
add()	      对两个数组的逐个字符串元素进行连接
multiply()	  返回按元素多重连接后的字符串
center()	  居中字符串
capitalize()  将字符串第一个字母转换为大写
title()	      将字符串的每个单词的第一个字母转换为大写
lower()	      数组元素转换为小写
upper()	      数组元素转换为大写
split()	      指定分隔符对字符串进行分割，并返回数组列表
splitlines()  返回元素中的行列表，以换行符分割
strip()	      移除元素开头或者结尾处的特定字符
join()	      通过指定分隔符来连接数组中的元素
replace()	  使用新字符串替换字符串中的所有子字符串
decode()	  数组元素依次调用str.decode
encode()	  数组元素依次调用str.encode
'''
#np.char.add()函数一次对两个数组的元素进行字符串拼接
print('连接两个字符串：')
print(np.char.add(['hello'], [' xyz']))
print('\n')

print('连接示例：')
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))

#numpy.char.multiply() 函数执行多重连接
print (np.char.multiply('Runoob ',3))

#numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充
# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print (np.char.center('Runoob', 20,fillchar = '*'))

#numpy.char.capitalize() 函数将字符串的第一个字母转换为大写
print (np.char.capitalize('runoob'))

#numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写
print (np.char.title('i like runoob'))

#numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower
# 操作数组
print(np.char.lower(['RUNOOB', 'GOOGLE']))
# 操作字符串
print(np.char.lower('RUNOOB'))

#numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper
# 操作数组
print(np.char.upper(['runoob', 'google']))
# 操作字符串
print(np.char.upper('runoob'))

#numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格
# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))

#numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组
# 换行符 \n(\n，\r，\r\n 都可用作换行符)
print (np.char.splitlines('i\nlike runoob?'))
print (np.char.splitlines('i\rlike runoob?'))

#numpy.char.strip() 函数用于移除开头或结尾处的特定字符
# 移除字符串头尾的 a 字符
print(np.char.strip('ashok arunooba', 'a'))
# 移除数组元素头尾的 a 字符
print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))

#numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
# 操作字符串
print(np.char.join(':', 'runoob'))
# 指定多个分隔符操作数组元素
print(np.char.join([':', '-'], ['runoob', 'google']))

#numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串
print (np.char.replace ('i like runoob', 'oo', 'cc'))

#numpy.char.encode()函数对数组中的每个元素调用str.encode函数。
#默认编码是 utf-8，可以使用标准 Python 库中的编解码器
a = np.char.encode('runoob', 'cp500')
print (a)

#numpy.char.decode() 函数对编码的元素进行 str.decode() 解码
a = np.char.encode('runoob', 'cp500')
print (a)
print (np.char.decode(a,'cp500'))
```

### 13.数学函数

```python
'''
NumPy 数学函数
NumPy 包含大量的各种数学运算的函数，包括三角函数，算术运算的函数，复数处理函数等。
三角函数
NumPy 提供了标准的三角函数：sin()、cos()、tan()。
实例
import numpy as np

a = np.array([0,30,45,60,90])
print ('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print (np.sin(a*np.pi/180))
print ('\n')
print ('数组中角度的余弦值：')
print (np.cos(a*np.pi/180))
print ('\n')
print ('数组中角度的正切值：')
print (np.tan(a*np.pi/180))
输出结果为：
不同角度的正弦值：
[0.         0.5        0.70710678 0.8660254  1.        ]


数组中角度的余弦值：
[1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01
 6.12323400e-17]


数组中角度的正切值：
[0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00
 1.63312394e+16]
arcsin，arccos，和 arctan 函数返回给定角度的 sin，cos 和 tan 的反三角函数。
这些函数的结果可以通过 numpy.degrees() 函数将弧度转换为角度。
实例
import numpy as np

a = np.array([0,30,45,60,90])
print ('含有正弦值的数组：')
sin = np.sin(a*np.pi/180)
print (sin)
print ('\n')
print ('计算角度的反正弦，返回值以弧度为单位：')
inv = np.arcsin(sin)
print (inv)
print ('\n')
print ('通过转化为角度制来检查结果：')
print (np.degrees(inv))
print ('\n')
print ('arccos 和 arctan 函数行为类似：')
cos = np.cos(a*np.pi/180)
print (cos)
print ('\n')
print ('反余弦：')
inv = np.arccos(cos)
print (inv)
print ('\n')
print ('角度制单位：')
print (np.degrees(inv))
print ('\n')
print ('tan 函数：')
tan = np.tan(a*np.pi/180)
print (tan)
print ('\n')
print ('反正切：')
inv = np.arctan(tan)
print (inv)
print ('\n')
print ('角度制单位：')
print (np.degrees(inv))
输出结果为：
含有正弦值的数组：
[0.         0.5        0.70710678 0.8660254  1.        ]


计算角度的反正弦，返回值以弧度为单位：
[0.         0.52359878 0.78539816 1.04719755 1.57079633]


通过转化为角度制来检查结果：
[ 0. 30. 45. 60. 90.]


arccos 和 arctan 函数行为类似：
[1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01
 6.12323400e-17]


反余弦：
[0.         0.52359878 0.78539816 1.04719755 1.57079633]


角度制单位：
[ 0. 30. 45. 60. 90.]


tan 函数：
[0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00
 1.63312394e+16]


反正切：
[0.         0.52359878 0.78539816 1.04719755 1.57079633]


角度制单位：
[ 0. 30. 45. 60. 90.]
舍入函数
numpy.around() 函数返回指定数字的四舍五入值。
numpy.around(a,decimals)
参数说明：
a: 数组
decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
实例
import numpy as np

a = np.array([1.0,5.55,  123,  0.567,  25.532])
print  ('原数组：')
print (a)
print ('\n')
print ('舍入后：')
print (np.around(a))
print (np.around(a, decimals =  1))
print (np.around(a, decimals =  -1))
输出结果为：
原数组：
[  1.      5.55  123.      0.567  25.532]


舍入后：
[  1.   6. 123.   1.  26.]
[  1.    5.6 123.    0.6  25.5]
[  0.  10. 120.   0.  30.]
numpy.floor()
numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整。
实例
import numpy as np

a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print ('提供的数组：')
print (a)
print ('\n')
print ('修改后的数组：')
print (np.floor(a))
输出结果为：
提供的数组：
[-1.7  1.5 -0.2  0.6 10. ]


修改后的数组：
[-2.  1. -1.  0. 10.]
numpy.ceil()
numpy.ceil() 返回大于或者等于指定表达式的最小整数，即向上取整。
实例
import numpy as np

a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print  ('提供的数组：')
print (a)
print ('\n')
print ('修改后的数组：')
print (np.ceil(a))
输出结果为：
提供的数组：
[-1.7  1.5 -0.2  0.6 10. ]


修改后的数组：
[-1.  2. -0.  1. 10.]
'''
```

### 14.算术函数

```python
'''
NumPy 算术函数
NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。
需要注意的是数组必须具有相同的形状或符合数组广播规则。
实例
import numpy as np

a = np.arange(9, dtype = np.float_).reshape(3,3)
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
b = np.array([10,10,10])
print (b)
print ('\n')
print ('两个数组相加：')
print (np.add(a,b))
print ('\n')
print ('两个数组相减：')
print (np.subtract(a,b))
print ('\n')
print ('两个数组相乘：')
print (np.multiply(a,b))
print ('\n')
print ('两个数组相除：')
print (np.divide(a,b))
输出结果为：
第一个数组：
[[0. 1. 2.]
 [3. 4. 5.]
 [6. 7. 8.]]

第二个数组：
[10 10 10]

两个数组相加：
[[10. 11. 12.]
 [13. 14. 15.]
 [16. 17. 18.]]

两个数组相减：
[[-10.  -9.  -8.]
 [ -7.  -6.  -5.]
 [ -4.  -3.  -2.]]

两个数组相乘：
[[ 0. 10. 20.]
 [30. 40. 50.]
 [60. 70. 80.]]

两个数组相除：
[[0.  0.1 0.2]
 [0.3 0.4 0.5]
 [0.6 0.7 0.8]]
此外 Numpy 也包含了其他重要的算术函数。
numpy.reciprocal()
numpy.reciprocal() 函数返回参数逐元素的倒数。如 1/4 倒数为 4/1。
实例
import numpy as np

a = np.array([0.25,  1.33,  1,  100])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 reciprocal 函数：')
print (np.reciprocal(a))
输出结果为：
我们的数组是：
[  0.25   1.33   1.   100.  ]

调用 reciprocal 函数：
[4.        0.7518797 1.        0.01     ]
numpy.power()
numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
实例
import numpy as np

a = np.array([10,100,1000])
print ('我们的数组是；')
print (a)
print ('\n')
print ('调用 power 函数：')
print (np.power(a,2))
print ('\n')
print ('第二个数组：')
b = np.array([1,2,3])
print (b)
print ('\n')
print ('再次调用 power 函数：')
print (np.power(a,b))
输出结果为：
我们的数组是；
[  10  100 1000]

调用 power 函数：
[    100   10000 1000000]

第二个数组：
[1 2 3]

再次调用 power 函数：
[        10      10000 1000000000]
numpy.mod()
numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果。
实例
import numpy as np

a = np.array([10,20,30])
b = np.array([3,5,7])
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
print (b)
print ('\n')
print ('调用 mod() 函数：')
print (np.mod(a,b))
print ('\n')
print ('调用 remainder() 函数：')
print (np.remainder(a,b))
输出结果为：
第一个数组：
[10 20 30]

第二个数组：
[3 5 7]

调用 mod() 函数：
[1 0 2]

调用 remainder() 函数：
[1 0 2]
'''
```

### 15.统计函数

```python
'''
NumPy 统计函数
NumPy 提供了很多统计函数，用于从数组中查找最小元素，最大元素，百分位标准差和方差等。 函数说明如下：
numpy.amin() 和 numpy.amax()
numpy.amin() 用于计算数组中的元素沿指定轴的最小值。
numpy.amax() 用于计算数组中的元素沿指定轴的最大值。
实例
import numpy as np

a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 amin() 函数：')
print (np.amin(a,1))
print ('\n')
print ('再次调用 amin() 函数：')
print (np.amin(a,0))
print ('\n')
print ('调用 amax() 函数：')
print (np.amax(a))
print ('\n')
print ('再次调用 amax() 函数：')
print (np.amax(a, axis =  0))
输出结果为：
我们的数组是：
[[3 7 5]
 [8 4 3]
 [2 4 9]]


调用 amin() 函数：
[3 3 2]


再次调用 amin() 函数：
[2 4 3]


调用 amax() 函数：
9


再次调用 amax() 函数：
[8 7 9]
numpy.ptp()
numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）。
实例
import numpy as np

a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 ptp() 函数：')
print (np.ptp(a))
print ('\n')
print ('沿轴 1 调用 ptp() 函数：')
print (np.ptp(a, axis =  1))
print ('\n')
print ('沿轴 0 调用 ptp() 函数：')
print (np.ptp(a, axis =  0))
输出结果为：
我们的数组是：
[[3 7 5]
 [8 4 3]
 [2 4 9]]


调用 ptp() 函数：
7


沿轴 1 调用 ptp() 函数：
[4 5 7]


沿轴 0 调用 ptp() 函数：
[6 3 6]
numpy.percentile()
百分位数是统计中使用的度量，表示小于这个值的观察值的百分比。 函数numpy.percentile()接受以下参数。
numpy.percentile(a, q, axis)
参数说明：
a: 输入数组
q: 要计算的百分位数，在 0 ~ 100 之间
axis: 沿着它计算百分位数的轴
首先明确百分位数：
第 p 个百分位数是这样一个值，它使得至少有 p% 的数据项小于或等于这个值，且至少有 (100-p)% 的数据项大于或等于这个值。
举个例子：高等院校的入学考试成绩经常以百分位数的形式报告。比如，假设某个考生在入学考试中的语文部分的原始分数为 54 分。相对于参加同一考试的其他学生来说，他的成绩如何并不容易知道。但是如果原始分数54分恰好对应的是第70百分位数，我们就能知道大约70%的学生的考分比他低，而约30%的学生考分比他高。
这里的 p = 70。
实例
import numpy as np

a = np.array([[10, 7, 4], [3, 2, 1]])
print ('我们的数组是：')
print (a)

print ('调用 percentile() 函数：')
# 50% 的分位数，就是 a 里排序之后的中位数
print (np.percentile(a, 50))

# axis 为 0，在纵列上求
print (np.percentile(a, 50, axis=0))

# axis 为 1，在横行上求
print (np.percentile(a, 50, axis=1))

# 保持维度不变
print (np.percentile(a, 50, axis=1, keepdims=True))
输出结果为：
我们的数组是：
[[10  7  4]
 [ 3  2  1]]
调用 percentile() 函数：
3.5
[6.5 4.5 2.5]
[7. 2.]
[[7.]
 [2.]]
numpy.median()
numpy.median() 函数用于计算数组 a 中元素的中位数（中值）
实例
import numpy as np

a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 median() 函数：')
print (np.median(a))
print ('\n')
print ('沿轴 0 调用 median() 函数：')
print (np.median(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 median() 函数：')
print (np.median(a, axis =  1))
输出结果为：
我们的数组是：
[[30 65 70]
 [80 95 10]
 [50 90 60]]


调用 median() 函数：
65.0


沿轴 0 调用 median() 函数：
[50. 90. 60.]


沿轴 1 调用 median() 函数：
[65. 80. 60.]
numpy.mean()
numpy.mean() 函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算。
算术平均值是沿轴的元素的总和除以元素的数量。
实例
import numpy as np

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 mean() 函数：')
print (np.mean(a))
print ('\n')
print ('沿轴 0 调用 mean() 函数：')
print (np.mean(a, axis =  0))
print ('\n')
print ('沿轴 1 调用 mean() 函数：')
print (np.mean(a, axis =  1))
输出结果为：
我们的数组是：
[[1 2 3]
 [3 4 5]
 [4 5 6]]


调用 mean() 函数：
3.6666666666666665


沿轴 0 调用 mean() 函数：
[2.66666667 3.66666667 4.66666667]


沿轴 1 调用 mean() 函数：
[2. 4. 5.]
numpy.average()
numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。
该函数可以接受一个轴参数。 如果没有指定轴，则数组会被展开。
加权平均值即将各数值乘以相应的权数，然后加总求和得到总体值，再除以总的单位数。
考虑数组[1,2,3,4]和相应的权重[4,3,2,1]，通过将相应元素的乘积相加，并将和除以权重的和，来计算加权平均值。
加权平均值 = (1*4+2*3+3*2+4*1)/(4+3+2+1)
实例
import numpy as np

a = np.array([1,2,3,4])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 average() 函数：')
print (np.average(a))
print ('\n')
# 不指定权重时相当于 mean 函数
wts = np.array([4,3,2,1])
print ('再次调用 average() 函数：')
print (np.average(a,weights = wts))
print ('\n')
# 如果 returned 参数设为 true，则返回权重的和
print ('权重的和：')
print (np.average([1,2,3,  4],weights =  [4,3,2,1], returned =  True))
输出结果为：
我们的数组是：
[1 2 3 4]


调用 average() 函数：
2.5


再次调用 average() 函数：
2.0


权重的和：
(2.0, 10.0)
在多维数组中，可以指定用于计算的轴。
实例
import numpy as np

a = np.arange(6).reshape(3,2)
print ('我们的数组是：')
print (a)
print ('\n')
print ('修改后的数组：')
wt = np.array([3,5])
print (np.average(a, axis =  1, weights = wt))
print ('\n')
print ('修改后的数组：')
print (np.average(a, axis =  1, weights = wt, returned =  True))
输出结果为：
我们的数组是：
[[0 1]
 [2 3]
 [4 5]]


修改后的数组：
[0.625 2.625 4.625]


修改后的数组：
(array([0.625, 2.625, 4.625]), array([8., 8., 8.]))
标准差
标准差是一组数据平均值分散程度的一种度量。
标准差是方差的算术平方根。
标准差公式如下：
std = sqrt(mean((x - x.mean())**2))
如果数组是 [1，2，3，4]，则其平均值为 2.5。 因此，差的平方是 [2.25,0.25,0.25,2.25]，并且再求其平均值的平方根除以 4，即 sqrt(5/4) ，结果为 1.1180339887498949。
实例
import numpy as np

print (np.std([1,2,3,4]))
输出结果为：
1.1180339887498949
方差
统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数，即 mean((x - x.mean())** 2)。
换句话说，标准差是方差的平方根。
实例
import numpy as np

print (np.var([1,2,3,4]))
输出结果为：
1.25
'''
```

### 16.排序-条件筛选函数

```python
#排序-条件刷选函数
import numpy as np
'''
NumPy 提供了多种排序的方法。 这些排序函数实现不同的排序算法，每个排序算法的特征在于执行速度，最坏情况性能，所需的工作空间和算法的稳定性。 下表显示了三种排序算法的比较。
种类	                    速度	   最坏情况	        工作空间	  稳定性
'quicksort'（快速排序）	1	   O(n^2)	        0	      否
'mergesort'（归并排序）	2	   O(n*log(n))	    ~n/2	  是
'heapsort'（堆排序）	    3	   O(n*log(n))	    0	      否

numpy.sort()
numpy.sort() 函数返回输入数组的排序副本。函数格式如下：
numpy.sort(a, axis, kind, order)
参数说明：
a: 要排序的数组
axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序， axis=0 按列排序，axis=1 按行排序
kind: 默认为'quicksort'（快速排序）
order: 如果数组包含字段，则是要排序的字段
'''
a = np.array([[3,7],[9,1]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 sort() 函数：')
print (np.sort(a))
print ('\n')
print ('按列排序：')
print (np.sort(a, axis = 0))
print ('\n')
# 在 sort 函数中排序字段
dt = np.dtype([('name',  'S10'),('age',  int)])
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)
print ('我们的数组是：')
print (a)
print ('\n')
print ('按 name 排序：')
print (np.sort(a, order =  'name'))

#numpy.argsort() 函数返回的是数组值从小到大的索引值
x = np.array([3,  1,  2])
print ('我们的数组是：')
print (x)
print ('\n')
print ('对 x 调用 argsort() 函数：')
y = np.argsort(x)
print (y)
print ('\n')
print ('以排序后的顺序重构原数组：')
print (x[y])
print ('\n')
print ('使用循环重构原数组：')
for i in y:
    print (x[i], end=" ")

#numpy.argmax() 和 numpy.argmin()函数分别沿给定轴返回最大和最小元素的索引。
a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print  ('我们的数组是：')
print (a)
print ('\n')
print ('调用 argmax() 函数：')
print (np.argmax(a))
print ('\n')
print ('展开数组：')
print (a.flatten())
print ('\n')
print ('沿轴 0 的最大值索引：')
maxindex = np.argmax(a, axis =  0)
print (maxindex)
print ('\n')
print ('沿轴 1 的最大值索引：')
maxindex = np.argmax(a, axis =  1)
print (maxindex)
print ('\n')
print ('调用 argmin() 函数：')
minindex = np.argmin(a)
print (minindex)
print ('\n')
print ('展开数组中的最小值：')
print (a.flatten()[minindex])
print ('\n')
print ('沿轴 0 的最小值索引：')
minindex = np.argmin(a, axis =  0)
print (minindex)
print ('\n')
print ('沿轴 1 的最小值索引：')
minindex = np.argmin(a, axis =  1)
print (minindex)

#numpy.nonzero() 函数返回输入数组中非零元素的索引。
a = np.array([[30,40,0],[0,20,10],[50,0,60]])
print ('我们的数组是：')
print (a)
print ('\n')
print ('调用 nonzero() 函数：')
print (np.nonzero (a))

#numpy.where() 函数返回输入数组中满足给定条件的元素的索引。
x = np.arange(9.).reshape(3,  3)
print ('我们的数组是：')
print (x)
print ( '大于 3 的元素的索引：')
y = np.where(x >  3)
print (y)
print ('使用这些索引来获取满足条件的元素：')
print (x[y])

#numpy.extract() 函数根据某个条件从数组中抽取元素，返回满条件的元素
x = np.arange(9.).reshape(3,  3)
print ('我们的数组是：')
print (x)
# 定义条件, 选择偶数元素
condition = np.mod(x,2)  ==  0
print ('按元素的条件值：')
print (condition)
print ('使用条件提取元素：')
print (np.extract(condition, x))
```

### 16.矩阵库

```python
'''
NumPy 矩阵库(Matrix)
NumPy 中包含了一个矩阵库 numpy.matlib，该模块中的函数返回的是一个矩阵，而不是 ndarray 对象。
一个 的矩阵是一个由行（row）列（column）元素排列成的矩形阵列。
矩阵里的元素可以是数字、符号或数学式。以下是一个由 6 个数字元素构成的 2 行 3 列的矩阵：

转置矩阵
NumPy 中除了可以使用 numpy.transpose 函数来对换数组的维度，还可以使用 T 属性。。
例如有个 m 行 n 列的矩阵，使用 t() 函数就能转换为 n 行 m 列的矩阵。



实例
import numpy as np

a = np.arange(12).reshape(3,4)

print ('原数组：')
print (a)
print ('\n')

print ('转置数组：')
print (a.T)
输出结果如下：
原数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]


转置数组：
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
matlib.empty()
matlib.empty() 函数返回一个新的矩阵，语法格式为：
numpy.matlib.empty(shape, dtype, order)
参数说明：
shape: 定义新矩阵形状的整数或整数元组
Dtype: 可选，数据类型
order: C（行序优先） 或者 F（列序优先）
实例
import numpy.matlib
import numpy as np

print (np.matlib.empty((2,2)))
# 填充为随机数据
输出结果为：
[[-1.49166815e-154 -1.49166815e-154]
 [ 2.17371491e-313  2.52720790e-212]]
numpy.matlib.zeros()
numpy.matlib.zeros() 函数创建一个以 0 填充的矩阵。
实例
import numpy.matlib
import numpy as np

print (np.matlib.zeros((2,2)))
输出结果为：
[[0. 0.]
 [0. 0.]]
numpy.matlib.ones()
numpy.matlib.ones()函数创建一个以 1 填充的矩阵。
实例
import numpy.matlib
import numpy as np

print (np.matlib.ones((2,2)))
输出结果为：
[[1. 1.]
 [1. 1.]]
numpy.matlib.eye()
numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
numpy.matlib.eye(n, M,k, dtype)
参数说明：
n: 返回矩阵的行数
M: 返回矩阵的列数，默认为 n
k: 对角线的索引
dtype: 数据类型
实例
import numpy.matlib
import numpy as np

print (np.matlib.eye(n =  3, M =  4, k =  0, dtype =  float))
输出结果为：
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]]
numpy.matlib.identity()
numpy.matlib.identity() 函数返回给定大小的单位矩阵。
单位矩阵是个方阵，从左上角到右下角的对角线（称为主对角线）上的元素均为 1，除此以外全都为 0。

实例
import numpy.matlib
import numpy as np

# 大小为 5，类型位浮点型
print (np.matlib.identity(5, dtype =  float))
输出结果为：
[[ 1.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.]
 [ 0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  1.]]
numpy.matlib.rand()
numpy.matlib.rand() 函数创建一个给定大小的矩阵，数据是随机填充的。
实例
import numpy.matlib
import numpy as np

print (np.matlib.rand(3,3))
输出结果为：
[[0.23966718 0.16147628 0.14162   ]
 [0.28379085 0.59934741 0.62985825]
 [0.99527238 0.11137883 0.41105367]]
矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
实例
import numpy.matlib
import numpy as np

i = np.matrix('1,2;3,4')
print (i)
输出结果为：
[[1  2]
 [3  4]]
实例
import numpy.matlib
import numpy as np

j = np.asarray(i)
print (j)
输出结果为：
[[1  2]
 [3  4]]
实例
import numpy.matlib
import numpy as np

k = np.asmatrix (j)
print (k)
输出结果为：
[[1  2]
 [3  4]]
'''
```

### 17.线性代数

```python
'''
NumPy 线性代数
NumPy 提供了线性代数函数库 linalg，该库包含了线性代数所需的所有功能，可以看看下面的说明：
函数	描述
dot	两个数组的点积，即元素对应相乘。
vdot	两个向量的点积
inner	两个数组的内积
matmul	两个数组的矩阵积
determinant	数组的行列式
solve	求解线性矩阵方程
inv	计算矩阵的乘法逆矩阵
numpy.dot()
numpy.dot() 对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和(数学上称之为内积)；对于二维数组，计算的是两个数组的矩阵乘积；对于多维数组，它的通用计算公式如下，即结果数组中的每个元素都是：数组a的最后一维上的所有元素与数组b的倒数第二位上的所有元素的乘积和： dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])。
numpy.dot(a, b, out=None)
参数说明：
a : ndarray 数组
b : ndarray 数组
out : ndarray, 可选，用来保存dot()的计算结果
实例
import numpy.matlib
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.dot(a,b))
输出结果为：
[[37  40]
 [85  92]]
计算式为：
[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]
numpy.vdot()
numpy.vdot() 函数是两个向量的点积。 如果第一个参数是复数，那么它的共轭复数会用于计算。 如果参数是多维数组，它会被展开。
实例
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])

# vdot 将数组展开计算内积
print (np.vdot(a,b))
输出结果为：
130
计算式为：
1*11 + 2*12 + 3*13 + 4*14 = 130
numpy.inner()
numpy.inner() 函数返回一维数组的向量内积。对于更高的维度，它返回最后一个轴上的和的乘积。
实例
import numpy as np

print (np.inner(np.array([1,2,3]),np.array([0,1,0])))
# 等价于 1*0+2*1+3*0
输出结果为：
2
多维数组实例
import numpy as np
a = np.array([[1,2], [3,4]])

print ('数组 a：')
print (a)
b = np.array([[11, 12], [13, 14]])

print ('数组 b：')
print (b)

print ('内积：')
print (np.inner(a,b))
输出结果为：
数组 a：
[[1 2]
 [3 4]]
数组 b：
[[11 12]
 [13 14]]
内积：
[[35 41]
 [81 95]]
数组 a：
[[1 2]
 [3 4]]
数组 b：
[[11 12]
 [13 14]]
内积：
[[35 41]
 [81 95]]
内积计算式为：
1*11+2*12, 1*13+2*14
3*11+4*12, 3*13+4*14
numpy.matmul
numpy.matmul 函数返回两个数组的矩阵乘积。 虽然它返回二维数组的正常乘积，但如果任一参数的维数大于2，则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播。
另一方面，如果任一参数是一维数组，则通过在其维度上附加 1 来将其提升为矩阵，并在乘法之后被去除。
对于二维数组，它就是矩阵乘法：
实例
import numpy.matlib
import numpy as np

a = [[1,0],[0,1]]
b = [[4,1],[2,2]]
print (np.matmul(a,b))
输出结果为：
[[4  1]
 [2  2]]
二维和一维运算：
实例
import numpy.matlib
import numpy as np

a = [[1,0],[0,1]]
b = [1,2]
print (np.matmul(a,b))
print (np.matmul(b,a))
输出结果为：
[1  2]
[1  2]
维度大于二的数组 ：
实例
import numpy.matlib
import numpy as np

a = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print (np.matmul(a,b))
输出结果为：
[[[ 2  3]
  [ 6 11]]

 [[10 19]
  [14 27]]]
numpy.linalg.det()
numpy.linalg.det() 函数计算输入矩阵的行列式。
行列式在线性代数中是非常有用的值。 它从方阵的对角元素计算。 对于 2×2 矩阵，它是左上和右下元素的乘积与其他两个的乘积的差。
换句话说，对于矩阵[[a，b]，[c，d]]，行列式计算为 ad-bc。 较大的方阵被认为是 2×2 矩阵的组合。
实例
import numpy as np
a = np.array([[1,2], [3,4]])

print (np.linalg.det(a))
输出结果为：
-2.0
实例
import numpy as np

b = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
print (b)
print (np.linalg.det(b))
print (6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))
输出结果为：
[[ 6  1  1]
 [ 4 -2  5]
 [ 2  8  7]]
-306.0
-306
numpy.linalg.solve()
numpy.linalg.solve() 函数给出了矩阵形式的线性方程的解。
考虑以下线性方程：
x + y + z = 6

2y + 5z = -4

2x + 5y - z = 27
可以使用矩阵表示为：

如果矩阵成为A、X和B，方程变为：
AX = B

或

X = A^(-1)B
numpy.linalg.inv()
numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵。
逆矩阵（inverse matrix）：设A是数域上的一个n阶矩阵，若在相同数域上存在另一个n阶矩阵B，使得： AB=BA=E ，则我们称B是A的逆矩阵，而A则被称为可逆矩阵。注：E为单位矩阵。
实例
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.linalg.inv(x)
print (x)
print (y)
print (np.dot(x,y))
输出结果为：
[[1 2]
 [3 4]]
[[-2.   1. ]
 [ 1.5 -0.5]]
[[1.0000000e+00 0.0000000e+00]
 [8.8817842e-16 1.0000000e+00]]
现在创建一个矩阵A的逆矩阵:
实例
import numpy as np

a = np.array([[1,1,1],[0,2,5],[2,5,-1]])

print ('数组 a：')
print (a)
ainv = np.linalg.inv(a)

print ('a 的逆：')
print (ainv)

print ('矩阵 b：')
b = np.array([[6],[-4],[27]])
print (b)

print ('计算：A^(-1)B：')
x = np.linalg.solve(a,b)
print (x)
# 这就是线性方向 x = 5, y = 3, z = -2 的解
输出结果为：
数组 a：
[[ 1  1  1]
 [ 0  2  5]
 [ 2  5 -1]]
a 的逆：
[[ 1.28571429 -0.28571429 -0.14285714]
 [-0.47619048  0.14285714  0.23809524]
 [ 0.19047619  0.14285714 -0.0952381 ]]
矩阵 b：
[[ 6]
 [-4]
 [27]]
计算：A^(-1)B：
[[ 5.]
 [ 3.]
 [-2.]]
结果也可以使用以下函数获取：
x = np.dot(ainv,b)
'''
```

### 18.小试matplotlib

```python
#matplotlib
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()
'''
以上实例中，np.arange() 函数创建 x 轴上的值。y 轴上的对应值存储在另一个数组对象 y 中。
这些值使用 matplotlib 软件包的 pyplot 子模块的 plot() 函数绘制。图形由 show() 函数显示。
'''

'''
注意：matplotlib默认不支持中文，所以需要搞中文的时候记得去查文档
'''

#散点图
x = np.arange(1,11)
y =  2  * x +  5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob")
plt.show()

#绘制正弦波
# 计算正弦曲线上点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1)
y = np.sin(x)
plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, y)
plt.show()

#subplot() 函数允许你在同一图中绘制不同的东西
# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0,  3  * np.pi,  0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2,  1,  1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()

#pyplot 子模块提供 bar() 函数来生成条形图。
x =  [5,8,10]
y =  [12,16,6]
x2 =  [6,9,11]
y2 =  [6,15,7]
plt.bar(x, y, align =  'center')
plt.bar(x2, y2, color =  'g', align =  'center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

#numpy.histogram() 函数是数据的频率分布的图形表示。 水平尺寸相等的矩形对应于类间隔，称为 bin，变量 height 对应于频率。
#numpy.histogram()函数将输入数组和 bin 作为两个参数。 bin 数组中的连续元素用作每个 bin 的边界。
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
np.histogram(a,bins =  [0,20,40,60,80,100])
hist,bins = np.histogram(a,bins =  [0,20,40,60,80,100])
print (hist)
print (bins)

#Matplotlib 可以将直方图的数字表示转换为图形。
#pyplot 子模块的 plt() 函数将包含数据和 bin 数组的数组作为参数，并转换为直方图。
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a, bins =  [0,20,40,60,80,100])
plt.title("histogram")
plt.show()
```

### 19.小结

```python
'''
总结:
    数组的创建:
        np.array(),np.arrange(),np.random.ran...,np.zero(),np.full)...
    数组的数据类型:
        np.arry([...],dtype=...),np.dtype,np.asdtype(...)...
    维度及其改维度:
        np.ndim,np.shape,np.reshape,np.size,np.flatten(),np.itemssize...
    选取元素:
        ex[行,列] --> ex[起始行:终止行,起始列:终止列] --> ex[[行一,行二]] --> ex[起始行:终止行] --> ex[[对行],[对列]]
    布尔索引:
        ex < 5 --> ex[ex < 5] --> ex[(ex < 5 | ex > 10)] , ... = value , np.where(ex < value) --> np.where(ex < value,0,1)
    广播机制:
        将平时对单个数与单个数运算的维度转变为单个数与一群数和一群数和一群数维度,
        将一群数视为一个对象,对这个对象做的操作会被广播到每一个数
        而后一群数与一群数的运算也有它们的规则:
            同行同列:数全是对齐的,相对应的运算
            同行不同列(其一是一列)时:...
            同列不同行(其一是一行)时:...
        注:线性代数的运算需要使用矩阵库,而规则在线性代数课上有教
    浅拷贝和深拷贝:
        三个程度:b = a --> c = a.view() --> d = a.copy()
    文件操作:
        savetxt(),loadtxt(),load()
'''
```

## Pandas

......

## Matplotlib

......





