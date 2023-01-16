# Python笔记文档

## Python简介

Python是一门跨平台的计算机程序设计语言，最初用于编写脚本程序及科学计算。随着版本的更新，Python多被用于网站开发，数据分析，人工智能等领域。

我们一般使用程序设计语言去解决实际问题通常经历如下过程：

+ 提出问题
+ 确定数据结构
+ 确定算法
+ 编写程序
+ 调试程序
+ 编写使用说明文档等

----

##  变量与字符串

```
在讲变量之前要先明确"字符串"的概念:
print()函数会将括号里面的变量或字符串打印到屏幕上，在后面验证我们代码执行结果是否为我们预期目的有着重要作用
```

### 字符串

字符串就是一系列被双引号或单引号所包含的字符。

```python
print("I told that i will to be a'betrer man'")
print('I told that i will to be a "better man"')
```

### 注释及文档注释

```python
# 这就是一行注释 => 注释会被编译器或解释器略去，因此注释在代码中起到解释说明等作用

"""这是一行双引号文档注释"""
'''这是一行单引号文档注释'''

"""
这是第一行文档注释
这是第二行文档注释
......
这是第n行文档注释

文档注释经常在编写函数，类，项目的使用说明或其用处使用。

例如模块的文档字符串：
    第一行：介绍本模块等大致功能
    第二行为空
    第三行开始是本模块的详细介绍
使用 __doc__()
"""
```

### 变量的定义

```python
message = "hello world!"
print(message)
```

上述语句中定义了一个message变量，它储存着字符串hello world！

注意：变量名不需要加双引号，但在给变量赋值的时候右边的字符串需要双引号。

想修改变量时，只需要知道顺序结构，即在后面再重新赋值一个即可。

### 变量的命名

1.变量名只能含有字母，数字和下划线。

2.变量名中不能含有空格，但可以使用下划线来间隔单词。

3.不能将python中的关键字和函数名作为变量名。

4.变量名应该既简短又具有描述性。

5.慎用小写字母l和大写字母O，它们易被看成1和0.

### 初探方法

使用方法来修改字符串的大小写：

​	用**title()**,**upper()**,**lower()**三个方法来修改字符串的大小写

方法的使用：

```python
name = "hello,csdn！"
print(name.title())    # 首字母大写
print(name.upper())    # 全部字母大写
print(name.lower())    # 全部字母小写
```

让python对变量执行方法title()指定的操作.每个方法后面都跟着一对括号
这是因为方法通常需要额外的信息来完成其工作.这种信息是在括号内提供上述三个方法不需要额外的信息,因此括号是空的。

### 字符串的拼接

合并和拼接字符串

```python
first_name = "Hello"
last_name = "Csdn"
full_name = first_name + " " + last_name
print(full_name)

>>>Hello Csdn
```

**print()**亦可以使用逗号来表示打印多个字符或者变量

```python
print(full_name,"!","I want to make my python notes in here")

>>>Hello Csdn ！I want to make my python notes in here
```

### 格式操作

**\t**添加空白,**\n**换行

```python
print("adadadada")
print("\tadadadada")
print("adcdefg")
print("a\nb\nc\nd\ne\nf\ng")
```

**rstrip()**/**lstrip()**/**strip()**分别删除前面/后面/前后面的空白

```python
print(' write '.rstrip())
print(' write '.lstrip())
print(' write '.strip())
```

### format格式化

```python
for i in range(1, 10001):
	sentence = "说{}次，人生苦短，我学Python".format(i)
	print(sentence)
    
>>>说1次，人生苦短，我学Python
>>>说2次，人生苦短，我学Python
>>>说3次，人生苦短，我学Python
>>>说4次，人生苦短，我学Python
>>>......
>>>说10000次，人生苦短，我学Python
```

### format格式控制

```python
# {<参数序号> : <格式控制标记>}
# 六个可选择并组合字段 <填充> <对齐> <宽度> <,> <.精度> <类型>

x = "Python"
ex = "{0:30}".format(x)   # 使x字符串宽度为三十
print(ex)

ex = "{0:>30}".format(x)   # >表示右对齐 靠右排
print(ex)

ex = "{0:<30}".format(x)   # >表示左对齐 靠左排 默认
print(ex)

ex = "{0:^30}".format(x)   # ^表示居中对齐 向中靠拢
print(ex)

ex = "{0:*^30}".format(x)   # *为填充字符 此格式标记表示靠中字符串并填充*
print(ex)

ex = "{0:-^30}".format(x)   # -为填充字符 此格式标记表示靠中字符串并填充-
print(ex)

ex = "{0:-^30,}".format(123456789)   # ,表示千分位，此格式标记表示向中靠拢填充-并将数字千分位
print(ex)

ex = "{0:.3f}".format(12345.67890)   # .表示精度 此格式标记表示浮点数四舍五入到三位小数
print(ex)   # 输出浮点数：e/E-对应指数形式 f-对应浮点数形式 %-浮点数大百分形式

ex = "{0:.5}".format(x)   # .表示精度 此格式标记对于字符串则表示其最大长度为5
print(ex)

x = "不同输出格式可输出不同到形式{:d}例如这个十进制"
print(x.format(30))   # b-二进制 c-Unicode d-十进制 o-八进制 x/X-小/大写十六进制

"""
输出结果：
Python                        
                        Python
Python                        
            Python            
************Python************
------------Python------------
---------123,456,789----------
12345.679
Pytho
不同输出格式可输出不同到形式30例如这个十进制
"""
```

## 数字运算与输入

### 整数运算

```python
# 加法运算
three = 1+2
print(1+2)
print(three)

>>>3
>>>3

# 减法运算
print(3-2)

>>>1

# 乘法运算
print(2*3)

>>>6

# 除法运算
print(3/2)

>>>1.5

# 次方运算
print(3**2)
print(3**3)

>>>9
>>>27
```

### 浮点数

```python
print(0.1+0.1)
print(0.2+0.2)
print(2*0.1)
print(2*0.2)

>>>0.2
>>>0.4
>>>0.2
>>>0.4
```

### 计算精度问题

```python
print(0.1+0.2)
print(3*0.1)

>>>0.30000000000000004
>>>0.30000000000000004
```

### 乘法妙用

```python
# 一个字符串进行数乘会输出一个或多个它本身
print('-_-'*6)

>>>-_--_--_--_--_--_-
```

### 输入输出

在python中使用input()函数来让用户输入:

```python
age = input('请输入你的年龄:')
print(age)
```

—此时执行上述语句，终端显示"请输入你的年龄:",假如我输入了我的年龄20，则会自动赋值给age并由print()函数打印显示在我的屏幕上。但是当我拿变量age写如下代码时却报错了：

```python
age = input('请输入你的年龄:')
if age >= 18:
    print("你已经成年！")
else:
    print("你还未成年！")
```

执行这段代码会报错，会被提示类型错误。

即，**input()**函数接收了你输入的年龄。你以为你输入了数字，它就会储存为数字，可惜它会以字符形式来储存，而用字符形式是无法和18比较的。

因此在这里引入类型转换

```python
# print()函数的使用

print("待输出字符串或变量")

print(变量1, 变量2,..., 变量n)

print(1, 2, 3, sep="-")   # sep设置分隔符

print("Python", end="!")   # 设置其结尾输出，默认end为\n

print("{}".format(1))   # 用format格式化输出
```

### 类型转换

str(8)会将8转换成字符类型，int("8")将8转换成数字类型，eval("8")将字符串转化为表达式。

```python
# eval可以将字符串转换为表达式
age = eval(input('请输入你的年龄:'))  # 也可以用int()
if age >= 18:
    print("你已经成年！")
else:
    print("你还未成年！")
    
>>>请输入你的年龄:20
>>>你已经成年!
```

------

## Python数据类型

### 列表

列表属于**组合数据类型**，组合数据类型还包括**字符串**、**元组**、**字典**和**集合**。**字符串**也是最常用的基本数据类型之一，同时**字符串**、**列表**和**元组**又被称作**序列类型**。序列类型最显著的特点之一就是可以进行**索引**、**切片**，因此序列类型的元素是按顺序排好的。

#### 列表定义

列表由按特定顺序排列的元素组成。列表中的元素可以是任意类型，元素之间无任何关系，可以执行增加、删除，替换，查找等操作。列表无需预先定义大小。

在python中使用[]括起来一个个字符串/数字/...就表示为一个列表，将此列表赋值给一个变量，即此变量就指代此列表。

```python
list_str = ['元素1','元素2','元素3','元素4']
print(list_str)

>>>['元素1','元素2','元素3','元素4']

list_number = [1,2,3,4]
print(list_number)

>>>[1,2,3,4]
```

#### 数值列表

```python
list_number = list(range(1,5))
print(list_number)

>>>[1,2,3,4]
```

**range()**函数可以传入三个参数，分别为起始参数，终止参数，步长。

正如上述代码中所示，range(1,5)得到1，2，3，4，但不会得到5，这是需要记忆的点！

#### 访问元素

在python中访问列表中的元素非常简单，格式为 **列表名[索引]**。

注意：索引从0开始，遵守减一原则。

下面列举索引的所有使用姿势。

```python
list_str = ['元素1','元素2','元素3','元素4']
print(list_str[0])
print(list_str[1])
print(list_str[2])
print(list_str[3])

>>>元素1
>>>元素2
>>>元素3
>>>元素4
```

```python
list_str = ['元素1','元素2','元素3','元素4']
print(list_str[-1])
print(list_str[-2])
print(list_str[-3])
print(list_str[-4])

>>>元素4
>>>元素3
>>>元素2
>>>元素1
```

```python
# 列表切片
list_str = ['元素1','元素2','元素3','元素4']
print(list_str[:4]) # 切片
>>>['元素1', '元素2', '元素3', '元素4']
```

```python
list_str = ['元素1','元素2','元素3','元素4']
print(list_str[:]) # 值得一提的是，可以使用此方法来拷贝这个列表。
>>>['元素1', '元素2', '元素3', '元素4']
```

#### 添加元素

在python中添加元素只需使用**append()**，**insert()**即可！

```python
# 创建一个空列表
list = []
# 给列表添加元素
list.append(1)
list.append(2)
list.append(3)
list.append(4)
print(list)

>>>[1, 2, 3, 4]
```

通过上述代码可以发现，**append()**接收一个参数，并在每一次被调用时将此元素添加到列表的最后一位！

```python
# 创建一个空列表
list = []
# 给列表插入元素
list.insert(0,1) # 指定第一个元素插入1
list.insert(1,2) # 指定第二个元素插入2
list.insert(2,3) # 指定第三个元素插入3
list.insert(3,4) # 指定第四个元素插入4
print(list)

>>>[1, 2, 3, 4]
```

通过上述代码可以发现，**insert()**接收两个参数，一个是制定插入位置，另一个为插入的元素！

比如往一个非常多元素的列表中将一个元素插入到第一位，那么原本列表的第一位元素和后边的所有元素均后移一位！

#### 删除元素

在python中删除元素可以使用**del语句**，**remove()**方法，**pop()**方法。，它们各有千秋，看情况使用！

下面通过代码来直观的了解一下。

```python
list_str = ['元素1','元素2','元素3','元素4']
del list_str[0]    # 会删除列表中的第一个元素
print(list_str)

>>>['元素2','元素3','元素4']
```

**del**语句是通过，del关键字和指定的元素位置来删除元素的，格式为**del list[索引]**。

```python
list_str = ['元素1','元素2','元素3','元素4']
poped_list_str = list_str.pop() # 列表中的最后一个元素被删除,但是删除的元素会被赋予给poped_list_str
print(poped_list_str) # 输出被删除的最后一个元素
print(list_str) # 输出被删除最后一个元素之后的列表

>>>元素4
>>>['元素1','元素2','元素3']
```

**pop()**方法会删除列表的最后一个元素，格式为**list.pop()**。值得注意的是，使用pop()方法删除的元素可被复制给一个新的变量。

顾名思义pop弹出，因此给pop传入索引值可弹出指定索引的元素的值，只是此时的算法复杂度为O(n).

```python
list_str = ['元素1','元素2','元素3','元素4']
list_str.remove('元素4')
print(list_str)

>>>['元素1','元素2','元素3']
```

**remove()**方法的使用和pop相似，不同的是remove是通过传入元素名称来指定删除！

#### 其他方法

| 方法      | 作用                                               |
| --------- | -------------------------------------------------- |
| sort()    | 该方法对列表进行永久排序                           |
| sorted()  | 该方法对列表进行暂时性排序                         |
| reverse() | 该方法可以反转列表                                 |
| len()     | 该方法用来确定列表长度                             |
| min()     | 该方法用来确定数字列表中的最小值                   |
| max()     | 该方法用来确定数字列表中的最大值                   |
| sum()     | 该方法用来确定数字列表中的总和                     |
| list()    | 该方法用来将一个序列转化为列表                     |
| count()   | list.count(a)该方法用来统计a在list中出现的次数     |
| clear()   | list.clear()该方法用来清除列表中的元素             |
| extend()  | list.extend(seq)一次性在list末尾另一个序列的元素   |
| index()   | list.index(a, [start], [end])显示列表中a元素的索引 |
| copy()    | list.copy()对原列表复制，生成一个新列表            |

### 元组

#### 元组定义

列表是可修改的，动态的，但有时候需要创建一系列不可修改的元素，因此就有了元组。

元组最大的特点就是一旦定义便不可修改，要想修改只能重新定义！

元组看起来犹如列表，但使用圆括号而不是方括号来标识。

定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。

```python
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

>>>200
>>>50
```

```python
many = (100,100,100)
print(many[0])
print(many[1])
print(many[2])

>>>100
>>>100
>>>100
```

#### 元组特殊操作

```python
tup1 = (100, 200, 300)
print(id(tup1))   # 输出tup1的id

tup2 = (10, 20, 30)
print(id(tup2))   # 输出tup2的id

tup = tup1 + tup2
print(tup, id(tup))

del tup   # 删除tup

>>> 4349884672
>>> 4350961088
>>> (100, 200, 300, 10, 20, 30) 4349806528
```

#### 元组操作函数

| 函数        | 说明                   |
| ----------- | ---------------------- |
| len()函数   | 返回元组中元素的个数   |
| min()函数   | 返回元组中元素的最小值 |
| max()函数   | 返回元组中元素的最大值 |
| tuple()函数 | 将seq转换为一个元组    |

### 字典

字典也是一种可变的组合数据类型，与列表和元组的不同在于，字典上一种无序组合数据类型。字典通过键及其对应的值构成键值对来确定一个元素。键和值之间用冒号:分隔，每个键值对就是一个元素，且用逗号,分隔，整个字典包含在花括号{}内。

注意：在字典中，键不可重复，且只能是不可变的数据类型；值可以重复出现，且可以是任意数据类型。另外，字典是没有顺序的数据类型，所以在对字典进行输出操作时，出现的结果可能与创建时的顺序不一致。

#### 字典定义

字典是由一系列键值对组成。

```python
dict = {'键1':'值1','键2':'值2'}
```

#### 访问字典

```python
dict = {'键1':'值1','键2':'值2'}
print(dict['键1'])
print(dict['键2'])

>>>值1
>>>值2
```

访问值只需**字典名[键名]**即可。

#### 添加键值对

```python
human = {}
human['man'] = 'woman'
print(human)

>>>{'man':'woman'}
```

#### 修改字典值

```python
human = {'man':'woman'}
human['man'] = 'new_woman'
print(human)

>>>{'man':'new_woman'}
```

#### 删除键值对

```python
human = {'man':'woman'}
del human['man']
print(human)

>>>{}
```

#### 字典的函数

| 函数       | 说明                                         |
| ---------- | -------------------------------------------- |
| len(dict)  | 计算字典中元素的个数，也可以认为计算键的个数 |
| str(disc)  | 将字典转换为字符串                           |
| type(dict) | 返回参数的数据类型                           |

#### 字典的方法

| 方法      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| clear()   | 清空字典所有键值对                                           |
| copy()    | 复制当前字典                                                 |
| keys()    | 返回一个字典中的所有键                                       |
| values()  | 返回一个字典中的所有值                                       |
| items()   | 返回一个字典中的所有键值对（元组类型）                       |
| get()     | 如果指定键存在则返回相应的值，不存在返回default              |
| pop()     | 如果指定键存在则返回相应的值，并删除键值对，不存在返回default |
| popitem() | 随即返回并删除字典中的一个键值对                             |

### 集合

集合也是一种组合数据类型，可以包含0个、1个或多个元素，其中元素的存储时无序的，集合中不允许出现重复值。

#### 集合定义

集合（set）是一个无序的不重复元素序列。

可以使用大括号 **{ }** 或者 **set()** 函数创建集合。

特别注意：创建一个空集合必须用 **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典。

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # 去重功能

>>>{'orange', 'banana', 'pear', 'apple'}

print('orange' in basket)   # 判断orange是否在basket中

>>> True

print('crabgrass' in basket)

>>> False

# 集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(a)  

>>>{'a', 'r', 'b', 'c', 'd'}

print(a - b)                           # 集合a中包含而集合b中不包含的元素

>>>{'r', 'd', 'b'}

print(a | b)                           # 集合a或b中包含的所有元素

>>>{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

print(a & b)                           # 集合a和b中都包含了的元素

>>>{'a', 'c'}

print(a ^ b)                           # 不同时包含于a和b的元素

>>>{'r', 'd', 'b', 'm', 'z', 'l'}
```

#### 集合方法

| 方法           | 描述                     |
| :------------- | :----------------------- |
| add()/update() | 为集合添加元素           |
| clear()        | 移除集合中的所有元素     |
| copy()         | 拷贝一个集合             |
| difference()   | 返回多个集合的差集       |
| intersection() | 返回集合的交集           |
| union()        | 返回两个集合的并集       |
| remove()       | 移除指定元素             |
| pop()          | 随机移除元素             |
| in操作符       | 判断某个元素是否在集合中 |

-----

## 控制语句

### if语句

```python
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('你已经成年')
else:
    print('你还未成年')
```

此示例即为一个简单的if控制语句，当输入了你的年龄并且转换成整型赋值给age后，按顺序结构执行到if语句，此时判断语句会判断a是

否大于等于18，如果大于等于18则执行‘print(‘你已经成年’)’，忽略else语句，否则执行else语句。

### 条件测试

每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试.

根据条件测试的值为True还是False来决定是否执行if语句中的代码。

如果条件测试的值为True，Python就执行紧跟在if语句后面的代码，如果为False，则忽略

```python
car = 'lanbogini'
print(car == 'lanbogini')

>>>true
```

```python
car = 'lanbogini'
print(car != 'lanbogini')

>>>flase
```

```python
# 使用> < >= <=
age = int(input("请输入你的年龄："))
if age>= 18:
    print('you are a big boy!')
else:
    print('you are too small!')
```

```python
# and,or,not
age_0 = 22
age_1 = 18
age_0 >= 0 and age_1 >=21
   # 结果为false
age_1 = 22
age_0 >= 21 and age_1 >= 21
   # 结果为true
   # 也可以写成(age_0 >= 21 and (age_1 >= 21))

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 > 21
   # 结果为true
age_0 = 18 
age_0 >= 21 or age_1 >=21
   # 结果为false
```

```python
cars = ['lanbogini','maikailun','baoma','xuefulan']
print('lanbogini' in cars) 
print('jjjjjj' in cars)
   # 利用这种语法格式即可检查列表中是否存在我们想要的元素
    
>>>true
>>>false
```

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
   print(user.title() + ',you can post a respone if you wish.')
```

### 布尔表达式

布尔表达式是条件测试的别名，与条件表达式不一样的是，布尔表达式的结果要么为true要么为false

布尔表达式通常用来记录条件，如游戏是否在运行，或用户是否可以编辑网站的特定内容

在跟踪程序状态或程序中的重要的条件方面，布尔值提供了一中高效的方式

```python
game_active = True
can_edit = False
```

值得一提的是，列表空或不空亦可以作为条件。

```python
lists = []
if lists:
    for value in lists:
        print('your lists has a ',value)
else:
    print('the lists has not a value ')
    # 在这边，直接拿列表来当条件，如果列表为空则为false，列表不为空则为true
    # false则执行else，true则执行if
    
>>>the lists has not a value 
```

### if语句其他格式

```python
# if语句
# 理解条件测试后就可以编写if语句了
'''
格式if conditional_test:
        do something
'''

# if-else语句
'''
格式if conditional_test:
       do something
    else:
       do something
'''

# if-elif-else语句

'''
正常三段式时if-elif-else

测试多个条件时if-if-if-......

省略else的时候if-elif-elif-......-elif

不省略的时候if-elif-elif-......-else
'''
```

-----

## 循环

在python中有两种循环结构，即**for循环**与**while循环**！

### for循环

先说for循环，其基本结构为**for 元素 in 可迭代对象:**，则干嘛干嘛...

**可迭代对象:**简单来理解就是可以被循环的对象，例如**列表、字典、字符串、元组、集合、生成器等**

```python
for i in range(1,5):
	print(i)
    
>>>1
>>>2
>>>3
>>>4
```

**for循环**的使用就如上述所示，值得注意的是，在python中用锁进来区分条件执行区间，不像c语言那样用;或者{}来区分！

```python
# 列表
li = [1,2,3,4]
for i in li:
	print(i)
    
>>>1
>>>2
>>>3
>>>4
```

```python
# 字典
dic = {'num1':1,'num2':2,'num3':3}
for k,v in dic.items():
    print(k,v)
    
>>>num1 1
>>>num2 2
>>>num3 3
```

```python
dic = {'num1':1,'num2':2,'num3':3}
for k in dic.keys():
    print(k)
    
>>>num1
>>>num2
>>>num3
```

```python
dic = {'num1':1,'num2':2,'num3':3}
for v in dic.values():
    print(v)
    
>>>1
>>>2
>>>3
```

```python
# 字符串
for i in "abcd":
	print(i)
    
>>>a
>>>b
>>>c
>>>d
```

```python
# 元组
tur = (1,2,3,4)
for i in tur:
  print(i)

>>>1
>>>2
>>>3
>>>4
```

```python
# 集合
set = {1,2,3,4,4,4,4}
for i in set:
	print(i)
    
>>>1
>>>2
>>>3
>>>4
```

### 遍历技巧

```python
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
	print(k,v)
    
>>>0 tic
>>>1 tac
>>>2 toe
```

```python
# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
l = ['tic', 'tac', 'toe']
for i,v in enumerate(l):
  print(i,v)

>>>0 tic
>>>1 tac
>>>2 toe
```

```python
# 同时遍历两个或更多的序列，可以使用 zip() 组合
l1 = [1,2,3]
l2 = [4,5,6]
for a,b in zip(l1,l2):
	print(a,b)
    
>>>1 4
>>>2 5
>>>3 6
```

```python
# 列表解析式
li = [1,2,3,4]
new_li = [x**2 for x in li]
print(new_li)

>>>[1, 4, 9, 16]

# 复杂的列表解析式

```

### while循环

与for循环不一样的是**while循环**是在条件为真的时候会一直循环执行循环体内的语句！

因此非常重要的一点是在使用**while循环**时一定要设置好**循环退出条件**！

**while循环**的语法格式为：while 条件: ...

```python
li = [1,2,3,4]
while li:
	print(li)
    
>>>[1,2,3,4]
>>>[1,2,3,4]
>>>...
```

上述代码即为死循环，它会一直循环打印li列表！

```python
li = [1,2,3,4,]
while li:
	poped = li.pop()
	print("被删除元素:" + str(poped))
	print("列表:" + str(li))
    
>>>被删除元素:4
>>>列表:[1, 2, 3]
>>>被删除元素:3
>>>列表:[1, 2]
>>>被删除元素:2
>>>列表:[1]
>>>被删除元素:1
>>>列表:[]
```

上述代码就是一个好的循环，因为不断有元素被删除，直至到列表为空，循环条件为false，循环不在执行！

```python
active = True
while active:
    message = input('输入信息，我将返回给你，或者输入quit退出程序：')
    
    if message == 'quit':
        active = False
        print("你已经成功退出程序")
    else:
        print(message)
        
>>>输入信息，我将返回给你，或者输入quit退出程序：代码改变世界 艺术就是爆炸
>>>代码改变世界 艺术就是爆炸
>>>输入信息，我将返回给你，或者输入quit退出程序：quit
>>>你已经成功退出程序
```

**while循环**一个非常有用的应用，让用户把握退出的时机！

### break语句

**break**正如其名“打断”，再循环体内时我们在某些情况下不需要全循环完毕在退出循环，而是在某个条件成立的时候可以直接退出整个循环，**break**应运而生！

```python
while True:
    city = input('请输入你喜欢的城市名字，亦可以输入quit退出程序:')
    
    if city == 'quit':
        print('你已经成功退出程序')
        break
    else:
        print(city + "是一个非常美丽的城市")
        
>>>请输入你喜欢的城市名字，亦可以输入quit退出程序:厦门
>>>厦门是一个非常美丽的城市
>>>请输入你喜欢的城市名字，亦可以输入quit退出程序:quit
>>>你已经成功退出程序
```

### continue语句

在循环中使用continue：要返回到循环开头，并根据条件测试结果决定是否继续执行，可使用continue语句。

与break不同的是，continue是打断本次循环回到循环开头，在此判断循环条件看是否需要执行！

```python
# 例如用从一数到十，但只打印偶数的循环
current_number = 0
while current_number <10:
    current_number += 1
    current_numbers = current_number % 2
    if current_numbers == 0:
        print(current_number) 
        
>>>2
>>>4
>>>6
>>>8
>>>10
```

### pass语句

pass语句是用来占位置的，没有其他任何用处！

```python
def name():
	pass

def post():
	pass

li = []
if li:
	pass
else:
	pass
```

上述代码运行不会有任何东西输出，因为pass语句只是用来占位而没有任何其他作用！

### 循环嵌套

正如其名，在循环里面写循环，套娃之中在套娃！

```python
li = [1,2,3]
for i in li:
  for j in li:
    print(j)
  print(i)

>>>1
>>>2
>>>3
>>>1
>>>1
>>>2
>>>3
>>>2
>>>1
>>>2
>>>3
>>>3
```

其他的还可以for与while循环相互嵌套，while与while循环相互嵌套，函数与函数嵌套调用...

### 计数器

下面我介绍为在日常编程中常用的两种计数的方法。

```python
# 这个常规编程时常用
count = 0
for i in range(1,3):
	count = count + 1
	print("循环了{}次".format(count))
    
>>>循环了1次
>>>循环了2次
```

```python
# 使用迭代器-我主要在异步编程时使用
def creat_counter():
    def increace():
        n = 0   # 计数器起始值
        while True:
            n = n + 1
            yield n

    ic = increace()   # 注意这里并没有调用

    def counter():
        return next(ic)   # 这里调用increace并返回计数的值

    return counter   # 返回counter给creat_counter函数

counter_ = creat_counter()   # 将creat_counter函数内的counter赋值给counter_
for i in range(1, 3):
    count = counter_()    # counter_调用的实际就是creat_counter函数内的counter()
    print("循环了{}次".format(count))
    
>>>循环了1次
>>>循环了2次
```

解释一下大致运行流程:

首先定义了一个生成计数器函数，在这个函数里面又分别定义了两个函数，increace函数为生成器，主要作用为运行一次就给n+1并记住这个值，而后将increace函数实例化给ic，定义一个counter函数使用next来输出调用ic并得到n值，最后将counter函数return。

在使用时，首先实例化creat_counter函数给counter\_（实际上就是把counter给counter_），随后在循环体内调用counter\_函数，此时会执行creat_counter函数内的counter函数，counter函数会调用increace函数使n加一并记住这个值以待下次在此基础上继续加一，而后n会被return给counter，而counter又会被return给creat_counter，最后传给count变量指向n这个值，并最终被foumat函数将n的值添加给字符串，从而得到“循环了1次”，在下次循环时，不一样的是，当执行到了increace时，并不会按你看到的执行n=0，而是直接n为上次得到的值n=1的基础上进行加一......

要验证的话很简单，可在n=0的下一行添加print(n)，会发现n只会执行一次，按理来说应该执行两次的。而你在n = n + 1下一行添加print(n)则会执行两次分别为1，2。

----

## 函数

函数是用于执行特定操作的可复用代码块。函数可以在模块、类或其他函数内定义，在类内定义的函数称为方法。使用函数的优点如下：

+ 减少代码重复编写
+ 一个函数解决一个问题
+ 使代码逻辑更清晰
+ 提高代码的重用率

在Python中，函数可以复制给变量，存储在集合中或作为参数传递。函数分为两种基本类型：内置函数和用户定义函数。内置函数是Python语言解释器的一部分，例如：abs()、min()等，用户定义的函数是使用def保留字创建的函数。下面介绍Python函数。

### 函数定义

```
1.定义函数:使用关键字def来告诉python我要定义函数，然后写上函数名和括号，最后定义以冒号结尾
2.紧跟在缩进后的语句构成函数体，它们将实现函数具体功能
```

```python
def flag():
  '''实现简单的字符串输出'''
	print("代码改变世界 艺术就是爆炸")
    
flag()

>>>代码改变世界 艺术就是爆炸
```

上述代码就实现了一个简单的函数，这个函数的名字为flag，函数内写了一行输出字符串的代码，最后在函数外调用flag()。

注意一下那个三引号中间的注释，它将会在你调用函数时，预览在函数解释当中，它将在大量工作时发挥重要作用

### 函数传参

函数是可以传递参数的，通过在函数名后的括号内写上形参，而后在调用函数的时候传递实参！

**1.位置实参：其实就是按照定义形参的顺序一一对应要传递的实参**

```python
def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print('\n I have a ' , animal_type , '!')
    print('My ' , animal_type , "'s name is " , pet_name.title() , '.')

describe_pet('hamster','harry')    # 其中，hamster和harry分别对应储存在animal_type和pet_name中

>>>
>>>I have a  hamster !
>>>My  hamster 's name is  Harry .
```

**2.关键字实参：其实就是在调用的时候，直接指明形参1=实参1，形参2=实参2......**

```python
def describe_pet(animal_type,pet_name):
    '''显示宠物信息'''
    print('\n I have a ' , animal_type , '!')
    print('My ' , animal_type , "'s name is " , pet_name.title() , '.')

describe_pet(animal_type = 'hamster',pet_name = 'harry')

>>>
>>>I have a  hamster !
>>>My  hamster 's name is  Harry .
```

**3.默认值：其实就是在定义函数的时指定某个形参默认等于一个值，调用时如果没有给这个形参传递值，那么就使用默认值**

```python
def describe_pet(pet_name,animal_type = 'dog'):
    '''显示宠物信息'''
    print('\n I have a ' , animal_type , '!')
    print('My ' , animal_type , "'s name is " , pet_name.title() , '.')

describe_pet(pet_name = 'lixuexue') 

>>>
>>>I have a  dog !
>>>My  hamster 's name is  lixuexue .
```

**注意：默认值需要放置在后面**

**4.传递任意数量的实参：*形参**

```python
#在形参前面加个*号来表示将要传递一个或多个实参
def pri(*arrs):
	print(arrs)
print([1,2,3],[4,5,6],[7,8,9])

>>>([1, 2, 3], [4, 5, 6], [7, 8, 9])
'''
解释：
形参名*toppings中的星号让python创建了一个名为toppings的空元组，并将其收到的所有值都封装到这个元组中
函数体内的print语句通过生产输出来证明python能够处理使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形
它以类似的方式处理不同的调用，注意：python将实参封装到一个元组中，即便函数只收到一个值也是如此

将实参封装到元组中，日常生活中有了解过整体代换，应该亦是如此吧！

注意：如果有位置形参或关键字形参时，任意数量形参放置在最后，以便在接收了位置/关键字实参后在接收任意数量的实参！
'''
```

**5.传递任意数量的关键字实参：\*\*形参**

```python
def pri(**names):
  print(names)

pri(n1="lixue",n2="lilian")

>>>{'n1': 'lixue', 'n2': 'lilian'}
```

由此可知，**topping接收任意数量关键字实参并将这些值存储在一个字典里面！

```python
def name(fir_name,la_name,**names):
  dict_name = {}
  dict_name['fir_name'] = fir_name
  dict_name['la_name'] = la_name
  for k,v in names.items():
    dict_name[k] = v
  print(dict_name)

name('li','hong',n1='lixue',n2='lilian',n3='xiaolibai')

>>>{'fir_name': 'li', 'la_name': 'hong', 'n1': 'lixue', 'n2': 'lilian', 'n3': 'xiaolibai'}
```

### 函数返回值

在使用函数的时候我们总是会传入一些值，当然就应该要传出某些值！

```python
def flag(name):
  '''实现简单的字符串输出'''
	return "代码改变世界 艺术就是爆炸 - {}".format(name)

p = flag("回到古代见李白")
print(p)

>>>代码改变世界 艺术就是爆炸 - 回到古代见李白
```

上述代码就是一个简单的函数有返回值的例子，它传入一个值，返回一个值，值被p变量接收，而后打印出来！

**值得注意的是：p = flag("回到古代见李白")这是调用并将返回值赋值给p，但是 p = flag 则是将函数flag赋值给p，p指向这个函数，p就是函数flag了，print(p("回到古代见李白"))会返回和上述代码相同的结果！**

```python
def flag(name):
  '''实现简单的字符串输出'''
  return "代码改变世界 艺术就是爆炸 - {}".format(name)

p = flag
print(p('回到古代见李白'))

>>>代码改变世界 艺术就是爆炸 - 回到古代见李白
```

### lambda关键字

使用lambda关键字可以创建一个匿名函数--->一个短小精悍没有名字的函数！

它的格式为：lambda 参数: 表达式

```python
lambda x: x**2   # 匿名函数的定义
num = lambda x: x**2 # 匿名函数可赋值给一个变量
print(num(8))   # 调用承接的匿名函数
print((lambda x: x**2)(8))   # 匿名函数的调用并打印

>>>64
>>>64
```

既然匿名函数可赋值给一个变量，那么就可以做一些高级的事情了！

```python
def func(sqrt,li):
	return [sqrt(x) for x in li]   # 列表解析式
sqrt = lambda x: x**2
li = [1,2,3,4]
sqrt_li = func(sqrt,li)
print(sqrt_li)

>>>[1, 4, 9, 16]
```

你也许会说，[x**2 for x in li]可以完成一样的事情啊，的确如此，但是如果不是计算平方，而是更复杂的情况呢？

### 变量的作用域

变量是有作用域的，通常我们定义在外边的变量是全局变量，定义在函数内的变量叫做局部变量！

全局变量即在程序的任意地方均可访问，只要在程序运行的过程中这个变量都存在！只有在程序关闭时全局变量才会消失。

而局部变量的作用范围只在所处的那个函数模块范围内！一旦程序运行出此函数，那么这个变量就会被回收！

但是通过global关键字，可将定义在函数内的变量声明为全局变量。

global语句用于表明特定变量在全局作用域里，并应在全局作用域中重新绑定；nonlocal语句表明特定变量在外层作用域中，并应在外层作用域中重新绑定。

### global关键字

```python
# example1
a = 1

def test1():
   a = 2

test1()
print(a)

>>>1
'''由example1可知，a=2变量的存活时间仅为函数运行期间'''

# example2
b = 1

def test2():
   global b
   b = 2

test2()
print(b)

>>>2

'''由example2可知，通过在函数内部声明此变量为全局变量，从而将其修改并改变函数外部的变量值'''

# example3
global c
c = 1

def test3():
   c = 2

test3()
print(c)

>>>1

'''由example3可知，将global写在外部，然并卵！！！'''
```

### 函数番外

传递形参的数据可以是字符串，数值，列表，字典，集合等

函数的返回值可以是字符串，数值，列表，字典，集合等

通过将代码封装成一个个函数，可以非常直观的调用和安排程序的实现，直观清晰！

### 内置函数

来源:菜鸟教程---这方面的整理菜鸟教程还是挺全的！！！

| 内置函数                                                     | 内置函数                                                     | 内置函数                                                     | 内置函数                                                     | 内置函数                                                     |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | ------------------------------------------------------------ |
| [abs()](https://www.runoob.com/python/func-number-abs.html)  | [divmod()](https://www.runoob.com/python/python-func-divmod.html) | [input()](https://www.runoob.com/python/python-func-input.html) | [open()](https://www.runoob.com/python/python-func-open.html) | [staticmethod()](https://www.runoob.com/python/python-func-staticmethod.html) |
| [all()](https://www.runoob.com/python/python-func-all.html)  | [enumerate()](https://www.runoob.com/python/python-func-enumerate.html) | [int()](https://www.runoob.com/python/python-func-int.html)  | [ord()](https://www.runoob.com/python/python-func-ord.html)  | [str()](https://www.runoob.com/python/python-func-str.html)  |
| [any()](https://www.runoob.com/python/python-func-any.html)  | [eval()](https://www.runoob.com/python/python-func-eval.html) | [isinstance()](https://www.runoob.com/python/python-func-isinstance.html) | [pow()](https://www.runoob.com/python/func-number-pow.html)  | [sum()](https://www.runoob.com/python/python-func-sum.html)  |
| [basestring()](https://www.runoob.com/python/python-func-basestring.html) | [execfile()](https://www.runoob.com/python/python-func-execfile.html) | [issubclass()](https://www.runoob.com/python/python-func-issubclass.html) | [print()](https://www.runoob.com/python/python-func-print.html) | [super()](https://www.runoob.com/python/python-func-super.html) |
| [bin()](https://www.runoob.com/python/python-func-bin.html)  | [file()](https://www.runoob.com/python/python-func-file.html) | [iter()](https://www.runoob.com/python/python-func-iter.html) | [property()](https://www.runoob.com/python/python-func-property.html) | [tuple()](https://www.runoob.com/python/att-tuple-tuple.html) |
| [bool()](https://www.runoob.com/python/python-func-bool.html) | [filter()](https://www.runoob.com/python/python-func-filter.html) | [len()](https://www.runoob.com/python/att-string-len.html)   | [range()](https://www.runoob.com/python/python-func-range.html) | [type()](https://www.runoob.com/python/python-func-type.html) |
| [bytearray()](https://www.runoob.com/python/python-func-bytearray.html) | [float()](https://www.runoob.com/python/python-func-float.html) | [list()](https://www.runoob.com/python/att-list-list.html)   | [raw_input()](https://www.runoob.com/python/python-func-raw_input.html) | [unichr()](https://www.runoob.com/python/python-func-unichr.html) |
| [callable()](https://www.runoob.com/python/python-func-callable.html) | [format()](https://www.runoob.com/python/att-string-format.html) | [locals()](https://www.runoob.com/python/python-func-locals.html) | [reduce()](https://www.runoob.com/python/python-func-reduce.html) | unicode()                                                    |
| [chr()](https://www.runoob.com/python/python-func-chr.html)  | [frozenset()](https://www.runoob.com/python/python-func-frozenset.html) | [long()](https://www.runoob.com/python/python-func-long.html) | [reload()](https://www.runoob.com/python/python-func-reload.html) | [vars()](https://www.runoob.com/python/python-func-vars.html) |
| [classmethod()](https://www.runoob.com/python/python-func-classmethod.html) | [getattr()](https://www.runoob.com/python/python-func-getattr.html) | [map()](https://www.runoob.com/python/python-func-map.html)  | [repr()](https://www.runoob.com/python/python-func-repr.html) | [xrange()](https://www.runoob.com/python/python-func-xrange.html) |
| [cmp()](https://www.runoob.com/python/func-number-cmp.html)  | [globals()](https://www.runoob.com/python/python-func-globals.html) | [max()](https://www.runoob.com/python/func-number-max.html)  | [reverse()](https://www.runoob.com/python/att-list-reverse.html) | [zip()](https://www.runoob.com/python/python-func-zip.html)  |
| [compile()](https://www.runoob.com/python/python-func-compile.html) | [hasattr()](https://www.runoob.com/python/python-func-hasattr.html) | [memoryview()](https://www.runoob.com/python/python-func-memoryview.html) | [round()](https://www.runoob.com/python/func-number-round.html) | [__import__()](https://www.runoob.com/python/python-func-__import__.html) |
| [complex()](https://www.runoob.com/python/python-func-complex.html) | [hash()](https://www.runoob.com/python/python-func-hash.html) | [min()](https://www.runoob.com/python/func-number-min.html)  | [set()](https://www.runoob.com/python/python-func-set.html)  |                                                              |
| [delattr()](https://www.runoob.com/python/python-func-delattr.html) | [help()](https://www.runoob.com/python/python-func-help.html) | [next()](https://www.runoob.com/python/python-func-next.html) | [setattr()](https://www.runoob.com/python/python-func-setattr.html) |                                                              |
| [dict()](https://www.runoob.com/python/python-func-dict.html) | [hex()](https://www.runoob.com/python/python-func-hex.html)  | object()                                                     | [slice()](https://www.runoob.com/python/python-func-slice.html) |                                                              |
| [dir()](https://www.runoob.com/python/python-func-dir.html)  | [id()](https://www.runoob.com/python/python-func-id.html)    | [oct()](https://www.runoob.com/python/python-func-oct.html)  | [sorted()](https://www.runoob.com/python/python-func-sorted.html) | [exec 内置表达式](https://www.runoob.com/python/python-func-exec.html) |

### 高阶函数

一个函数接收另外一个函数作为参数，这个函数称之为高阶函数。

```python
def sqrt(func,li):
  return new_li = [func(i) for i in li]

func = lambda x: x**2
li = [1,2,3]
sqrt_li = sqrt(func,li)
print(sqr_li)

>>>[1,4,9]
```

**1.enumerate()函数**

**序列函数enumerate(*iterable, start=0)**

在Python中有这么几种序列，列表，元组，字符串（同样属于string类型）

而在日常编程中，有时候我们在遍历序列的时候需要同时输出索引，按照正常思路通常我们会在外部引用一个变量来对循环进行计数从而达到计算每一个元素索引的目的，但是在Python有内置enumerate函数来帮助我们便捷的在遍历序列时同时输出索引！

```python
# 可变序列-列表
example = [1,2,3]

for i in enumerate(example):
    print(i)
    
>>>(0, 1)
>>>(1, 2)
>>>(2, 3)

# 可以看到，enumerate函数接收一个序列/可迭代对象并返回不可变序列-元组类型的索引和元素
# 可迭代对象（iterable）包括以下类型：迭代器iterator、序列sequence、字典dictionary等

# 因此，还可以这样输出
example = [1,2,3]
for i,j in enumerate(example):
    print(i,j)
    
>>>0 1
>>>1 2
>>>2 3
```

```python
dict = {'a':'andy','b':'bob','c':'cily'}

for i in enumerate(dict):
    print(i)

>>>(0, 'a')
>>>(1, 'b')
>>>(2, 'c')

dict = {'a':'andy','b':'bob','c':'cily'}

for i,j in enumerate(dict):
    print(i,j)

>>>0 a
>>>1 b
>>>2 c

# 还记得如何遍历出字典的key和value吗？
```

**2.zip()函数**

**序列函数zip(*iterables)**

可迭代对象（iterable）包括以下类型：迭代器iterator、序列sequence、字典dictionary等

我们平常在解决问题时总是会遇到需要同时遍历多个列表，字典等等，针对这种情况，我们可以利用Python中内置的zip函数，顾名思义zip就是拉链，给多个可迭代对象拉上拉链！

```python
# 同时遍历多个列表
a = [1,2,3,4]
b = [1,2,3,4]
# 注意同时遍历多个可迭代对象时，输出元素个数取决于最少元素的可迭代对象
for i,j in zip(a,b):
    print(i,j)

>>>1 1
>>>2 2
>>>3 3
>>>4 4

# zip(a)和zip(b)
print(zip(a),zip(b))

>>><zip object at 0x1010a0b00>
>>><zip object at 0x101106c40>

# 与enumerate函数搭配使用
a = [1,2,3,4]
b = [1,2,3,4]

for i,(a,b) in enumerate(zip(a,b)):
    print("{}:{},{}".format(i,a,b))
    
>>>0:1,1
>>>1:2,2
>>>2:3,3
>>>3:4,4
```

**3.map()函数**

**序列函数map(function, iterable, ...)**

在编程时有时也会有这样的需求，就是对可迭代对象中的元素（比如列表），做一些复杂的操作实现，此时借助Python内置函数map就可以轻松实现！

map函数接收一个函数对象和多个可迭代对象，其作用就是将function作用与可迭代对象中的每一个元素，这样去借助Python内置函数写出来的代码更加Pythonic，而不需要自己实现相应的循环遍历操作...

通俗地讲，map(function, iterable, ...)的作用就是，先让函数作用于列表中的每个元素，然后这些元素作用后新生成的元素再次组成一个数据集，这个数据集是迭代器，map函数的最终结果就是返回这么一个迭代器。

```python
# 作用一个可迭代对象
def square(x):
    return x**2


example = [1,2,3,4,5]

print(map(square,example))

<map object at 0x102ee8160>
# 并没有返回相应操作后的元素列表，为什么呢？
# 原因就是map()是迭代器，需要使用list(map())来查看里面的元素
print(list(map(square,example)))

>>>[1, 4, 9, 16, 25]

# 作用多个可迭代对象
def add(x, y): # 注意形参数量和传入map的可迭代对象数量一致
    return x + y

l1 = [1, 2, 3]
l2 = [3, 2, 1]

list(map(add, l1, l2))

>>>[4, 4, 4]

# 返回了相应操作后的列表
# 这个例子只是简单的操作实现
# 根据需要可以实现复杂的函数操作
```

最后，通常map(function, iterable)可以使用[function(x) for x in iterable]来代替，如上面的例子可以改为：

```python
def square(x):
    return x**2
    
    
example = [1,2,3,4,5]

l =[square(x) for x in example]

print(l)

>>>[1, 4, 9, 16, 25]
```

**4.filter()函数**

**序列函数filter(function, iterable)**

参数function是一个能够对可迭代对象(iterable)中的元素进行True或者False判断的函数。filter函数返回的就是可迭代对象(iterable)中经过function函数判断后为True的元素构成的迭代器(iterator)。

```python
l = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

def function(n):
    if n > 0:
        return True
    else:
        return False
        

filter(function, l)  # 返回的是一个迭代器，无法直接查看。
>>><filter at 0x1f8ac90b348>

l1 = list(filter(function, l))  # 迭代器中的元素可以通过list()来查看。

l1
>>>[1, 2, 3, 4, 5] # 返回了判断为true的元素
```

filter配合可迭代对象如列表、字典，尤其是配合字典时，就很有意思：

```python
strength = {'吕布': 100, '张飞': 98, '关羽': 97, '张郃': 94, '牛金': 83, '潘凤': 75, '刘禅': 7}

for i in filter(lambda x: x[1] > 90, strength.items()):
    print(i, end = " ")
    
>>>('吕布', 100) ('张飞', 98) ('关羽', 97) ('张郃', 94) 

for i in filter(lambda x: 60 < x[1] < 90, strength.items()):
    print(i, end = " ")
    
>>>('牛金', 83) ('潘凤', 75) 

for i in filter(lambda x: x[1] < 10, strength.items()):
    print(i, end = " ")
    
>>>('刘禅', 7) 
```

**5.reduce()函数**

**序列函数functools.reduce(function, iterable[, initializer]) - 曾经的内置函数**

function：<u>一个有两个参数的函数。</u>

iterable：<u>可迭代对象，function累积性地对列表中的每个元素从左到右逐一进行二目计算（比如两个数相加或相乘），从而达到减少序列中元素数量的目的，最终把序列中的所有元素利用function累积计算成为了一个元素。reduce的意思是减少，符合这个函数表达的功能。</u>

initializer：<u>function的初始作用元素，默认为None。可选参数。</u>

```python
# import functools or from functools import reduce

from functools import reduce

def add(x, y):
    return x + y
    

reduce(add, [1, 2, 3, 4, 5])

>>>15

def multiply(x, y):
    return x * y
    

reduce(multiply, [1, 2, 3, 4, 5])

>>>120
```

下面介绍可选参数-initializer

```python
reduce(add, [1, 2, 3, 4, 5],  6)

>>>21

'''
添加了一个6之后，最后结果从15变成了21，是什么原因？
就是(((((6+1)+2)+3)+4)+5)的计算结果，
6是第一次调用函数add(x, y)中的x，1是y，后面2、3、4、5依次累加。
'''
```

**6.reverse()函数**

这个函数非常简单，其语法是reversed(seq)，返回一个反向排序的序列seq的**迭代器**。参数只有一个，且必须是序列这种具有反转功能的可迭代对象，比如序列中的字符串、列表、元组等，而不能是字典、集合等数据类型，否则会报错。

这里要强调的是，跟我们想象的不同，reversed(seq)函数返回的是迭代器，而不是seq经过反向排序后的相同数据类型。它也没有改变原序列seq，而是生成了一个新的反向排序的副本的迭代器；seq依然是原来的样子。

```python
t = (1, 2, 3, 5, 4)  # 元组。

reversed(t)  # reversed()函数生成了一个迭代器。
Out[78]: <reversed at 0x1f736509408>

t  # 经过reversed()函数后没有改变。
Out[79]: (1, 2, 3, 5, 4)

list(reversed(t))  # 迭代器用list()函数查看。
Out[80]: [4, 5, 3, 2, 1]

l = ['a', 'd', 'e', 'c', 'b']

list(reversed(l))
Out[82]: ['b', 'c', 'e', 'd', 'a']
```

**7.sorted()函数**

**sorted函数同样是排序函数，但比reversed函数复杂不少，甚至某种程度上可以说sorted函数包含了reversed函数的功能。**

sorted函数具体语法是：sorted(iterable, key=None, reverse=False)——根据iterable（可迭代对象）中的项返回一个新的已排序**列表**（注意**列表**两个字，即使iterable是个字符串，它也会将其转换成**列表**）。

<u>***iterable**（可迭代对象）——要进行排序的可迭代对象，以序列（列表等）最为常见。*</u>

<u>***key**——指定带有单个参数的函数，用于从iterable（可迭代对象）的每个元素中提取用于比较的键 (例如key=str.lower)。默认值为None(直接比较元素)。key参数在复合型数据类型中用得比较多。*</u>

<u>**reverse**——为一个布尔值，默认为False，即不反向排序。如果设为True，则每个列表元素将按反向顺序比较进行排序。换句话说，reverse=False时是默认的升序排序；reverse=True时是降序排序。觉得reverse这个参数眼熟吗？它其实就是前面reversed函数的另外一种形式，只不过在这里做了参数。*</u>

```python
s = 'pythoncoder'

sorted(s)  # sorted()函数返回的是一个**列表**。

>>>['c', 'd', 'e', 'h', 'n', 'o', 'o', 'p', 'r', 't', 'y']

print(s)  # s没有改变。

>>>'pythoncoder'

p = sorted(s, reverse=True)  # reverse=True时降序排序。
print(p)

>>>['y', 't', 'r', 'p', 'o', 'o', 'n', 'h', 'e', 'd', 'c']

str = ''
print(str.join(p))

>>>ytrpoonhedc
```

第二个参数key在复合型数据类型中常常与lambda函数搭配，能发挥不一样的效果。

```python
counsellors = (('周瑜', 97), ('郭嘉', 98), ('诸葛亮', 100), ('荀彧', 99), ('鲁肃', 96))

# 注意counsellors原本是个元组数据类型，但sorted()之后返回了一个列表类型。

sorted(counsellors, key=lambda x: x[1], reverse=True)

>>>[('诸葛亮', 100), ('荀彧', 99), ('郭嘉', 98), ('周瑜', 97), ('鲁肃', 96)]
```

### 函数闭包

当我们嵌套定义了函数，就创建了一个闭包函数！

```python
from math import pow

# 注意n与x这两个参数的传参
def make_pow(n):
    def inner_func(x):     # 嵌套定义了 inner_func
        return pow(x, n)   # 注意这里引用了外部函数的 n
    return inner_func      # 返回 inner_func

pow2 = make_pow(2)  # 理解为实例化一个函数make_pow
print(pow2) # 查看pow2
print(pow2(6)) # 调用pow2函数

>>><function make_pow.<locals>.inner_func at 0x104d4c940>
>>>36.0
```

```
闭包的作用：
闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在。
闭包在运行时可以有多个实例，即使传入的参数相同。
```

### 函数装饰器

```python
def hello():
    return 'hello world'
  
def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped
  
hello = makeitalic(hello)
print(hello())

>>><i>hello world</i>
```



```python
def makeitalic(func):
    def wrapped(*args, **kwargs):
        ret = func(*args, **kwargs)
        return '<i>' + ret + '</i>'
    return wrapped

@makeitalic
def hello1(name):
    return 'hello %s' %name

@makeitalic
def hello2(name1, name2):
    return 'hello %s, %s' % (name1, name2)

print(hello1('lxh'))
print(hello2('lxx','lxl'))

>>><i>hello lxh</i>
>>><i>hello lxx, lxl</i>
```



```python
def wrap_in_tag(tag):
    def decorator(func):
        def wrapped(*args, **kwargs):
            ret = func(*args, **kwargs)
            return '<' + tag + '>' + ret + '<' + tag +'>'
        return wrapped
    return decorator

# 现在，我们可以根据需要生成想要的装饰器了：
makebold = wrap_in_tag('b')

@makebold
def hello(name):
    return 'hello %s' %(name)

print(hello('lxh'))

# 更加简洁的写法
@wrap_in_tag('b')
def hello(name):
    return 'hello %s' % name

```



```python
def makebold(func):
    def wrapped():
        return '<b>' + func() + '</b>'

    return wrapped

def makeitalic(func):
    def wrapped():
        return '<i>' + func() + '</i>'

    return wrapped

@makebold
@makeitalic
def hello():
    return 'hello world'

# 上面定义了两个装饰器，对 hello 进行装饰，上面的最后几行代码相当于：

def hello():
    return 'hello world'

hello = makebold(makeitalic(hello))
```

```
小结:
本质上，装饰器就是一个返回函数的高阶函数。
装饰器可以动态地修改一个类或函数的功能，通过在原有的类或者函数上包裹一层修饰类或修饰函数实现。
事实上，装饰器就是闭包的一种应用，但它比较特别，接收被装饰函数为参数，并返回一个函数，赋给被装饰函数，闭包则没这种限制。
```

## 面向对象-类

在类内创建的函数称为方法，类是面向对象中重要的概念。面向对象是相对于面向过程来讲的，面向对象把相关的数据和方法组织为一个整体看待，从更高的层次来进行系统分析、建模、更贴近事物的自然运行模式。

**面向对象与面向过程的区别：**

| 面向对象                                                     | 面向过程                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 面向对象是把构成问题的事物分解成多个对象，每个对象对应着它们的行为。 | 面向过程是把问题分解成步骤，然后用函数逐个的按次序来进行实现。 |
| 将问题中一个个对象进行类的实现                               | 遵从一个函数只解决一个问题原则                               |
| 最后组织各个对象逻辑实现                                     | 根据业务逻辑从上到下编写代码                                 |

### 简单的类实现

使用**面向对象**简而言之就是从问题中提取出一个个对象并抽象成对象，**封装**成**类**。

使用类来构建项目更为清晰和简洁！

```python
# 一个简单的面向对象的小例子
class Turtle:

    '''属性'''
    color = "green"
    leg = "four"
    weight = "10kg"
    shell = True
    mouth_size = "big"

    '''方法'''
    def climb(self):
        print("小乌龟正在爬...")

    def run(self):
        print("小乌龟正在跑...")

    def bite(self):
        print("小乌龟正在咬人...")

    def eat_food(self):
        print("小乌龟正在吃东西...")

    def sleep(self):
        print("小乌龟正在睡觉...")
```

上述代码虽然创建了一个类，但它还不算是一个真正的类，类可以理解为由属性和方法组成的。

比如一个人，他的皮肤白，身高高，体重重等等就是一个个属性，而他会走路，会跳跃，会打篮球等等就是一个个行为(方法)。

方法在类中就是用函数来实现，而需要注意的是：属性需要写在一个魔法方法里面！

```python
class Turtle:
	'''属性'''
  	def __init__(self):   # Python魔法方法:__init__(self),它会在创建对象(初始化)的时候自动被调用
      # 定义的这些属性在类中任何地方随意访问
      self.color = "green"
      self.leg = "four"
      self.weight = "10kg"
      self.shell = True
      self.mouth_size = "big"

    '''方法'''
    def climb(self):
        print("小乌龟正在爬...")

    def run(self):
        print("小乌龟正在跑...")

    def bite(self):
        print("小乌龟正在咬人...")

    def eat_food(self):
        print("小乌龟正在吃东西...")

    def sleep(self):
        print("小乌龟正在睡觉...")
```

我们注意到有非常多的self，通俗的来理解：self是当一个对象的方法被调用的时候,对象会将自身作为第一个参数传给self参数，python就会知道是那个对象在调用方法了！

```python
class Turtle:
		'''属性'''
    def __init__(self, color, leg, weight):
      self.color = color
      self.leg = leg
      self.weight = weight

    '''方法'''
    def Tcolor(self):
        print("我的颜色是{}".format(self.color))

    def Tleg(self):
        print("我有{}条腿".format(self.leg))

    def Tweight(self):
        print("我有{}斤".format(self.weight))

# 实例化类
whiteTurtle = Turtle("白色", "四", "三十")
# 调用类的方法
whiteTurtle.Tcolor()
whiteTurtle.Tleg()
whiteTurtle.Tweight()

>>>我的颜色是白色
>>>我有四条腿
>>>我有三十斤
```

当定义了一个类之后，调用的话就是先实例化一个类，然后对类中的方法进行调用。

一旦定义了一个类，便可以将这个类实例化给很多对象，只要你想，想实例化给多少对象都想行！例如上述代码就只实例化类一个小白龟对象！

注意：在init魔法方法里定义的变量，在实例化类时需要进行传值！

### 类的继承和多肽

受现实世界启发，比如动物涵盖了所有动物（猫，狗，鸭......），又如人涵盖了（黄种人，黑人，白人......），通常是利用一些特点来将动物或其他进行一级又一级的分类。

受现实世界启发，我们在创建类时亦可以这样设计，设计一个个类时考虑它们的共同点与继承关系，这样可以尽最大可能的保证利用已写的一些类的数据和方法，写出代码质量高且结构清晰的程序！

在面向对象中，当我们已经创建了一个类，而又想再创建一个与之相似的类，比如添加几个方法，或者修改原来的方法，这时我们不必从头开始，可以从原来的类派生出一个新的类，我们把原来的类称为父类或基类，而派生出的类称为子类，子类继承了父类的所有数据和方法。

例如：当我们已经创建了一个Animal类，Animal类中有动物通用的行为和特征时我们需要在创建一个被Animal涵盖的类只需继承Animal类，我们创建一个Dog类，众所周知Dog是一种动物，因此具有动物的通用行为！但动物之间又互相有所不同，因此我们可以重写一些数据和代码以尽可能的使代码简洁易读！

```python
# 首先我们定义一个Animal类：
class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)

# 而后我们想创建一个Dog类：
class Dog(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('WangWang.., I am %s. ' % self.name)

# 可以看到，Dog类和Animal类几乎是一样的，只是greet方法不一样，我们完全没必要创建一个新的类，而可以从Animal类派生出一个新的类：
class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s. ' % self.name)
        
# Dog类是从Animal类继承而来的，Dog类自动获得了Animal类的所有数据和方法，而且还可以对父类的方法进行修改。
# 具体使用：
animal = Animal('animal')  # 创建 animal 实例
animal.greet()

dog = Dog('dog')  # 创建 dog 实例
dog.greet()

# 我们还可以对Dog类添加新的方法：
class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s. ' % self.name)

    def run(self):
        print('I am running.I am running')

dog = Dog('dog')
dog.greet()
dog.run()

>>>Hello, I am animal.
>>>WangWang.., I am dog. 
>>>WangWang.., I am dog. 
>>>I am running.I am running
```

多态的概念其实不难理解，它是指->对不同类型的变量进行相同的操作，它会根据对象（或类）类型的不同而表现出不同的行为。

```python
# 事实上，我们经常用到多态的性质，比如：
print(1 + 2)
print('a' + 'b')
>>>3
>>>'ab'
# 可以看到，我们对两个整数进行 + 操作，会返回它们的和。
# 对两个字符进行相同的 + 操作，会返回拼接后的字符串。
# 也就是说，不同类型的对象对同一消息会作出不同的响应。
```

```python
# 再看看类的例子：
class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s.' % self.name)


class Cat(Animal):
    def greet(self):
        print('MiaoMiao.., I am %s' % self.name)

        
# 这个方法实现了隐藏对象调用细节
def hello(animal):
    animal.greet()

dog = Dog('dog')
cat = Cat('cat')

hello(dog)
hello(cat)

>>>WangWang.., I am dog.
>>>MiaoMiao.., I am cat
# 注意：Dog和Cat分别继承了Ainimal类并重写了greet方法，因此当我们实例化Dog类给dog变量时调用的hello方法中的animal是Dog对象，调用的也就是Dog对象的greet方法。
# 因此我们就能看到，cat和dog是两个不同的对象，对它们调用greet方法，它们会自动调用实际类型的greet方法，作出不同的响应。这就是多态的魅力。
```

```python
'''
小结:
继承可以拿到父类的所有数据和方法，子类可以重写父类的方法，也可以新增自己特有的方法。
有了继承，才有了多态，不同类的对象对同一消息会作出不同的相应。
'''
```

### super()的简单使用

在类的继承中，如果重定义某个方法，该方法会覆盖父类的同名方法，但有时，我们希望能同时实现父类的功能，这时，我们就需要调用父类的方法了，可通过使用 super 来实现，比如：

```python
class Animal(object):
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print('Hello, I am %s.' % self.name)

class Dog(Animal):
    def greet(self):
      	'''实现了在保留父类greet方法功能的同时增加其他功能'''
        super(Dog, self).greet() #Python3可使用super().greet()
        print('WangWang...')

# 在上面，Animal是父类，Dog是子类，我们在Dog类重定义了greet方法，为了能同时实现父类的功能，我们又调用了父类的方法，看下面的使用：
dog = Dog('dog')
dog.greet()

>>>Hello, I am dog.
>>>WangWang..

# super的一个最常见用法可以说是在子类中调用父类的初始化方法了，比如：
class Base(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class A(Base):
    def __init__(self, a, b, c):
      '''在保留父类数据的同时增加新的数据'''
        super(A, self).__init__(a, b)  # Python3可使用super().__init__(a, b)
        self.c = c
```

### 定制类和魔法方法

在 Python 中，我们可以经常看到以双下划线 \_\_ 包裹起来的方法，比如最常见的 \__init__，这些方法被称为魔法方法。

那么我们为什么要学习和使用这些魔法方法呢？

原因在于，这些Python自带的魔法方法在很多情况下默认的功能无法满足我们的需要，此时我们就需要在类中进行重写。

比如，我们在写一个简单的类时自然而然的写了\_\_init\_\_魔法方法并写了一些属性，这个就是重写了Python的\_\_init__魔法方法。

**1.类的构造与初始化**

我们都知道一个最基本的魔术方法， __init__ 。通过此方法我们可以定义一个对象的初始操作。但你知道吗，当实例化我们定义的类，如x = SomeClass() 的时候， \_\_init\_\_ 并不是第一个被调用的方法。实际上，还有一个叫做 \_\_new\_\_ 的方法，来实例化这个对象。然后给在开始创建时候的初始化函数 来传递参数。在对象生命周期的另一端，也有一个 \_\_del\_\_ 方法。接下来看一看这三个方法：

因此，如果此魔法方法的默认功能不满足你的需求时，便可以进行此魔法方法的重写。不过一般情况下并不需要重写它。

**1.1\_\_new\_\_魔法方法**

- （1）\_\_new\_\_(cls, [...]) 是在一个对象实例化的时候所调用的第一个方法，所以它才是真正意义上的构造方法。
- （2）它的第一个参数是这个类，其他的参数是用来直接传递给 __init__ 方法。
- （3）\_\_new\_\_ 决定是否要使用该 __init__ 方法，因为 __new__ 可以调用其他类的构造方法或者直接返回别的实例对象来作为本类的实例，如果  __new__ 没有返回实例对象，则 __init__ 不会被调用。
- （4）__new__ 主要是用于继承一个不可变的类型比如一个 tuple 或者 string。

```python
# 以此例子说明__new__是执行在__init__之前
class Person(object):

    def __new__(cls, *args, **kwargs):
        print("__new__()方法被调用了")
        print('这个是*agrs', *args)
        print('这个是kwagrs', **kwargs)
        
        # cls表示这个类，剩余所有的参数传给__init__()方法，
        # 若不返回，则__init__()不会被调用
        return object.__new__(cls)

    def __init__(self, name, age):
        print("__init__()方法被调用了")
        self.name = name
        self.age = age
        print(self.name, self.age)

p = Person("张三", 20)

>>>__new__()方法被调用了
>>>这个是*agrs 张三 20
>>>这个是kwagrs
>>>__init__()方法被调用了
>>>张三 20
```

**那new()在什么场景使用呢？**

**当我们需要继承内置类时，例如，想要继承 int、str、tuple，就无法使用 init 来初始化了，只能通过 new 来初始化数据。**

**例如下面例子，第一个类实例化的对象无法与数字进行加和，而第二个类则可以进行加和。**

```python
# 以此例说明__new__的具体用处之一
class A(object):
    def __init__(self, a):
        self.a = a

a = A(10)
print(a + 10)

>>>TypeError: unsupported operand type(s) for +: 'A' and 'int'
# 需要重写__new__魔法方法以实现其数字加和

class A(int):
    def __new__(cls, a):
        return int.__new__(cls, a)

    def __init__(self, a):
        self.a = a
        
a = A(10)
print(a + 10)

>>>20
```

**1.2\_\_init\_\_魔法方法**

`__init__()`方法：构造器，当一个实例被创建的时候调用的初始化方法。

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('张三', 20)
p2 = Person('李四', 22)
```

**1.3\_\_del\_\_魔法方法**

`__del__()`方法：析构器，当一个实例被销毁时自动调用的方法。

```python
class Washer:
    def __del__(self):
        """
        当删除对象时，解释器会自动调用del方法
        """
        print('对象已删除！')

haier = Washer() 

>>>对象已删除！
#在程序结束前Python会进行垃圾回收，即，自动销毁删除这些变量之类的。
```

**2.类的表示**

**2.1\_\_str__ & \_\_repr__魔法方法**

这两个方法都是用来描述类或对象信息的。

比如你直接实例化了一个对象，打印出来的是这个对象的地址。

而要是重新在类中定义了这两个方法，那打印对象的结果就是方法返回的信息。

```python
# 观察下面两个类我相信你就懂得了它们的用处了
class A:
    def __init__(self):
        pass

a = A()
print(a)


class B:
    def __init__(self):
        pass

    def __repr__(self):
        return '我是__repr__魔法方法'

    def __str__(self):
        return '我是__str__魔法方法'

b = B()
print(b)

>>><__main__.A object at 0x104c04190>   # 不定义str方法，直接打印，结果是对象的内存地址
>>>我是__str__魔法方法   # 定义了str方法，显示的就是str方法返回的内容

'''
那么为什么要写__repr__魔法方法呢？
其目的不一样: __repr__的目标是准确性，或者说，__repr__的结果是让解释器用的。
		    __str__的目标是可读性，或者说，__str__的结果是让人看的
'''
```

**2.2\_\_bool\_\_魔法方法**

当调用 bool(obj) 时，会调用 `__bool__()` 方法，返回 True 或 False。

```python
class Person:
    def __init__(self, old):
        self.old = old

    def __bool__(self):
        if self.old > 18:
            return True
        return False

student = Person(17)
print(bool(student))

>>>False
```

**3.访问控制**

- __setattr__：定义当一个属性被设置时的行为
- __getattr__：定义当用户试图获取一个不存在的属性时的行为
- __delattr__：删除某个属性时调用
- __getattribute__：访问任意属性或方法时调用

```python
class Person(object):

    def __setattr__(self, key, value):
        """属性赋值"""
        if key not in ('name', 'age'):
            return
        if key == 'age' and value < 0:
            raise ValueError()
        super(Person, self).__setattr__(key, value)

    def __getattr__(self, key):
        """访问某个不存在的属性"""
        return 'unknown'

    def __delattr__(self, key):
        """删除某个属性"""
        if key == 'name':
            raise AttributeError()
        super().__delattr__(key)

    def __getattribute__(self, key):
        """所有属性/方法调用都经过这里"""
        if key == 'money':
            return 100
        elif key == 'hello':
            return self.say
        return super().__getattribute__(key)

p1 = Person()
p1.name = '张三'  # 调用__setattr__
p1.age = 20  # 调用__setattr__
print(p1.name, p1.age)  # 张三 20

setattr(p1, 'name', '李四')	# 调用__setattr__
setattr(p1, 'age', 30)  # 调用__setattr__
print(p1.name, p1.age)  # 李四 30

print(p1.sex)  # 调用__getattr__

# 上面只要是访问属性的地方，都会调用__getattribute__方法，因此你可以重写它来达到一些目的
```

**4.容器类操作**

- __setitem__(self, key, value)：定义设置容器中指定元素的行为，相当于 self[key] = value；

- __getitem__(self, key)： 定义获取容器中指定元素的行为，相当于 self[key]；

- __delitem__(self, key)：定义删除容器中指定元素的行为，相当于 del self[key]；

- __len__(self)：定义当被 len() 调用时的行为（返回容器中元素的个数）；

- __iter__(self)：定义当迭代容器中的元素的行为；

- __contains__(self, item)：定义当使用成员测试运算符（in 或 not in）时的行为；

- __reversed__(self)：定义当被 reversed() 调用时的行为。

Python 中常见的容器类型有：字典、元组、列表、字符串

因为它们都是「可迭代」的。可迭代是因为，它们都实现了容器协议，也就是下面要介绍到的魔法方法。

下面通过自己定义类实现列表，来说明这些方法的用法：

```python
# 实现一个自己的列表
class MyList(object):
    """自己实现一个list"""

    def __init__(self, values=None):
        # 初始化自定义list
        self.values = values or []
        self._index = 0

    def __setitem__(self, key, value):
        # 添加元素
        self.values[key] = value

    def __getitem__(self, key):
        # 获取元素
        return self.values[key]

    def __delitem__(self, key):
        # 删除元素
        del self.values[key]

    def __len__(self):
        # 自定义list的元素个数
        return len(self.values)

    def __iter__(self):
        # 可迭代
        return self

    def __next__(self):
        # 迭代的具体细节
        # 如果__iter__返回self 则必须实现此方法
        if self._index >= len(self.values):
            raise StopIteration()
        value = self.values[self._index]
        self._index += 1
        return value

    def __contains__(self, key):
        # 元素是否在自定义list中
        return key in self.values

    def __reversed__(self):
        # 反转
        return list(reversed(self.values))

# 初始化自定义list
my_list = MyList([1, 2, 3, 4, 5])

print(my_list[0])	     # __getitem__
my_list[1] = 20		     # __setitem__

print(1 in my_list)	     # __contains__
print(len(my_list))     # __len__

print([i for i in my_list])  # __iter__
del my_list[0]	             # __del__

reversed_list = reversed(my_list) # __reversed__
print([i for i in reversed_list])  # __iter__

# 尝试自己去独立实现一个字典
```

**5.可调用对象**

在Python中，方法也是一种高等的对象。这意味着他们也可以像其他对象一样被传递到方法中，这是一个非常惊人的特性。 Python中有一个特殊的魔术方法可以让类的实例的行为表现的像函数一样，你可以调用他们，将一个函数当做一个参数传到另外一个函数中等等。这个魔法方法就是 **\_\_call\_\_(self, [args...])**。

下面通过实际例子说明：

```python
class Circle(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y = y

a = Circle(10, 20)	 # __init__
print(a.x, a.y)	# 10 20

a(100, 200)	# 此时a这个对象可以当做一个方法来执行，这是__call__魔法方法的功劳
print(a.x, a.y)	 # 100 200
```

**6.比较操作**

- `__eq__()`
- `__ne__()`
- `__lt__()`
- `__gt__()`

**\_\_eq\_\_ 方法，可以判断两个对象是否相等**

```python
class Person(object):
    def __init__(self, uid):
        self.uid = uid

    def __eq__(self, other):
        return self.uid == other.uid

p1 = Person(1)
p2 = Person(1)
p3 = Person(2)
print(p1)
print(p1 == p2) # True
print(p2 == p3) # False
```

**判断两个对象是否不相等，这个和eq()方法基本一样，只不过这个是反面**

```python
class Person(object):
    def __init__(self, uid):
        self.uid = uid

    def __ne__(self, other):
        """对象 != 判断"""
        return self.uid != other.uid

p1 = Person(1)
p2 = Person(1)
p3 = Person(2)

print(p1 != p2) # False
print(p2 != p3) # True
```

**这两个方法比较对象的大小的，`__lt__()`为小于，`__gt__()`为大于**

```python
class Person(object):
    def __init__(self, uid):
        self.uid = uid

    def __lt__(self, other):
        """对象 < 判断 根据self.uid"""
        return self.uid < other

    def __gt__(self, other):
        """对象 > 判断 根据self.uid"""
        return self.uid > other

p1 = Person(1)
p2 = Person(1)
p3 = Person(2)

print(p1 < p2) # False
print(p2 < p3) # True

print(p1 > p2) # False
print(p2 > p3) # False
```

**7.序列化**

Python 提供了序列化模块 `pickle`，当使用这个模块序列化一个实例化对象时，也可以通过魔法方法来实现自己的逻辑，这些魔法方法包括：

- `__getstate__()`
- `__setstate__()`

```python
import pickle

class Person(object):

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __getstate__(self):
        # 执行 pick.dumps 时 忽略 age 属性
        return {
            'name': self.name,
            'birthday': self.birthday
        }

    def __setstate__(self, state):
        # 执行 pick.loads 时 忽略 age 属性
        self.name = state['name']
        self.birthday = state['birthday']

person = Person('李四', 20, (2017, 2, 23))
pickled_person = pickle.dumps(person) # 自动执行 __getstate__ 方法

p = pickle.loads(pickled_person) # 自动执行 __setstate__ 方法
print(p.name, p.birthday)  # 李四 (2017, 2, 23)
# 由于执行 pick.loads 时 忽略 age 属性，所以下面执行回报错
print(p.age)  # AttributeError: 'Person' object has no attribute 'age'
```

```python
'''
__getstate__()：
这个例子首先初始了 Person 对象，其中包括 3 个属性：name、age、birthday。
当调用 pickle.dumps(person) 时，__getstate__ 方法就会被调用，在这里忽略了 Person 对象的 age 属性，那么 person 在序列化时，就只会对其他两个属性进行保存。

__setstate__()：
同样地，当调用 pickle.loads(pickled_person) 时，__setstate__ 会被调用，其中传入的参数就是 __getstate__ 返回的结果。
在 __setstate__ 方法，我们从入参中取得了被序列化的 dict，然后从 dict 中取出对应的属性，就达到了反序列化的效果。
'''
```

### \_\_slots\_\_ 魔法

限制类中绑定的属性，防止用户从外部添加类属性。注意：仅对当前类生效，对子类不生效。

```python
# 在 Python 中，我们在定义类的时候可以定义属性和方法。
# 当我们创建了一个类的实例后，我们还可以给该实例绑定任意新的属性和方法。

# 看下面一个简单的例子：

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point(3, 4)
p.z = 5    # 绑定了一个新的属性
print(p.z)
print(p.__dict__)

# 在上面，我们创建了实例 p 之后，给它绑定了一个新的属性 z，
# 这种动态绑定的功能虽然很有用，但它的代价是消耗了更多的内存。

# 因此，为了不浪费内存，可以使用 __slots__来告诉 Python
# 只给一个固定集合的属性分配空间，对上面的代码做一点改进，如下：

class Point(object):
    __slots__ = ('x', 'y')       # 只允许使用 x 和 y 从而限制用户从类的外部来添加属性

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# 上面，我们给 __slots__ 设置了一个元组，来限制类能添加的属性。
# 现在，如果我们想绑定一个新的属性，比如 z，就会出错了，如下：

p = Point(3, 4)
p.z = 5
#---------------------------------------------------------------------------
"""AttributeError                            Traceback (most recent call last)
<ipython-input-648-625ed954d865> in <module>()
----> 1 p.z = 5
AttributeError: 'Point' object has no attribute 'z'
"""

# 使用 __slots__ 有一点需要注意的是，__slots__ 设置的属性仅对当前类有效，
# 对继承的子类不起效，除非子类也定义了 __slots__，这样，子类允许定义的属性就是自身的 slots 加上父类的 slots。

'''
小结:
slots 魔法：限定允许绑定的属性.
__slots__ 设置的属性仅对当前类有效，对继承的子类不起效，
除非子类也定义了 slots，这样，子类允许定义的属性就是自身的 slots 加上父类的 slots。
'''
```

### @property装饰器

使类中的方法可以像属性那样访问

```python
# 在使用@property 之前，让我们先来看一个简单的例子：

class Exam(object):
    def __init__(self, score):
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

e = Exam(60)
e.get_score()

e.set_score(70)
e.get_score()

'''
在上面，我们定义了一个 Exam 类，为了避免直接对 _score 属性操作，
我们提供了 get_score 和 set_score 方法，这样起到了封装的作用，
把一些不想对外公开的属性隐蔽起来，而只是提供方法给用户操作，在方法里面，我们可以检查参数的合理性等。
'''

# 这样做没什么问题，但是我们有更简单的方式来做这件事，
# Python 提供了 property 装饰器，被装饰的方法，我们可以将其『当作』属性来用，看下面的例子：

class Exam(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

e = Exam(60)
e.score

e.score = 90
e.score

e.score = 200
e.score

# 在上面，我们给方法 score 加上了 @property，
# 于是我们可以把 score 当成一个属性来用，
# 此时，又会创建一个新的装饰器 score.setter，
# 它可以把被装饰的方法变成属性来赋值。

# 另外，我们也不一定要使用 score.setter 这个装饰器，这时 score 就变成一个只读属性了：

class Exam(object):
    def __init__(self, score):
        self._score = score

    @property
    def score(self):
        return self._score

e = Exam(60)
e.score
e.score = 200  # score 是只读属性，不能设置值

'''
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-676-b0515304f6e0> in <module>()
----> 1 e.score = 200

AttributeError: can't set attribute
'''

'''
小结:
@property 把方法『变成』了属性。
'''
```

### 静态方法和类方法

在前面我们创建的类中的方法均是基于对象的行为与特征，但是有一些方法它不基于对象的行为与特征。

就好比我们创建一个三角形对象，在将三条边组合之前需要验证其中两边之和是否大于第三边，那么这个方法它就不属于该对象的行为与特征。此时我们使用静态方法来表示这类不基于对象的方法。

简而言之就是：那些和我们封装类行为没啥关系的，但是又需要创建的方法，写成静态方法。

```python
from math import sqrt


class Triangle(object):

    def __init__(self, a, b , c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    def tri_len(self):
        return self._a + self._b + self._c

    def tri_area(self):
        half = self.tri_len() / 2
        return sqrt(half * (half - self.a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 1, 2, 3
    # 静态方法和类方法都是通过给类发送消息调用(而不是创建的对象)
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print("此三角形的周长：{}".format(t.tri_len()))
        print("此三角形的面积：{}".format(t.tri_area()))
    else:
        print("无法构成三角形")
        
        
if __name__ == "__main__":
    main()
```

和静态方法比较类似，Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方也称之为类的元数据对象），通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象。

简而言之：使用类方法来获取类相关的信息并且还能创建出类的对象。

```python
from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
```

**元类**
类创建实例，元类创建类。

元类主要做了三件事：

1. 拦截类的创建
2. 修改类的定义
3. 返回修改后的类

当你创建类时，解释器会调用元类来生成它，定义一个继承自 object 的普通类意味着调用 type 来创建它。

### 面向对象编程实战

```python
import requests
import re
import os
from threading import Thread


# 类来实现的31小说网爬虫
class Spider(object):

    def __init__(self,name,url,):
        '''爬虫的属性'''
        self.name = name
        self.url = url
		self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

    def attain_urls(self,content_url):
        '''爬虫的方法'''
        req = requests.get(url=content_url, headers=self.headers)
        res = req.text

        title_list = re.findall('<dd><a href=".*?">(.*?)</a></dd>', res, re.S)
        list_urls = re.findall("(\/\d+\/\d+\/\d+\.html)", res, re.S)

        print(title_list,list_urls)

        return title_list,list_urls


    def parse_data(self,url,File_path,title):
        '''解析数据'''
        pre_req = requests.get(url=url, headers=self.headers)
        pre_res = pre_req.text

        story = re.findall('<p>(.*?)</p>', pre_res, re.S)
        print(story)
        
        # 持久性存储
        filePath = File_path + "." + title + '.text'
        with open(filePath, 'w', encoding='utf-8') as fp:
            fp.write(story)


    def save_data(self):
        '''保存数据'''
        name = input("请输入小说名字:")
        content_url = input("请输入小说目录页面url:")

        File_path = './' + name + '/'
        if not os.path.exists(File_path):
            os.mkdir(File_path)

        title_list,list_urls = self.attain_urls(content_url)

        count = 0
        for url in list_urls:
            title = "try"

            url = self.url + content_url

            #self.parse_data(url,File_path,title)
            self.theading(url,File_path,title)

            count = count + 1


    def theading(self,url,File_path,title):
        '''多线程'''
        thead = Thread(target=self.parse_data,args=(url,File_path,title,))
        thead.setDaemon(True)
        thead.start()


if __name__ == "__main__":
  	# 注爬虫因时效性可能无法正常运行
    spider = Spider(name="31小说网爬虫",url="http://www.31xiaoshuo.com")
    spider.save_data()
```

### 面向对象设计模式

**面向对象设计原则**

- 单一职责原则 （**S**RP）- 一个类只做该做的事情（类的设计要高内聚）
- 开闭原则 （**O**CP）- 软件实体应该对扩展开发对修改关闭
- 依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
- 里氏替换原则（**L**SP） - 任何时候可以用子类对象替换掉父类对象
- 接口隔离原则（**I**SP）- 接口要小而专不要大而全（Python中没有接口的概念）
- 合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
- 最少知识原则（迪米特法则，Lo**D**）- 不要给没有必然联系的对象发消息

**GoF设计模式**

- 创建型模式：单例、工厂、建造者、原型
- 结构型模式：适配器、门面（外观）、代理
- 行为型模式：迭代器、观察者、状态、策略

**1.工厂模式**

```python
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("{}岁的{}正在向我们走来".format(self.age, self.name))

    def relax(self):
        print("{}岁的{}正在休息".format(self.age, self.name))


class Woman(Person):
    def __init__(self, name, age):
        super(Woman, self).__init__(name, age)
        self.sex = "woman"

    def relax(self):
        super(Woman, self).relax()
        print("她的休息方式是追偶像剧")


class Man(Person):
    def __init__(self, name, age):
        super(Man, self).__init__(name, age)
        self.sex = "man"

    def relax(self):
        super(Man, self).relax()
        print("他休息的方式是在泡茶")


class Boy(Person):
    def __init__(self, name, age):
        super(Boy, self).__init__(name, age)
        self.sex = "man"

    def relax(self):
        super(Boy, self).relax()
        print("他休息的方式是打游戏")


class Girl(Person):
    def __init__(self, name, age):
        super(Girl, self).__init__(name, age)
        self.sex = "woman"

    def relax(self):
        super(Girl, self).relax()
        print("她的休息方式是玩洋娃娃")


class Factory:
    @staticmethod
    def produce(obj_kind, name, age):
        selector = {"W": Woman(name, age), "M": Man(name, age),
                   "B": Boy(name, age), "G": Girl(name, age)}
        return selector[obj_kind]


if __name__ == "__main__":
    for i in [("W", "lyf", 30), ("M", "ldh", 45), ("B", "bjt", 25), ("G", "zjm", 20)]:
        Person = Factory.produce(i[0], i[1], (i[2]))
        Person.walk()
        Person.relax()
        print("{0:-^20}".format("分割线"))
```



# Python进阶语法笔记

## 文件操作与异常

### 文件操作

文件的打开与关闭

```python
# 这会在这个文件目录下创建文件
# 如果这个文件不存在就新建
# 存在的话会覆盖

f = open('test.txt','w')
# 这里面的w是'写'
# 即：有w，r，wb，rb等等，w为写，r为读，wb为以二进制写入，rb为以二进制来读
# w，r一个也没写时，默认为r读
f.close()  #关闭文件
```

文件的写入与读取

```python
# 文件的写入
f = open("test.txt","w")
f.write('hello world!')   # 将字符串写入文件中
f.close()   # 养成好习惯：有文件关闭的语句

# 更保险的写入
with open("test.txt","w") as fp:
  fp.write('hello world!')   # 使用with结构会自动打开文件和完成操作之后关闭文件

# 读取操作
f = open("test.txt","w")
f.write('hello world!')   # 将字符串写入文件中
f.close()

f = open("test.txt","r")   # 只读模式
content = f.read(5)   # 读前五个字节
print(content)

content = f.read(6)   # 读从第五开始的后面六个
print(content)   # 这之中，要知道指针的概念，读几个就移动几个              
f.close()

# 更快的读取
f = open("test.txt","r")   # 只读模式
content = f.readlines()
print(content)
f.close()

# 一行一行的读
f = open("test.txt","r")
content = f.readline()
print("1:%s"%content)

content = f.readline()
print("2:%s"%content)
f.close()
```

### os库

```python
# os库基本介绍

# os库之路径操作
'''
  os.path子库以path为入口，用于操作和处理文件路径
  import os.path
  import os.path as op

  相关函数(联想英文单词意思)：
      os.path.abspath(path):返回path在当前系统中的绝对路径 #仅对同目录下文件有效
          os.path.abspath("file.txt")
          'C:\\Users\\Tian Song\\Pyhon36-32\\file.text'
      os.path.normpath(path):归一化path的表示形式，统一用\\分隔路径
          os.path.normpath("D://PYE//file.txt")
          'D:\\PYE\\file.txt'
      os.path.relpath(path):返回当前程序与文件之间的相对路径
          os.path.relpath("C://PYE//file.txt")
          '..\\..\\..\\..\\..\\..\\PYE\\file.txt'
      os.path.dirname(path):返回path中的目录名称
          os.path.dirname("D://PYE//file.txt")
          'D://PYE'
      os.path.basename(path):返回path中最后的文件名称
          os.path.basename("D://PYE//file.txt")
          'file.txt'
      os.path.join(path,*paths):组合path与paths，返回一个路径字符串
          os.path.join("D:/","PYE/file.txt")
          "D:/PYE/file.txt"
      os.path.exists(path):判断path对应文件或目录是否存在，从而返回True或False
          os.path.exists("D://PYE//file.txt")
          False
      os.path.isfile(path):判断path所对应的path是否为已存在的文件，返回True或False
          os.path,isfile("D://PYE//file.txt")
          True
      os.path.isdir(path):判断所对应的path是否为已存在的目录，返回True或False
          os.path.isdir("D://PYE//file.txt")
          False
      os.path.getatime(path):返回path对应文件或目录上一次的访问时间
          os.path.getatime("D://PYE//file.txt")
          ......
      os.path.getmtime(path):返回path对应文件或目录最近一次的修改时间
          os.path.getmtime("D://PYE//file.txt")
          ......
      os.path.getctime(path):返回path对应文件或目录的创建时间
          os.path.getctime("D://PYE//file.txt")
          ......
      os.path.size(path):返回path对应文件的大小，以字节为单位
          os.path.size("D://PYE//file.txt")
          ......
'''

# os库之进程管理
  # 进程管理指的是：使用我们编写的Python程序去调用其他的外部程序
'''
进程管理:
    os.system(command)
    -执行程序或命令command
    -在windows系统中，返回值为cmd的调用返回信息
        例如:调用计算机中的计算器程序
          import os 
          os.system("C:\\Windows\\System32\\calc.exe")-调用计算器程序
          并且如果调用成功会返回一个0，表明程序运行成功
    
        例如:调用计算机中的画图程序，并且指定一个图片让他默认打开
          import os 
          os.system("C:\\Windows\\System32\\mspaint.exe \ D:\\PYECourse\\grwordcloud.png)
          调用成功会返回一个0
'''

# os库之环境参数
  # 环境参数指的是获取或改变操作系统中的环境信息
'''
环境参数(获取或改变系统环境信息):
    os.chdir(path):修改当前程序操作的路径
        os.chdir("D:")--将程序的路径修改问D:下
    os.getcwd(path):返回程序的当前路径
        os.getcwd()
        如果执行了上一个代码，那么会返回'D:\\'
    os.getlogin():获得当前系统登录的用户名称
        os.getlogin()
        '回到古代见李白'
    os.cpu_count():获得当前系统的CPU数量
        os.cpu_count()
    os.urandom(n):获得n个字节长度的随机字符串，通常用于加解密运算
        os..urandom(10)
        b'\xd8|\xfb\x82\xfb[m\r\x822'
'''
```

### 异常

为了防止在程序运行当中，程序发生意外报错引发中断(崩溃)，引入错误与异常检查

```python
# 简单粗暴型直接捕获所有的异常
try:
    pass
except Exception as result:
    pass
```

## Python数据存储

### 存储为txt

```python
# 1.存储为文本文件(只是其中一种存储方式)

with open('./文件名','w',encoding='utf-8') as fp:
        fp.write('需要存储的数据')
        #......的操作
```

### 存储为csv

```python
# 2.存储为csv文件

# 写入操作
import csv
with open('text.csv','w',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)     
    writer.writerow()
    writer.writerows()

# 读取操作
with open('text.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
    print(row)
```

### 存储为json

```python
# 3.存储为json文件

# 写入操作
with open('test.json','w') as jsonfile:
    json.dump(jsonfile,data)
    
# 读取操作
with open('test.json') as jsonfile:
    json.loads(jsonfile)
```

### Py Sqlite3

````python
**1和2可用sqlite可视化管理工具来手动创建**

```
sqlite执行流程:
	1.获取连接
	2.打开游标
	3.执行sql语句（增删改查）
	4.提交数据
	5.关闭游标
	6.关闭数据库
```




# 1.连接数据库

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# 创建游标
cursor = conn.cursor()
# 关闭游标
cursor.close()
# 提交事物
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()




# 2.创建表

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# 创建表
sql = 'CREATE TABLE Student(id integer PRIMARY KEY autoincrement, Name  varchar(30), Age integer)'
cursor.execute(sql)

# 提交事物
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()




# 3.插入数据

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# 插入数据 e1 （insert into 表名(列1，列2，列3,...) values(?,?,?,...)）
sql = "INSERT INTO Student(Name, Age) VALUES(\'lucy\', 22)"
cursor.execute(sql)

# 插入数据 e2
data = ('jack', 21) # 数据需要为元组类型来一一对应
sql = "INSERT INTO Student(Name, Age) VALUES(?, ?)"
cursor.execute(sql, data)

# 提交事物
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()




# 4.插入多条数据

scroce_list = [('Jack',90,70),('Keye',90,60),
               ('Peac',70,70),('Quot',80,70),
               ('Iooo',70,80),('Lili',70,90),]
# 连接数据库
conn = sqlite.connect("test.db")

# 创建游标
cur = conn.cursor()

# 执行sql语句
sql = "insert into test(stu_name,math_scroce,_chinese_scroce) values=(?,?,?)"
cur.excutemany(sql,scroce_list) #插入多条数据需要使用excutemany函数

# 提交数据
conn.commit()

# 关闭游标
cur.close()

# 关闭数据库
conn.close()

# 验证是否插入成功，大于0即成功
print(cur.rowcount)




# 5.更新记录

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# update 表名 set 列名=?... where 条件 ->在这里条件就是指定id=3的那一行的数据
cursor.execute("UPDATE Student SET name = ? where id = ?",("lily","3"))

# 提交事物
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()




# 6.删除数据

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# delete from 表名 where 列=?
cursor.execute("delete from Student where id=?",("1",)) # 逗号不能省，元组元素只有一个的时候一定要加逗号,将删除lucy

# 提交事物
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()




# 7.查询数据

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# 查询数据 e1 sql语句:select * from 表名 where 列名=?
sql = "select * from Student"
values = cursor.execute(sql)
for i in values:
    print(i)

# 查询数据 e2
sql = "select * from Student where id=?"
values = cursor.execute(sql, (1,))
for i in values:
    print('id:', i[0])
    print('name:', i[1])
    print('age:', i[2])

# 提交事物
conn.commit()   # 查询数据可以不写这一行代码不需要提交数据

# 关闭游标
cursor.close()

# 关闭连接
conn.close()




# 8.删除表

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# 删除表格Student
cursor.execute("DROP TABLE Student")

# 提交事物
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()

````

### PyMongodb

```
#3.利用MongoDB数据库进行存储

PyMongo的安装:pip install pymong
1.连接数据库：
import pymongo
client = pymongo.MongoClient(host="localhost",port=27017)
等价于 client = MongoClient("mongo://localhost:27017/)

2.操作数据库：

1.创建一个数据库:
    db = client.test == db = client['test']

2.生成集合集合(collection)对象:
    collection = db.students == collection = db['students']
    注意MongoDB可以建立多个数据库,而数据库又可以生成多个集合...

3.调用collection的insert方法即可插入数据:
    insert_one:
        student = {
            'id':'123456'
        }
        result = collection.insert_one(student)
    inset_many:
        注意:多条数据的插入需要以列表来传递
        student1 = {
            'id':123456,
            'id':456789,
            'name':'lxh'
        }
        student2 = {
            'id':654321,
            'id':987654,
            'name':'lxx'
        }
        student_list = [student1,student2]
        result = collection.insert_many(student_list)

    用这种最新的插入方法可以取出其ObjectId值:print(result.inserted_ids)

4.查询:
  利用find_one或find方法进行查询:
    find_one(拿来查询有无某个数据):
        result = collection.find_one({'id':'123456'})
        print(type(result))
        print(result)
        也可以根据ObjectId来查询

        #find_one查询得到的是单个结果
    find(拿来查找有无这一部分的数据):
        results = collection.find({'id':123456})
        print(results)
        for result in results:
            print(result)

    如果要查询大于123456的数据:results = collection.find({'id':{'$gt':123456}})
        results = collection.find({'id':{'$gt':123456}})
        for result in results:
            print(result)
    $lt--小于         {'age':{'$lt':20}}        表示age大于20的...
    $gt--大于         {'age':{'$gt':20}}        表示age小于20的...
    $lte--小于或等于   {'age':{'$lte':20}}       表示age大于或等于20的...
    $gte--大于或等于   {'age':{'$gte':20}}       表示age小于或等于20的...
    $ne--不等于       {'age':{' $ne':20}}       表示age不等于20的...
    $in--在范围内     {'age':{'$in':[20,23]}}    表示age在20,23这个范围的
    $nin--不在范围内   {'age':{'$lt':[20,23]}}   表示age不在这个范围的

  正则匹配查询:$regex来指定正则匹配
    results = collection.find({'$regex':'M.*'})
    查找以M为开头的字符串

    $regex--匹配正则表达式
    $exists--属性是否存在 {'name':{'$exists':True}} name属性存在
    $type--类型判断
    $mod--数字模操作
    $text--文字查询 {'$text':{'$search:'Mike'}} text类型的属性中包含Mike字符串
    $where--高级条件查询

5.计数:调用count方法统计查询结果有多少条数据
    count = collection.find().count()
    print(count)

    统计符合某个条件的数据
    count = collection.find({'age':20}).count()
    print(count)

6.排序:排序时可以调用sort方法,并在其中传入排序的字段及升降序标志
    升序
    result = collection.find().sort('id',pymongo.ASCENDING)
    print([result['name']] for result in results)
    降序
    result = collection.find().sort('id',pymongo.DESCENDING)
    print([result['name']] for result in results)

7.偏移:skip(),limit()

8.更新:update_one  update_many

9.删除:delete_one  delete_many

其他操作:
    find_one_and_delete 查找后删除
    find_one_and_replace 替换
    find_one_and_update 更新操作
对索引进行操作相关方法有:
    creat_index
    creat_indexes
    drop_index
```



## Python的高级特性

### 迭代器

到目前为止，您可能已经注意到大多数容器对象都可以使用 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

这种访问风格清晰、简洁又方便。 迭代器的使用非常普遍并使得 Python 成为一个统一的整体。 在幕后，[`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句会在容器对象上调用 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter)。 该函数返回一个定义了 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的迭代器对象，此方法将逐一访问容器中的元素。 当元素用尽时，[`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 将引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常来通知终止 `for` 循环。 你可以使用 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next) 内置函数来调用 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法；这个例子显示了它的运作方式:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

看过迭代器协议的幕后机制，给你的类添加迭代器行为就很容易了。 定义一个 `__iter__()` 方法来返回一个带有 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法的对象。 如果类已定义了 `__next__()`，则 `__iter__()` 可以简单地返回 `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
        

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

### 生成器

[生成器](https://docs.python.org/zh-cn/3/glossary.html#term-generator) 是一个用于创建迭代器的简单而强大的工具。 它们的写法类似于标准的函数，但当它们要返回数据时会使用 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 语句。 每次在生成器上调用 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next) 时，它会从上次离开的位置恢复执行（它会记住上次执行语句时的所有数据值）。 一个显示如何非常容易地创建生成器的示例如下:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        

>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

可以用生成器来完成的操作同样可以用前一节所描述的基于类的迭代器来完成。 但生成器的写法更为紧凑，因为它会自动创建 `__iter__()` 和 [`__next__()`](https://docs.python.org/zh-cn/3/reference/expressions.html#generator.__next__) 方法。

另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。 这使得该函数相比使用 `self.index` 和 `self.data` 这种实例变量的方式更易编写且更为清晰。

除了会自动创建方法和保存程序状态，当生成器终结时，它们还会自动引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration)。 这些特性结合在一起，使得创建迭代器能与编写常规函数一样容易。

### 上下文管理器

```python
'''
上下文管理器

什么是上下文？其实我们可以简单地把它理解成环境。
从一篇文章中抽出一句话，让你来理解，我们会说这是断章取义。
为什么？因为我们压根就没考虑到这句话的上下文是什么。
编程中的上下文也与此类似，比如『进程上下文』，
指的是一个进程在执行的时候，CPU 的所有寄存器中的值、进程的状态以及堆栈上的内容等，
当系统需要切换到其他进程时，系统会保留当前进程的上下文，也就是运行时的环境，以便再次执行该进程。

迭代器有迭代器协议（Iterator Protocol），上下文管理器（Context manager）也有上下文管理协议（Context Management Protocol）。

上下文管理器协议，是指要实现对象的 __enter__() 和 __exit__() 方法。
上下文管理器也就是支持上下文管理器协议的对象，也就是实现了 __enter__() 和 __exit__() 方法。
这里先构造一个简单的上下文管理器的例子，以理解 __enter__() 和 __exit__() 方法。

from math import sqrt, pow

class Point(object):
    def __init__(self, x, y):
        print 'initialize x and y'
        self.x, self.y = x, y

    def __enter__(self):
        print "Entering context"
        return self

    def __exit__(self, type, value, traceback):
        print "Exiting context"

    def get_distance(self):
        distance = sqrt(pow(self.x, 2) + pow(self.y, 2))
        return distance
上面的代码定义了一个 Point 类，并实现了 __enter__() 和 __exit__() 方法，我们还定义了 get_distance 方法，用于返回点到原点的距离。

通常，我们使用 with 语句调用上下文管理器：

with Point(3, 4) as pt:
    print 'distance: ', pt.get_distance()

# output
initialize x and y   # 调用了 __init__ 方法
Entering context     # 调用了 __enter__ 方法
distance:  5.0       # 调用了 get_distance 方法
Exiting context      # 调用了 __exit__ 方法
上面的 with 语句执行过程如下：

Point(3, 4) 生成了一个上下文管理器；
调用上下文管理器的 __enter__() 方法，并将 __enter__() 方法的返回值赋给 as 字句中的变量 pt;
执行语句体（指 with 语句包裹起来的代码块）内容，输出 distance；
不管执行过程中是否发生异常，都执行上下文管理器的 __exit__() 方法。__exit__() 方法负责执行『清理』工作，如释放资源，关闭文件等。如果执行过程没有出现异常，或者语句体中执行了语句 break/continue/return，则以 None 作为参数调用 __exit__(None, None, None) ；如果执行过程中出现异常，则使用 sys.exc_info 得到的异常信息为参数调用 __exit__(exc_type, exc_value, exc_traceback)；
出现异常时，如果 __exit__(type, value, traceback) 返回 False 或 None，则会重新抛出异常，让 with 之外的语句逻辑来处理异常；如果返回 True，则忽略异常，不再对异常进行处理；
上面的 with 语句执行过程没有出现异常，我们再来看出现异常的情形：

with Point(3, 4) as pt:
    pt.get_length()        # 访问了对象不存在的方法

# output
initialize x and y
Entering context
Exiting context
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-216-ab4a0e6b6b4a> in <module>()
      1 with Point(3, 4) as pt:
----> 2     pt.get_length()

AttributeError: 'Point' object has no attribute 'get_length'
在我们的例子中，__exit__ 方法返回的是 None（如果没有 return 语句那么方法会返回 None）。因此，with 语句抛出了那个异常。我们对 __exit__ 方法做一些改动，让它返回 True。

from math import sqrt, pow

class Point(object):
    def __init__(self, x, y):
        print 'initialize x and y'
        self.x, self.y = x, y

    def __enter__(self):
        print "Entering context"
        return self

    def __exit__(self, type, value, traceback):
        print "Exception has been handled"
        print "Exiting context"
        return True

    def get_distance(self):
        distance = sqrt(pow(self.x, 2) + pow(self.y,2 ))
        return distance

with Point(3, 4) as pt:
    pt.get_length()      # 访问了对象不存在的方法

# output
initialize x and y
Entering context
Exception has been handled
Exiting context
可以看到，由于 __exit__ 方法返回了 True，因此没有异常会被 with 语句抛出。

内建对象使用 with 语句

除了自定义上下文管理器，Python 中也提供了一些内置对象，可直接用于 with 语句中，比如最常见的文件操作。

传统的文件操作经常使用 try/finally 的方式，比如：

file = open('somefile', 'r')
try:
    for line in file:
        print line
finally:
    file.close()     # 确保关闭文件
将上面的代码改用 with 语句：

with open('somefile', 'r') as file:
    for line in file:
        print line
可以看到，通过使用 with，代码变得很简洁，而且即使处理过程发生异常，with 语句也会确保我们的文件被关闭。

contextlib 模块

除了在类中定义 __enter__ 和 __exit__ 方法来实现上下文管理器，我们还可以通过生成器函数（也就是带有 yield 的函数）结合装饰器来实现上下文管理器，Python 中自带的 contextlib 模块就是做这个的。

contextlib 模块提供了三个对象：装饰器 contextmanager、函数 nested 和上下文管理器 closing。其中，contextmanager 是一个装饰器，用于装饰生成器函数，并返回一个上下文管理器。需要注意的是，被装饰的生成器函数只能产生一个值，否则会产生 RuntimeError 异常。

下面我们看一个简单的例子：

from contextlib import contextmanager

@contextmanager
def point(x, y):
    print 'before yield'
    yield x * x + y * y
    print 'after yield'

with point(3, 4) as value:
    print 'value is: %s' % value

# output
before yield
value is: 25
after yield
可以看到，yield 产生的值赋给了 as 子句中的 value 变量。

另外，需要强调的是，虽然通过使用 contextmanager 装饰器，我们可以不必再编写 __enter__ 和 __exit__ 方法，但是『获取』和『清理』资源的操作仍需要我们自己编写：『获取』资源的操作定义在 yield 语句之前，『释放』资源的操作定义在 yield 语句之后。

小结

上下文管理器是支持上下文管理协议的对象，也就是实现了 __enter__ 和 __exit__ 方法。
通常，我们使用 with 语句调用上下文管理器。with 语句尤其适用于对资源进行访问的场景，确保执行过程中出现异常情况时也可以对资源进行回收，比如自动关闭文件等。
__enter__ 方法在 with 语句体执行前调用，with 语句将该方法的返回值赋给 as 字句中的变量，如果有 as 字句的话。
__exit__ 方法在退出运行时上下文时被调用，它负责执行『清理』工作，比如关闭文件，释放资源等。如果退出时没有发生异常，则 __exit__ 的三个参数，即 type, value 和 traceback 都为 None。如果发生异常，返回 True 表示不处理异常，否则会在退出该方法后重新抛出异常以由 with 语句之外的代码逻辑进行处理。
'''
```

## 多线程与多进程

### 多线程

```python
# 多线程
    #为什么使用多线程?
        #--->进程是分配资源的最小单位，一旦创建一个进程就会分配一定的资源
        #线程是程序执行的最小单位,实际上进程只负责分配资源，而利用这些资源执行程序的是线程，也就是说进程是线程的容器,
          #一个进程中最少有一个线程来负责执行程序,同时线程自己不拥有系统资源，只需要一点儿在运行中必不可少的资源,
          #但它可与同属一个进程的其他线程共享进程所拥有的全部资源,就像通过QQ软件(一个进程)打开两个窗口(两个线程)跟两个人聊天一样,
          #实现多任务的同时也节省了资源

# 多线程的作用:
'''
例如:
def func1():
    print("任务1")

def func2():
    print("任务2")

func1()
func2()

当运行程序之后，在进程中默认会有一个线程用来执行程序,这个线程称之为主线程
主线程会按照顺序去先执行func1,在执行func2

而多线程:在进程中创建一个新的线程，这个线程称之为子线程
此时,主线程执行func1，子线程执行func2    (它们是同时执行)
'''


# 多线程完成多任务
    #线程的创建步骤
'''
    1.导入线程模块:import threading
    2.通过现场类创建线程对象:线程对象 = threading.Thread(target=任务名)
        参数:
        #target执行的目标任务，这里指的是函数名
        #name进程名，一般不用设置
        #group进程组，目前只能使用None
    3.启动线程执行任务:线程对象.start()
'''
import threading
import time

def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(1)
# 跳舞
def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(1)
    res = "我"
    return res

if __name__ == "__main__":

    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()




# 线程执行带有参数的进程
# args:以元组的方式给执行任务传参(只能有一个元组，按顺序传参)
'''
    import threading
    import time
    #唱歌
    def sing(num):
        for i in range(num):
            print("唱歌...")
            time.sleep(1)
    #跳舞
    def dance(num):
        for i in range(num):
            print("跳舞...")
            time.sleep(1)

    if __name__ == "__main__": #没用这个语句就报错了，以后记得使用--->这个是主进程入口==主程序入口

        sing_thread = threading.Thread(target=sing,args=(3,))
        dance_thread = threading.Thread(target=dance,args=(3,))

        sing_thread.start()
        dance_thread.start()
'''
# kwargs:以字典方式给执行任务传参(在传入参数的时候只需要key值与形参一样，不需要按顺序)
'''
    import threading
    import time
    # 唱歌
    def sing(num):
        for i in range(num):
            print("唱歌...")
            time.sleep(1)
    # 跳舞
    def dance(num):
        for i in range(num):
            print("跳舞...")
            time.sleep(1)

    if __name__ == "__main__":   # 没用这个语句就报错了，以后记得使用

        sing_thread = threading.Thread(target=sing,kwargs={"num":3})
        dance_thread = threading.Thread(target=dance,kwargs={"num":3})

        sing_thread.start()
        dance_thread.start()
'''


# 主线程和子线程的结束顺序:主线程会等待所有子线程执行结束之后才会结束
# 设置为主线程关闭,子进程会自动销毁---子进程守护模式
'''
设置守护主线程:
------法一:在每个子线程对象创建的后面,再写上,子线程对象.daemon = True 那么这个子线程就会守护主线程
------法二:在子线程启动之前,写上,子线程对象.thread.setDaemon(True)
------在主线程直接退出的时候，子线程如果还在运行，那么直接销毁
'''
# 线程之间的执行是无序的
```

### 多进程

```python
# 多任务介绍
    # 多任务是指在同一时间内执行多个任务
        # 例如:电脑在下载文件的时候同时下载多个文件，又比如同时打开很多软件......

    # 并发:在一段时间内交替去执行多个任务
        #例如：对于单核cpu处理多任务，操作系统轮流让各个人物交替执行

    # 并行:在一段时间内真正的同时一起执行多个任务
        # 对于多核cpu处理多任务，操作系统会给cpu的每个内核安排一个执行的任务，多个内核是真正的一起同时执行多个任务


# 进程介绍
    # 进程是资源分配的最小单位，它是操作系统进行资源分配和调度运行的基本单位，通俗理解:一个正在运行的程序就是一个进程，例如正在运行的qq，微信等，它们都是一个个的进程

def func1():
    print("1")

def func2():
    print("2")

# func1()
# func2()
'''
上述程序在运行之后,程序会默认创建一个进程，这个默认创建的进程我们称之为主进程(先执行func1，在执行func2)

而使用多进程则是:程序运行后又创建了一个进程，这个新创建的进程我们称之为子进程(主进程执行func1，子进程执行func2)
这样就达到了同时执行func1和func2了
'''

# 多进程完成多任务
    # 进程的创建步骤:
'''
1.导入进程包:
import multiprocessing

2.通过进程类创建进程对象:
进程对象=multiprocessing.Process(target=任务名)
    参数:
        #target执行的目标任务，这里指的是函数名
        #name进程名，一般不用设置
        #group进程组，目前只能使用None
3.启动进程执行任务:
进程对象.start()
'''
# 例如:
'''
import multiprocessing
import time
# 唱歌
def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(1)
# 跳舞
def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(1)

if __name__ == "__main__": #没用这个语句就报错了，以后记得使用

    sing_processing = multiprocessing.Process(target=sing)
    dance_processing = multiprocessing.Process(target=dance)

    sing_processing.start()
    dance_processing.start()
'''

# 进程执行带有参数的进程
    # args:以元组的方式给执行任务传参(只能有一个元组，按顺序传参)
'''
    import multiprocessing
    import time
    # 唱歌
    def sing(num):
        for i in range(num):
            print("唱歌...")
            time.sleep(1)
    # 跳舞
    def dance(num):
        for i in range(num):
            print("跳舞...")
            time.sleep(1)
    
    if __name__ == "__main__":   # 没用这个语句就报错了，以后记得使用--->这个是主进程入口==主程序入口
    
        sing_processing = multiprocessing.Process(target=sing,args=(3,))
        dance_processing = multiprocessing.Process(target=dance,args=(3,))
    
        sing_processing.start()
        dance_processing.start()
'''
    # kwargs:以字典方式给执行任务传参(在传入参数的时候只需要key值与形参一样，不需要按顺序)
'''
    import multiprocessing
    import time
    # 唱歌
    def sing(num):
        for i in range(num):
            print("唱歌...")
            time.sleep(1)
    # 跳舞
    def dance(num):
        for i in range(num):
            print("跳舞...")
            time.sleep(1)

    if __name__ == "__main__": #没用这个语句就报错了，以后记得使用

        sing_processing = multiprocessing.Process(target=sing,kwargs={"num":3})
        dance_processing = multiprocessing.Process(target=dance,kwargs={"num":3})

        sing_processing.start()
        dance_processing.start()
'''


# 获取进程编号
    # 第一种获取进程编号的方法:
        # 获取当前进程编号:
            # os.getpid()

    # 第二种获取进程编号的方法:
        # 获取当前父进程的编号:
            #nos.getppid()


import multiprocessing
import time
import os

# 唱歌
def sing(num):
    print("获取当前唱歌进程的编号:",os.getpid())
    print("获取当前唱歌主进程的编号:", os.getppid())
    for i in range(num):
        print("唱歌...")
        time.sleep(1)


# 跳舞
def dance(num):
    print("获取当前跳舞进程的编号:", os.getpid())
    print("获取当前跳舞主进程的编号:", os.getppid())
    for i in range(num):
        print("跳舞...")
        time.sleep(1)

# 主进程
if __name__ == "__main__":  # 没用这个语句就报错了，以后记得使用
    print("主进程的pid:",os.getpid())
    # 创建子进程对象并指定执行的任务名
    sing_processing = multiprocessing.Process(target=sing, args=(3,))
    dance_processing = multiprocessing.Process(target=dance, args=(3,))

    # 启动子进程并执行任务
    sing_processing.start()
    dance_processing.start()


# 进程的注意点
'''
主进程会等待所有子进程执行结束再结束:想想QQ
------因此,在创建多任务的时候一定要有主进程,然后在创建多个子进程

设置守护主进程:
------在每个子进程对象创建的后面,再写上,子进程对象.daemon = True 那么这个子进程就会守护主进程  
------在主进程直接退出的时候，子进程如果还在运行，那么直接销毁
'''


#实例:高并发的文件copy器
```

### 它们的对比

```
进程和线程对比

进程优缺点:
    优点:可以用多核
    缺点:资源开销大

线程优缺点:
    优点:资源开销小
    缺点:不能使用多核
```

## Python异步编程

### Asyncio

```
异步编程asyncio:

1.协程：
	协程也可以被称为微线程，是一种用户动态的上下文切换技术，简而言之，其实是通过一个线程实现代码块相互切换执行，例如:

	def fuc1():
		print(1)
		...
		print(2)

	def fuc2():
		print(3)
		...
		print(4)

	func1()
	func2()

	当是单线程时...
	当是协程时，可以实现运行这两个函数之间来回切换，先运行func1以下然后切换到func2在运行一下...依次类推！

	实现协程有这么几个方法:
		greenlet 早期模块
		yield关键字
		asyncio装饰器(py3.4后可用)
		async,await关键字(py3.5后可用)[官方推荐]


	* asyncio示例代码(后续会对这里面的代码逐一讲解):

		import asyncio

		#加上这个装饰器这个函数就变成了协程函数
		@asyncio.coroutine 
		def func1():
			print(1)
			yield from asyncio.sleep(2) #遇到IO耗时操作，自动切换到tasks中的其他任务
			print(2)

		#加上这个装饰器这个函数就变成了协程函数
		@asyncio.coroutine 
		def func2():
			print(3)
			yield from asyncio.sleep(2) #遇到IO耗时操作，自动切换到tasks中的其他任务
			print(4)


		#定义一任务列表，因为asyncio本质上是单线程快速在任务之间切换执行，因此一开始asyncio会随机的选择一个任务进行运行，当在此任务中遇到IO耗时操作时会自动切换到任务列表中的另一任务继续执行...
		tasks = [
			asyncio.ensure_future( func1() ),
			asyncio.ensure_future( func2() )
		]
	
		#asyncio运行事件列表，运行机制如上
		loop = asyncio.get_event_loop() #生成一个事件循环
		loop.run_until_complete(asyncio.wait(tasks)) #将任务放到任务列表

	通过asyncio能实现，遇到IO可以自动切换，这就是它的牛逼之处！

	试想，将上述的sleep IO阻塞换成网络请求（例如在下载图片），它不会去等待下载完成，而是自动发起下一次请求...

	* async & await关键字:

		将上述代码稍加修改（python官方为了代码更加简洁）:

		import asyncio

		async def func1():
			print(1)
			await from asyncio.sleep(2) 
			print(2)


		async def func2():
			print(3)
			await from asyncio.sleep(2) 
			print(4)


		tasks = [
			asyncio.ensure_future( func1() ),
			asyncio.ensure_future( func2() )
		]

		loop = asyncio.get_event_loop()
		loop.run_until_complete(asyncio.wait(tasks))

		将上述代码的装饰器删除，在def前面加上async关键字，yield关键字换成await关键字即可实现和上述代码一样的功能，它们本质和原理上是一样的！

	运行原理简述:


2.协程意义:
	在一个线程中如果遇到IO阻塞，线程不会傻等，而是利用等待的时间去做一些其他的任务。

	例如：去下载三张图片（网络IO）

	import aiohttp
	import asnycio

	async def fetch(session,url):
		print("发送请求:",url)
		async with session.get(url,verify=False) as response:
			content = await response.content.read()
			filename = url.rsplit('_')[-1]
			with open(filename,mode='wb') as fp:
				fp.write(content)

	async def main():
		async with aiohttp.ClientSession() as session:
			urls = [
				'图片网址1',
				'图片网址2',
				'图片网址3'
			]
			tasks = [asynico.creat_task(fetch(session,url)) for url in urls]

			await asyncio.wait(tasks)


	if __name__ == '__main__':
		asyncio.run(main())


	将爬取妹子图的那个爬虫改成协程的方式！
	...


3.异步编程:
	3.1.事件循环:
		理解为一个死循环，它会去检测和执行某些代码。

		这个死循环会去检测任务列表中任务的状态，如果为可执行的去执行，对目前不可执行的任务进行忽略，对已完成的任务进行删除

	3.2.快速上手:
		协程函数:定义函数的时候-> async def func()
			async def func():
				pass

		协程对象:执行 协程函数func()得到协程对象
			result = func() #定义协程对象(协程函数➕()变为协程对象)，函数并不会执行！

		注意:执行协程函数创建协程对象，函数内部代码不会执行

		那么如何运行协程函数内部代码呢？-> 用事件循环来执行:
			async def func():
				print('我可以执行啦！！！')

			result = func()

			#loop = asyncio.get_event_loop()
			#loop.run_until_complete(result)
			#上面两行是py3.5时的写法，现在的写法更简洁！
			asyncio.run(result) #python 3.7 以后，这一行即实现上述两行...

	3.3.await关键字:
		一般情况下await后面根一些可等待的对象 -> await + 可等待的对象(协程对象，Future，Task对象 -> 目前理解为IO等待)

		such as:

		示例1: -> 知道await为等 ---  
		import asyncio

		async def func():
			print('来啊')
			respone = await asyncio.sleep(2)
			print("结束:",response)

		asyncio.run( func() )


		示例2: -> 知道await后面可以根协程对象
		import asyncio

		async others():
			print("starts:")
			await asyncio.sleep(2)
			print("end")

			return "返回值"

		async func():
			print("执行协程函数内部代码:")

			response = await others()

			print("IO请求结束:"response)

		asyncio.run( func() )


		示例3: -> 知道协程函数中可以使用多个await
		import asyncio

		async def others():
		    print("starts:")
		    await asyncio.sleep(2)
		    print("end")

		    return "返回值"

		async def func():
		    print("执行协程函数内部代码:")

		    response1 = await others()

		    print("IO请求结束:",response1)

		    response2 = await others()

		    print("IO请求结束:",response2)

		asyncio.run( func() )

		await就是等待对象的值得到结果之后再继续往下走！

	3.4.Task对象:
		在事件循环中添加多个任务的。
		Tasks用于井发调度协程，通过 asyncio.create_task(协程对象) 的方式创建Task对象，这样可以让协程加入事件循环中等待被调度执行。除了使用 asyncio.create_task()函数以外，还可以用低层级的
		1oop.create_task()或ensure_future()函数。不建议手动实例化 Task 对象。
		
		注意：asyncio.create_task()函数在Python 3.7 中被加入。在Python 3.7 之前，可以改用低层级的asyncio.ensure_future()函数

		示例1:

		async def func()):
			print(1)
			await asyncio.sleep(2)
			print(2)
			return "返回債”
			
		async def main():
			print("main开始”）

			# 创建Task对象，将当前执行
			task1 = asyncio.create_task(func())
			task2 = asyncio.create_task(func())

			print("'main结束")
			# 当执行某协程遇到I0操作时，会自动化切换执行其他任务
			# 此处的awai t是等待相对应的协程全都执行完毕井获取结果
			ret1 = await task1
			ret2 = await task2

			print(ret1, ret2)

		asyncio.run( main() )


		示例2: -> 修改后

		async def func()):
			print(1)
			await asyncio.sleep(2)
			print(2)
			return "返回債”
			
		async def main():
			print("main开始”）

			tasks = [
				asyncio.create_task(func()),
				asyncio.create_task(func())
			]

			print("'main结束")
		
			done,pending = await asyncio.wait(tasks) / done.pending = await asyncio.wait(tasks.timeout=None)

			print(ret1, ret2)

		asyncio.run( main() )


		示例3:

		async def func()):
			print(1)
			await asyncio.sleep(2)
			print(2)
			return "返回債”

		tasks = [
				func(),
				func(),
			]

		done,pending = asyncio.run(asyncio.wait(tasks))

		Task对象就是帮助我们立即将我们的任务添加至事件循环中


	3.5.acyncio.Future对象:
		看视频，不常用！！！
		Task继承Future对象，Task对象内部await结果的处理时基于Future对象来的


	3.5.concurrent.futures.Future对象:
		看视频，不常用，扩充！！！使用线程池和进程chi实现异步时所需用到的对象！


	3.6.异步迭代器:
		看视频，不常用！！！


	3.7.异步上下文管理器：
		看视频，不常用！！！


4.uvloop:
	是asycio的事件循环的替代方案，其性能比asyncio的事件循环高很多
	当需要更高的性能时，将默认的事件循环设置为uvloop即可

	import asyncio
	import uvloop
	asyncio.set_event_loop_policy(uvloop.EventLoopPolicy()) #将默认的事件循环替换为uvloop
	#其他代码和之前无异

	...

	asyncio.run(...) #内部的事件循环会自动替换为uvloop


5.实战案例:



6.日常开发常用范式:
		#常用范式1:
		async def func()):
			print(1)
			await asyncio.sleep(2)
			print(2)
			return "返回債”
			
		async def main():
			print("main开始”）

			tasks = [
				asyncio.create_task(func()),
				asyncio.create_task(func())
			]

			print("'main结束")
		
			done,pending = await asyncio.wait(tasks)

			print(ret1, ret2)

		asyncio.run( main() )


		#常用范式2:
		import aiohttp
		import asnycio

		async def fetch(session,url):
			print("发送请求:",url)
			async with session.get(url,verify=False) as response:
				content = await response.content.read()
				filename = url.rsplit('_')[-1]
				with open(filename,mode='wb') as fp:
					fp.write(content)

		async def main():
			async with aiohttp.ClientSession() as session:
				urls = [
					'图片网址1',
					'图片网址2',
					'图片网址3'
				]
				tasks = [asynico.creat_task(fetch(session,url)) for url in urls]

				await asyncio.wait(tasks)

		if __name__ == '__main__':
			asyncio.run(main())

总结:掌握异步编程最大的意义就是用比较少的资源去做更多的事！！！
```



### 异步爬虫例子

```python
# asyncioSpiderPicUrls.py
import asyncio
import aiohttp

import requests
from lxml import etree
import os

async def detailFetch(session,detail_url):
    async with session.get(url=detail_url) as resp:
        detail_res = await resp.text()
        detail_tree = etree.HTML(detail_res)
        # 定位到目标图片地址
        src = detail_tree.xpath('//*[@id="big_preview"]/@src')[0]
        # 拼接出图片地址
        src_url = 'https:' + src
        with open('picurls.txt','a') as fp:
            fp.write(src_url)
            fp.write('\n')
        print(src_url)

async def fetch(session,url):
    async with session.get(url=url) as resp:
        html = await resp.text()
        tree = etree.HTML(html)
        # 定位图片地址列表
        span_list = tree.xpath('//*[@id="posts"]/div[2]/span')
        # 对图片地址元素列表里面的每一个元素进行定位与请求
        for span in span_list:
            try:
                # 定位到含有图片的网址
                href = span.xpath('./a/@href')[0]
                # 拼接为一个完整的含有图片的网址
                detail_url = 'https://anime-pictures.net' + href
                # 对此含有图片的网址进行请求
                await detailFetch(session,detail_url)

            except Exception as result:
                # print(result)
                pass

async def main():
    global i
    i = 1
    async with aiohttp.ClientSession(headers=heards) as session:
        urls = ['https://anime-pictures.net/pictures/view_posts/{}?lang=zh_CN'
                .format(i) for i in range(250,300)]

        tasks = [asyncio.create_task(fetch(session,url)) for url in urls]

        await asyncio.wait(tasks)


if __name__ == "__main__":

    # UA伪装
    heards = {
        'referer': 'https://anime-pictures.net/?lang=zh_CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

    asyncio.run(main())
```

```python
# asyncioSpider.py
import os
import asyncio
import aiohttp

def creat_counter():

    def increace():
        n = 0 # 计数器起始值，图片文件夹中的图片数
        while True:
            n = n + 1
            yield n
    ic = increace()

    def counter():
        return next(ic)

    return counter

async def fetch(session,url):
    i = counter_()
    async with session.get(url) as resp:
        content = await resp.read()
        print('正在下载第{}个图片'.format(i))
        with open('./动漫图片/'+str(i)+".jpg",'wb') as fp:
            fp.write(content)

async def main():
    async with aiohttp.ClientSession(headers=heards) as session:
        pic_urls = []

        with open('picurls.txt','r') as fp:
            for r in fp:
                pic_urls.append(r.strip())
            print(pic_urls)

        tasks = [asyncio.create_task(fetch(session,url)) for url in pic_urls]

        await asyncio.wait(tasks)

if __name__ == "__main__":
    counter_ = creat_counter()

    heards = {
        'referer': 'https://anime-pictures.net/?lang=zh_CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

    # 新建一个文件夹用来保存图片
    if not os.path.exists('./动漫图片/'):
        os.mkdir('./动漫图片/')

    asyncio.run(main())
```

# Python标准库



















