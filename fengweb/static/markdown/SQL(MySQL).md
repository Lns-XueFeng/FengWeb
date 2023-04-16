## SQL（MySQL）

本篇文档旨在记录SQL以及MySQL相关的概念与操作！

### 数据库

#### 命令行连接

```
mysql -u xuefeng -p
```

#### 操作数据库

```sql
# 显示数据库
show databases;
# 创建数据库
create database db_name;
# 删除数据库
drop database db_name;
# 使用数据库
use db_name;
```

### 数据类型

一个数据库的数据结构示例

| Field      | Type         | Null | Key  | Default | Extra          |
| ---------- | ------------ | ---- | ---- | ------- | -------------- |
| id         | bigint(20)   | NO   | PRI  | NULL    | auto_increment |
| create     | datatime     | YES  |      | NULL    |                |
| categoryId | bigint(20)   | YES  |      | NULL    |                |
| content    | longtext     | YES  |      | NULL    |                |
| title      | varchar(225) | YES  |      | NULL    |                |

MySQL 有三种主要数据类型

- 1.文本类
- 2.数字类
- 3.日期类

#### 文本类型

| 数据类型         | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| CHAR(size)       | 保存固定长度的字符串（可包含字母、数字以及特殊字符)。在括号中指定字符串的长度。最多255个字符 |
| VARCHAR(size)    | 保存可变长度的字符串（可包含字母、数字以及特殊字符)。在括号中指定字符串的最大长度。最多255个字符。 |
| TINYTEXT         | 存放最大长度为255个字符的字符串。                            |
| TEXT             | 存放最大长度为65,535个字符的字符串。                         |
| BLOB             | 用于 BLOBs(Binary Large oBjects)。存放最多65,535字节的数据。 |
| MEDIUMTEXT       | 存放最大长度为16,777,215个字符的字符串。                     |
| MEDIUMBLOB       | 用于 BLOBs (Binary Large oBjects)。存放最多16,777,215字节的数据。 |
| LONGTEXT         | 存放最大长度为4,294,967,295个字符的字符串。                  |
| LONGBLOB         | 用于 BLOBs (Binary Large oBjects)。存放最多4,294,967,295字节的数据。 |
| ENUM(x,y,z,etc.) | 允许你输入可能值的列表。可以在 ENUM 列表中列出最大65535个值。如果列表中不存在插入的值，则插入空值。注释:这些值是按照你输入的顺序存储的。可以按照此格式输入可能的值: ENUM('X','Y','Z') |
| SET              | 与 ENUM 类似，SET 最多只能包含64个列表项，不过 SET 可存储一个以上的值。 |

最常用文本数据类型：VARCHAR、TEXT、LONGTEXT

#### 数字类型

| 数据类型        | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| TINYINT(size)   | -128 到127常规。0到255无符号*。在括号中规定最大位数。        |
| SMALLINT(size)  | -32768到32767常规。0到65535无符号*。在括号中规定最大位数。   |
| MEDIUMINT(size) | -8388608到 8388607普通。0 to 16777215无符号*。在括号中规定最大位数。 |
| INT(size)       | -2147483648 到2147483647常规。0到4294967295无符号*。在括号中规定最大位数。 |
| BIGINT(size)    | -9223372036854775808到9223372036854775807常规。0到18446744073709551615无符号*。在括号中规定最大位数。 |
| FLOAT(size,d)   | 带有浮动小数点的小数字。在括号中规定最大位数。在 d 参数中规定小数点右侧的最大位数。 |
| DOUBLE(size,d)  | 带有浮动小数点的大数字。在括号中规定最大位数。在 d 参数中规定小数点右侧的最大位数。 |
| DECIMAL(size,d) | 作为字符串存储的 DOUBLE 类型，允许固定的小数点。             |

最常用数字数据类型：TINYINT、INT、BIGINT、DOUBLE

#### 日期类型

| DATE()      | 日期。格式: YYYY-MM-DD注释:支持的范围是从‘1000-01-01’到'9999-12-31' |
| ----------- | ------------------------------------------------------------ |
| DATETIME()  | *日期和时间的组合。格式: YYYY-MM-DD HH:MM:SS注释:支持的范围是从'1000-01-01 00:00:00’到 '9999-12-31 23:59:59' |
| TIMESTAMP() | *时间戳。TIMESTAMP 值使用Unix纪元('1970-01-01 00:00:00' UTC)至今的描述来存储。格式: YYYY-MM-DD HH:MM:SS注释:支持的范围是从‘1970-01-01 00:00:01'UTC到'2038-01-09 03:14:07' UTC |
| TIME()      | 时间。格式: HH:MM:SS 注释:支持的范围是从'-838:59:59'到 '838:59:59' |
| YEAR()      | 2位或4位格式的年。注释:4位格式所允许的值: 1901到 2155。2位格式所允许的值:70到69，表示从1970到2069。 |

最常用日期数据类型：DATETIME

### 各种表操作

#### 操作表

```sql
# 创建表
CREATE TABLE tb_name (
    id bigint(20) ,
    createTime datetime,
    ip varchar(255),
    mobile varchar(255),
    nickname varchar(255),
    passwd varchar(255),
    username varchar(255)，
    avatar varchar(255),
    brief text,
    job varchar(255),
    location varchar(255)，
    qq varchar(255),
    gender int(11)，
    city varchar(255),
    province varchar(255)
);

# 显示数据库中的表
show tables;

# 查看表的数据结构
describe tb_name;

# 删除表
drop table tb_name;
```

#### 修改列

```sql
# 增加列（属性）
# alter table [table_name] add [column_name] [data_type] [not null] [default ]
alter table tb_name add c1_name int(11) null;

# 删除列（属性）
# alter table [table_name] drop [column_name]
alter table tb_name drop c1_name;

# 修改表名
alter table tb_name rename new_tb_name;

# 修改列（属性）信息
# alter table [table_name] change [old_column_name] [new_column_name] [data_type]
alter table tb_name change c1_name c2_name;
alter table tb_name change c1_name c1_name text;
alter table tb_name change c1_name c2_name text;
```

#### 插入行

```sql
# 插入记录
# insert into [table_name] values(值1，值2...) 没指定列名就全部列都要添加
# insert into [table_name] (列1，列2...) values(值1，值2..) 指定列添加值
insert into tb_name values(10, "HelloWorld", 101);
insert into tb_name (c1_name, c2_name) values("HelloWorld", 101);
```

#### 更新行

```sql
# 更新记录
# update 表名 set 列名1=xxx,列名2=xxx...[where字句]
update tb_name set c1_name="HelloPython", c2_name=108;

# Update 警告！
# 在更新记录时要格外小心，基本上都要配合WHERE字句来进行更新记录
```

#### 删除行

```sql
# 删除记录
# delete from table_name where condition
delete from tb_name
where c1_name="HelloWorld" and c2_name="101";
```

#### 查看表

```sql
# 查看表中所有记录
select * from tb_name;

# 查看表中某列记录
select c1_name from tb_name;

# 查看表中多列记录
select c1_name, c2_name from tb_name;
```

### 组合查询

#### 检索数据

**1.检索单个列**

```sql
SELECT prod_name
FROM Products;
```

**2.检索多个列**

```sql
SELECT prod_id, prod_name, prod_price
FROM Products;
```

**3.检索所有列**

```sql
SELECT *
FROM Products;
```

**4.检索不同的值**

```sql
SELECT DISTINCT vend_id
FROM Products;
```

**5.限制结果数量**

```sql
SELECT prod_name
FROM Products
LIMIT 5;
```

```sql
SELECT prod_name
FROM Products
LIMIT 5 OFFSET 5;
```

#### 排序检索数据

**1.排序数据**

子句（clause）SQL语句由子句构成，有些子句是必需的，有些则是可选的。一个子句通常由一个关键字加上所提供的数据组成。子句的例子有我们在前一课看到的SELECT语句的FROM子句。

为了明确地排序用SELECT语句检索出的数据，可使用ORDER BY子句。ORDER BY子句取一个或多个列的名字，据此对输出进行排序。请看下面的例子：

```sql
SELECT prod_name
FROM Products
ORDER BY prod_name;
```

注意：ORDER BY子句的位置在指定一条ORDER BY子句时，应该保证它是SELECT语句中最后一条子句。如果它不是最后的子句，将会出错。

提示：通过非选择列进行排序通常，ORDER BY子句中使用的列将是为显示而选择的列。但是，实际上并不一定要这样，用非检索的列排序数据是完全合法的。

**2.按多个列排序**

下面的代码检索3个列，并按其中两个列对结果进行排序——首先按价格，然后按名称排序。

```sql
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price, prod_name;
```

**3.指定排序方向**

数据排序不限于升序排序（从A到Z），这只是默认的排序顺序。还可以使用ORDER BY子句进行降序（从Z到A）排序。为了进行降序排序，必须指定DESC关键字。

```sql
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price DESC;
```

```sql
SELECT prod_id, prod_price, prod_name
FROM Products
ORDER BY prod_price DESC, prod_name;
```

#### 过滤数据

**1.使用WHERE子句**

在SELECT语句中，数据根据WHERE子句中指定的搜索条件进行过滤。WHERE子句在表名（FROM子句）之后给出，如下所示：

```sql
SELECT prod_name, prod_price
FROM Products
WHERE prod_price = 3.49;
```

这条语句从products表中检索两个列，但不返回所有行，只返回prod_price值为3.49的行。

WHERE子句操作符如下：

| 操作符  | 说明 |
| ------- | ---- |
| =       |      |
| <>      |      |
| !=      |      |
| <       |      |
| <=      |      |
| !<      |      |
| >       |      |
| >=      |      |
| !>      |      |
| BETWEEN |      |
| IS NULL |      |

```sql
SELECT prod_name, prod_price
FROM Products
WHERE prod_price < 10;
```

```sql
SELECT prod_name, prod_price
FROM Products
WHERE prod_price <= 10;
```

```sql
SELECT vend_id, prod_name
FROM Products
WHERE vend_id <> 'DLL01';
```

```sql
SELECT vend_id, prod_name
FROM Products
WHERE vend_id != 'DLL01';
```

```sql
SELECT prod_name, prod_price
FROM Products
WHERE prod_price BETWEEN 5 AND 10;
```

NULL无值（no value），它与字段包含0、空字符串或仅仅包含空格不同。

确定值是否为NULL，不能简单地检查是否等于NULL。SELECT语句有一个特殊的WHERE子句，可用来检查具有NULL值的列。这个WHERE子句就是IS NULL子句。其语法如下：

```sql
SELECT prod_name
FROM Products
WHERE prod_price IS NULL;
```

#### 高级数据过滤

**1.组合WHERE子句**

为了进行更强的过滤控制，SQL允许给出多个WHERE子句。这些子句有两种使用方式，即以AND子句或OR子句的方式使用。

```sql
SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' AND prod_price <= 4;
```

此SQL语句检索由供应商DLL01制造且价格小于等于4美元的所有产品的名称和价格。这条SELECT语句中的WHERE子句包含两个条件，用AND关键字联结在一起。AND指示DBMS只返回满足所有给定条件的行。如果某个产品由供应商DLL01制造，但价格高于4美元，则不检索它。类似地，如果产品价格小于4美元，但不是由指定供应商制造的也不被检索。

```sql
SELECT prod_id, prod_price, prod_name
FROM Products
WHERE vend_id = 'DLL01' OR vend_id = 'BRS01';
```

此SQL语句检索由任一个指定供应商制造的所有产品的产品名和价格。OR操作符告诉DBMS匹配任一条件而不是同时匹配两个条件。如果这里使用的是AND操作符，则没有数据返回（因为会创建没有匹配行的WHERE子句）。

```sql
SELECT prod_name, prod_price
FROM Products
WHERE vend_id = 'DLL01' OR vend_id = 'BRS01'
    AND prod_price >= 10;
```

```sql
SELECT prod_name, prod_price
FROM Products
WHERE (vend_id = 'DLL01' OR vend_id = 'BRS01')
    AND prod_price >= 10;
```

**2.IN操作符**

IN操作符用来指定条件范围，范围中的每个条件都可以进行匹配。IN取一组由逗号分隔、括在圆括号中的合法值。下面的例子说明了这个操作符。

```sql
SELECT prod_name, prod_price
FROM Products
WHERE vend_id  IN ('DLL01','BRS01')
ORDER BY prod_name;
```

**3.NOT操作符**

WHERE子句中的NOT操作符有且只有一个功能，那就是否定其后所跟的任何条件。因为NOT从不单独使用（它总是与其他操作符一起使用），所以它的语法与其他操作符有所不同。NOT关键字可以用在要过滤的列前，而不仅是在其后。

下面的例子说明NOT的用法。为了列出除DLL01之外的所有供应商制造的产品，可编写如下的代码。

```sql
SELECT prod_name
FROM Products
WHERE NOT vend_id = 'DLL01'
ORDER BY prod_name;
```

这里的NOT否定跟在其后的条件，因此，DBMS不是匹配vend_id为DLL01，而是匹配非DLL01之外的所有东西。

为什么使用NOT？对于这里的这种简单的WHERE子句，使用NOT确实没有什么优势。但在更复杂的子句中，NOT是非常有用的。例如，在与IN操作符联合使用时，NOT可以非常简单地找出与条件列表不匹配的行。

#### 用通配符过滤

**1.LIKE操作符**

**百分号（%）通配符：**最常使用的通配符是百分号（%）。在搜索串中，%表示任何字符出现任意次数。例如，为了找出所有以词Fish起头的产品，可写以下的SELECT语句：

```sql
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE 'Fish%';
```

通配符可在搜索模式中的任意位置使用，并且可以使用多个通配符。下面的例子使用两个通配符，它们位于模式的两端：

```sql
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '%bean bag%';
```

通配符也可以出现在搜索模式的中间，虽然这样做不太有用。下面的例子找出以F起头、以y结尾的所有产品：

```sql
SELECT prod_name
FROM Products
WHERE prod_name LIKE 'F%y';
```

**2.下划线（_）通配符：**另一个有用的通配符是下划线（_）。下划线的用途与%一样，但它只匹配单个字符，而不是多个字符。

```sql
SELECT prod_id, prod_name
FROM Products
WHERE prod_name LIKE '__ inch teddy bear';
```

```sql
prod_id       prod_name
--------      --------------------
BR02           12 inch teddy bear
BR03           18 inch teddy bear
```

**3.方括号（[ ]）通配符：**方括号（[]）通配符用来指定一个字符集，它必须匹配指定位置（通配符的位置）的一个字符。

```sql
SELECT cust_contact
FROM Customers
WHERE cust_contact LIKE '[JM]%'
ORDER BY cust_contact;
```

```sql
cust_contact
-----------------
Jim Jones
John Smith
Michelle Green
```

此通配符可以用前缀字符^（脱字号）来否定。例如，下面的查询匹配以J和M之外的任意字符起头的任意联系人名（与前一个例子相反）：

```sql
SELECT cust_contact
FROM Customers
WHERE cust_contact LIKE '[^JM]%'
ORDER BY cust_contact;
```

当然，也可以使用NOT操作符得出类似的结果。^的唯一优点是在使用多个WHERE子句时可以简化语法：

```sql
SELECT cust_contact
FROM Customers
WHERE NOT cust_contact LIKE '[JM]%'
ORDER BY cust_contact;
```

#### 创建计算字段

**1.拼接字段：**将值联结到一起（将一个值附加到另一个值）构成单个值。

```sql
SELECT Concat(vend_name, '(', vend_country, ')')
FROM Vendors
ORDER BY vend_name;
```

上面两个SELECT语句拼接以下元素：

- 存储在vend_name列中的名字；
- 包含一个空格和一个左圆括号的字符串；
- 存储在vend_country列中的国家；
- 包含一个右圆括号的字符串。从上述输出中可以看到，SELECT语句返回包含上述四个元素的一个列（计算字段）。

说明：TRIM函数大多数DBMS都支持RTRIM()（正如刚才所见，它去掉字符串右边的空格）、LTRIM()（去掉字符串左边的空格）以及TRIM()（去掉字符串左右两边的空格）。

```sql
SELECT Concat(RTrim(vend_name), ' (',
    RTrim(vend_country), ')') AS vend_title
FROM Vendors
ORDER BY vend_name;
```

说明：AS通常可选在很多DBMS中，AS关键字是可选的，不过最好使用它，这被视为一条最佳实践。

**2.执行算术计算：**计算字段的另一常见用途是对检索出的数据进行算术计算。举个例子，Orders表包含收到的所有订单，OrderItems表包含每个订单中的各项物品。下面的SQL语句检索订单号20008中的所有物品：

```sql
SELECT prod_id,
        quantity,
        item_price,
        quantity*item_price AS expanded_price
FROM OrderItems
WHERE order_num = 20008;
```

```sql
prod_id          quantity          item_price        expanded_price
----------       -----------       ------------      -----------------
RGAN01           5                 4.9900            24.9500
BR03             5                 11.9900           59.9500
BNBG01           10                3.4900            34.9000
BNBG02           10                3.4900            34.9000
BNBG03           10                3.4900            34.9000
```

SQL算术操作符如下：

| 操作符 | 说明 |
| ------ | ---- |
| +      |      |
| -      |      |
| *      |      |
| /      |      |

#### 使用函数处理

与大多数其他计算机语言一样，SQL也可以用函数来处理数据。函数一般是在数据上执行的，为数据的转换和处理提供了方便。

**1.文本处理函数：**

```sql
SELECT vend_name, UPPER(vend_name) AS vend_name_upcase
FROM Vendors
ORDER BY vend_name;
```

```sql
vend_name                            vend_name_upcase
---------------------------          ----------------------------
Bear Emporium                        BEAR EMPORIUM
Bears R Us                           BEARS R US
Doll House Inc.                      DOLL HOUSE INC.
Fun and Games                        FUN AND GAMES
Furball Inc.                         FURBALL INC.
Jouets et ours                       JOUETS ET OURS
```

可以看到，UPPER()将文本转换为大写，因此本例子中每个供应商都列出两次，第一次为Vendors表中存储的值，第二次作为列vend_name_upcase转换为大写。

常用的文本处理函数：

| 函数                              | 说明                  |
| --------------------------------- | --------------------- |
| LEFT（或使用字符串函数）          | 返回字符串左边的字符  |
| LENGTH（也使用DATALENGTH()或LEN() | 返回字符串的长度      |
| LOWER()                           | 将字符串转换为小写    |
| LTRIM()                           | 去掉字符串左边的字符  |
| RIGHT()（或使用字符串函数）       | 返回字符串右边的字符  |
| RTRIM()                           | 去掉字符串右边的空格  |
| SUBSTR()或SUBSTRING()             | 提取字符串的组成部分  |
| SOUNDEX()                         | 返回字符串的SOUNDEX值 |
| UPPER()                           | 将字符串转换为大写    |

**日期和时间处理函数：**日期和时间采用相应的数据类型存储在表中，每种DBMS都有自己的特殊形式。日期和时间值以特殊的格式存储，以便能快速和有效地排序或过滤，并且节省物理存储空间。

应用程序一般不使用日期和时间的存储格式，因此日期和时间函数总是用来读取、统计和处理这些值。由于这个原因，日期和时间函数在SQL中具有重要的作用。遗憾的是，它们很不一致，可移植性最差。

我们举个简单的例子，来说明日期处理函数的用法。Orders表中包含的订单都带有订单日期。要检索出某年的所有订单，需要按订单日期去找，但不需要完整日期，只要年份即可。

DB2,MySQL和MariaDB具有各种日期处理函数，但没有DATEPART()。DB2,MySQL和MariaDB用户可使用名为YEAR()的函数从日期中提取年份：

```sql
SELECT order_num
FROM Orders
WHERE YEAR(order_date) = 2020;
```

**数值处理函数：**数值处理函数仅处理数值数据。这些函数一般主要用于代数、三角或几何运算，因此不像字符串或日期-时间处理函数使用那么频繁。

具有讽刺意味的是，在主要DBMS的函数中，数值函数是最一致、最统一的函数。如下所示：

| 函数   | 说明               |
| ------ | ------------------ |
| ABS()  | 返回一个数的绝对值 |
| COS()  | 返回一个数的余弦值 |
| EXP()  | 返回一个数的指数值 |
| PI()   | 返回圆周率Π的值    |
| SIN()  | 返回一个角度的正弦 |
| SQRT() | 返回一个数的平方根 |
| TAN()  | 返回一个角度的正切 |

#### 汇总数据

**1.聚集函数**

| 函数    | 说明             |
| ------- | ---------------- |
| AVG()   | 返回某列的平均值 |
| COUNT() | 返回某列的行数   |
| MAX()   | 返回某列的最大值 |
| MIN()   | 返回某列的最小值 |
| SUM()   | 返回某列之和     |

**AVG()函数：**

AVG()通过对表中行数计数并计算其列值之和，求得该列的平均值。AVG()可用来返回所有列的平均值，也可以用来返回特定列或行的平均值。

```sql
SELECT AVG(prod_price) AS avg_price
FROM Products;
```

```sql
SELECT AVG(prod_price) AS avg_price
FROM Products
WHERE vend_id = 'DLL01';
```

说明：NULL值AVG()函数忽略列值为NULL的行。

**COUNT()函数：**

COUNT()函数进行计数。可利用COUNT()确定表中行的数目或符合特定条件的行的数目。

```sql
SELECT COUNT(*) AS num_cust
FROM Customers;
```

```sql
SELECT COUNT(cust_email) AS num_cust
FROM Customers;
```

说明：NULL值如果指定列名，则COUNT()函数会忽略指定列的值为NULL的行，但如果COUNT()函数中用的是星号（＊），则不忽略。

**MAX()函数：**

MAX()返回指定列中的最大值。MAX()要求指定列名，如下所示：

```sql
SELECT MAX(prod_price) AS max_price
FROM Products;
```

说明：NULL值MAX()函数忽略列值为NULL的行。

**MIN()函数：**

MIN()的功能正好与MAX()功能相反，它返回指定列的最小值。与MAX()一样，MIN()要求指定列名，如下所示：

```sql
SELECT MIN(prod_price) AS min_price
FROM Products;
```

说明：NULL值MIN()函数忽略列值为NULL的行。

**SUM()函数：**

SUM()用来返回指定列值的和（总计）。

```
SELECT SUM(quantity) AS items_ordered
FROM OrderItems
WHERE order_num = 20005;
```

```sql
SELECT SUM(item_price＊quantity) AS total_price
FROM OrderItems
WHERE order_num = 20005;
```

说明：NULL值SUM()函数忽略列值为NULL的行。

**2.聚集不同值**

以上5个聚集函数都可以如下使用。

❑ 对所有行执行计算，指定ALL参数或不指定参数（因为ALL是默认行为）。

❑ 只包含不同的值，指定DISTINCT参数。

```sql
SELECT AVG(DISTINCT prod_price) AS avg_price
FROM Products
WHERE vend_id = 'DLL01';
```

**3.组合聚集函数**

目前为止的所有聚集函数例子都只涉及单个函数。但实际上，SELECT语句可根据需要包含多个聚集函数。请看下面的例子：

```sql
SELECT COUNT(*) AS num_items,
        MIN(prod_price) AS price_min,
        MAX(prod_price) AS price_max,
        AVG(prod_price) AS price_avg
FROM Products;
```

#### 分组数据

**1.创建分组**

```sql
SELECT vend_id, COUNT(*) AS num_prods
FROM Products
GROUP BY vend_id;
```

因为使用了GROUP BY，就不必指定要计算和估值的每个组了。系统会自动完成。GROUP BY子句指示DBMS分组数据，然后对每个组而不是整个结果集进行聚集。

在使用GROUP BY子句前，需要知道一些重要的规定。

- ❑ GROUP BY子句可以包含任意数目的列，因而可以对分组进行嵌套，更细致地进行数据分组。
- ❑ 如果在GROUP BY子句中嵌套了分组，数据将在最后指定的分组上进行汇总。换句话说，在建立分组时，指定的所有列都一起计算（所以不能从个别的列取回数据）。
- ❑ GROUP BY子句中列出的每一列都必须是检索列或有效的表达式（但不能是聚集函数）。如果在SELECT中使用表达式，则必须在GROUP BY子句中指定相同的表达式。不能使用别名。
- ❑ 大多数SQL实现不允许GROUP BY列带有长度可变的数据类型（如文本或备注型字段）。
- ❑ 除聚集计算语句外，SELECT语句中的每一列都必须在GROUP BY子句中给出。
- ❑ 如果分组列中包含具有NULL值的行，则NULL将作为一个分组返回。如果列中有多行NULL值，它们将分为一组。
- ❑ GROUP BY子句必须出现在WHERE子句之后，ORDER BY子句之前。

**2.过滤分组：**

除了能用GROUP BY分组数据外，SQL还允许过滤分组，规定包括哪些分组，排除哪些分组。例如，你可能想要列出至少有两个订单的所有顾客。为此，必须基于完整的分组而不是个别的行进行过滤。

WHERE过滤行，而HAVING过滤分组。HAVING支持所有WHERE操作符。

```sql
SELECT cust_id, COUNT(*) AS orders
FROM Orders
GROUP BY cust_id
HAVING COUNT(*) >= 2;
```

```sql
cust_id          orders
----------      -----------
1000000001      2
```

这条SELECT语句的前三行类似于上面的语句。最后一行增加了HAVING子句，它过滤COUNT(＊) >= 2（两个以上订单）的那些分组。

```sql
SELECT vend_id, COUNT(*) AS num_prods
FROM Products
WHERE prod_price >= 4
GROUP BY vend_id
HAVING COUNT(*) >= 2;
```

```
vend_id      num_prods
-------      -----------
BRS01        3
FNG01        2
```

这条语句中，第一行是使用了聚集函数的基本SELECT语句，很像前面的例子。WHERE子句过滤所有prod_price至少为4的行，然后按vend_id分组数据，HAVING子句过滤计数为2或2以上的分组。如果没有WHERE子句，就会多检索出一行（供应商DLL01，销售4个产品，价格都在4以下）：

```sql
SELECT vend_id, COUNT(*) AS num_prods
FROM Products
GROUP BY vend_id
HAVING COUNT(*) >= 2;
```

```sql
vend_id      num_prods
-------      -----------
BRS01        3
DLL01        4
FNG01        2
```

说明：使用HAVING和WHERE

HAVING与WHERE非常类似，如果不指定GROUP BY，则大多数DBMS会同等对待它们。不过，你自己要能区分这一点。使用HAVING时应该结合GROUP BY子句，而WHERE子句用于标准的行级过滤。

**3.分组和排序：**

```sql
SELECT order_num, COUNT(*) AS items
FROM OrderItems
GROUP BY order_num
HAVING COUNT(*) >= 3
ORDER BY items, order_num;
```

```sql
order_num      items
---------      -----
20006           3
20009           3
20007           5
20008           5
```

**4.SELECT子句顺序：**

| 子句     | 说明               | 是否必须使用           |
| -------- | ------------------ | ---------------------- |
| SELECT   | 要返回的列或表达式 | 是                     |
| FROM     | 从中检索数据的表   | 仅在从表选择数据时使用 |
| WHERE    | 行级过滤           | 否                     |
| GROUP BY | 分组说明           | 仅在按组计算聚集时使用 |
| HAVING   | 组级过滤           | 否                     |
| ORDER BY | 输出排序顺序       | 否                     |

#### 使用子查询

**1.子查询：**

```sql
SELECT cust_id
FROM Orders
WHERE order_num IN (SELECT order_num
                      FROM OrderItems
                      WHERE prod_id = 'RGAN01');
```

在SELECT语句中，子查询总是从内向外处理。在处理上面的SELECT语句时，DBMS实际上执行了两个操作。首先，它执行下面的查询：

```sql
SELECT order_num 
FROM orderitems 
WHERE prod_id='RGAN01';
```

此查询返回两个订单号：20007和20008。然后，这两个值以IN操作符要求的逗号分隔的格式传递给外部查询的WHERE子句。外部查询变成：

```sql
SELECT cust_id 
FROM orders 
WHERE order_num IN (20007,20008);
```

现在得到了订购物品RGAN01的所有顾客的ID。下一步是检索这些顾客ID的顾客信息。检索两列的SQL语句为：

```sql
SELECT cust_name, cust_contact
FROM Customers
WHERE cust_id IN (1000000004,1000000005);
```

可以把其中的WHERE子句转换为子查询，而不是硬编码这些顾客ID：

```sql
SELECT cust_name, cust_contact
FROM Customers
WHERE cust_id IN (SELECT cust_id
                   FROM Orders
                   WHERE order_num IN (SELECT order_num
                                        FROM OrderItems
                                        WHERE prod_id = 'RGAN01'));
```

为了执行上述SELECT语句，DBMS实际上必须执行三条SELECT语句。最里边的子查询返回订单号列表，此列表用于其外面的子查询的WHERE子句。外面的子查询返回顾客ID列表，此顾客ID列表用于最外层查询的WHERE子句。最外层查询返回所需的数据。

注意：只能是单列作为子查询的SELECT语句只能查询单个列。企图检索多个列将返回错误。

**2.作为计算字段使用子查询：**

使用子查询的另一方法是创建计算字段。假如需要显示Customers表中每个顾客的订单总数。订单与相应的顾客ID存储在Orders表中。

执行这个操作，要遵循下面的步骤：

(1) 从Customers表中检索顾客列表；

(2) 对于检索出的每个顾客，统计其在Orders表中的订单数目。

正如前两课所述，可以使用SELECT COUNT(＊)对表中的行进行计数，并且通过提供一条WHERE子句来过滤某个特定的顾客ID，仅对该顾客的订单进行计数。例如，下面的代码对顾客1000000001的订单进行计数：

```sql
SELECT COUNT(*) AS orders
FROM Orders
WHERE cust_id = 1000000001;
```

要对每个顾客执行COUNT(＊)，应该将它作为一个子查询。请看下面的代码：

```sql
SELECT cust_name,
        cust_state,
        (SELECT COUNT(*)
        FROM Orders
        WHERE Orders.cust_id = Customers.cust_id) AS orders
FROM Customers
ORDER BY cust_name;
```

```sql
cust_name                         cust_state      orders
-------------------------         ----------      ------
Fun4All                           IN              1
Fun4All                           AZ              1
Kids Place                        OH              0
The Toy Store                     IL              1
Village Toys                      MI              2
```

#### 联结表

**1.等值联结：**

```sql
SELECT vend_name, prod_name, prod_price
FROM Vendors, Products;
```

```sql
vend_name             prod_name                       prod_price
----------------     ----------------------------     ----------
Bears R Us            8 inch teddy bear                  5.99
Bears R Us            12 inch teddy bear                 8.99
...
Bear Emporium         8 inch teddy bear                  5.99
Bear Emporium         12 inch teddy bear                 8.99

...
Doll House Inc.       8 inch teddy bear                  5.99
Doll House Inc.       12 inch teddy bear                 8.99
...
Furball Inc.          8 inch teddy bear                  5.99
Furball Inc.          12 inch teddy bear                 8.99
...
Fun and Games         8 inch teddy bear                  5.99
Fun and Games         12 inch teddy bear                 8.99
...
Jouets et ours        8 inch teddy bear                  5.99
Jouets et ours        12 inch teddy bear                 8.99
...
```

**2.内联结：**目前为止使用的联结称为等值联结（equijoin），它基于两个表之间的相等测试。这种联结也称为内联结（inner join）。其实，可以对这种联结使用稍微不同的语法，明确指定联结的类型。下面的SELECT语句返回与前面例子完全相同的数据：

```sql
SELECT vend_name, prod_name, prod_price
FROM Vendors
INNER JOIN Products ON Vendors.vend_id = Products.vend_id;
```

此语句中的SELECT与前面的SELECT语句相同，但FROM子句不同。这里，两个表之间的关系是以INNER JOIN指定的部分FROM子句。在使用这种语法时，联结条件用特定的ON子句而不是WHERE子句给出。传递给ON的实际条件与传递给WHERE的相同。

**3.联结多个表：**SQL不限制一条SELECT语句中可以联结的表的数目。创建联结的基本规则也相同。首先列出所有表，然后定义表之间的关系。例如：

```sql
SELECT prod_name, vend_name, prod_price, quantity
FROM OrderItems, Products, Vendors
WHERE Products.vend_id = Vendors.vend_id
  AND OrderItems.prod_id = Products.prod_id
  AND order_num = 20007;
```

```sql
prod_name             vend_name           prod_price      quantity
---------------      -------------       ----------      --------
18 inch teddy bear    Bears R Us          11.9900          50
Fish bean bag toy     Doll House Inc.     3.4900           100
Bird bean bag toy     Doll House Inc.     3.4900           100
Rabbit bean bag toy   Doll House Inc.     3.4900           100
Raggedy Ann           Doll House Inc.     4.9900           50
```

这个例子显示订单20007中的物品。订单物品存储在OrderItems表中。每个产品按其产品ID存储，它引用Products表中的产品。这些产品通过供应商ID联结到Vendors表中相应的供应商，供应商ID存储在每个产品的记录中。这里的FROM子句列出三个表，WHERE子句定义这两个联结条件，而第三个联结条件用来过滤出订单20007中的物品。

#### 创建高级联结

迄今为止，我们使用的只是内联结或等值联结的简单联结。现在来看三种其他联结：自联结（self-join）、自然联结（natural join）和外联结（outer join）。

我感觉我暂时还用不到......

#### 组合查询

可用UNION操作符来组合数条SQL查询。利用UNION，可给出多条SELECT语句，将它们的结果组合成一个结果集。

**使用UNION：**使用UNION很简单，所要做的只是给出每条SELECT语句，在各条语句之间放上关键字UNION。

```sql
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL','IN','MI')
UNION
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4All';
```

**UNION规则：**

可以看到，UNION非常容易使用，但在进行组合时需要注意几条规则。

- ❑ UNION必须由两条或两条以上的SELECT语句组成，语句之间用关键字UNION分隔（因此，如果组合四条SELECT语句，将要使用三个UNION关键字）。
- ❑ UNION中的每个查询必须包含相同的列、表达式或聚集函数（不过，各个列不需要以相同的次序列出）。
- ❑ 列数据类型必须兼容：类型不必完全相同，但必须是DBMS可以隐含转换的类型（例如，不同的数值类型或不同的日期类型）。

**包含或取消重复的行：**如果想返回所有的匹配行，可使用UNION ALL而不是UNION。

```sql
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL','IN','MI')
UNION ALL
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4All';
```

```sql
cust_name        cust_contact           cust_email
-----------      -------------          ------------
Village Toys     John Smith             sales@villagetoys.com
Fun4All          Jim Jones              jjones@fun4all.com
The Toy Store    Kim Howard             NULL
Fun4All          Jim Jones              jjones@fun4all.com
Fun4All          Denise L. Stephens     dstephens@fun4all.com
```

**对组合查询结果排序：**SELECT语句的输出用ORDER BY子句排序。在用UNION组合查询时，只能使用一条ORDER BY子句，它必须位于最后一条SELECT语句之后。对于结果集，不存在用一种方式排序一部分，而又用另一种方式排序另一部分的情况，因此不允许使用多条ORDER BY子句。

```sql
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_state IN ('IL','IN','MI')
UNION
SELECT cust_name, cust_contact, cust_email
FROM Customers
WHERE cust_name = 'Fun4All'
ORDER BY cust_name, cust_contact;
```

```sql
cust_name        cust_contact           cust_email
-----------      -------------          -------------
Fun4All          Denise L. Stephens     dstephens@fun4all.com
Fun4All          Jim Jones              jjones@fun4all.com
The Toy Store    Kim Howard             NULL
Village Toys     John Smith             sales@villagetoys.com
```

### 进阶使用

#### 全文搜索

为了进行全文本搜索，必须索引被搜索的列，而且要随着数据的改变而不断地重新索引。在对表列进行适当设计后，MySQL会自动进行所有的索引和重新索引。在索引之后，SELECT可与Match()和Against()一起使用以实际执行搜索。

**1.启用全文本搜索支持：**一般在创建表时启用全文本搜索。

```sql
CREATE TABLE productnotes(
    note_id int not null auto_increment primary key,
    prod_id char(10) not null,
    note_date datetime not null,
    note_text text null,
    FULLTEXT(note_text)
) ENGINE=MyISAM;
```

MySQL根据子句FULLTEXT(note_text)的指示对它进行索引。这里的FULLTEXT索引单个列，如有需要也可以指定多个列。在定义之后，MySQL自动维护该索引。在增加、更新或删除行时，索引随之自动更新。

**2.进行全文本搜索：**在索引之后，使用两个函数Match()和Against()执行全文本搜索，其中Match()指定被搜索的列，Against()指定要使用的搜索表达式。

```sql
SELECT note_text
FROM productnotes
WHERE Match(note_text) Against("rabbit");
```

此SELECT语句检索单个列note_text。由于WHERE子句，一个全文本搜索被执行。Match(note_text)指示MySQL针对指定的列进行搜索，Against('rabbit')指定词rabbit作为搜索文本。由于有两行包含词rabbit，这两个行被返回。

全文本搜索的一个重要部分就是对结果排序。具有较高等级的行先返回（因为这些行很可能是你真正想要的行）。

全文本搜索提供了简单LIKE搜索不能提供的功能。而且，由于数据是索引的，全文本搜索还相当快

**3.使用查询扩展：**查询扩展用来设法放宽所返回的全文本搜索结果的范围。利用查询扩展，能找出可能相关的结果，即使它们并不精确包含所查找的词。

```sql
SELECT note_text
FROM productnotes
WHERE Match(note_text) Against("anvils" WITH QUERY EXPANSION);
```

这次返回了7行。第一行包含词anvils，因此等级最高。第二行与anvils无关，但因为它包含第一行中的两个词（customer和recommend），所以也被检索出来。第3行也包含这两个相同的词，但它们在文本中的位置更靠后且分开得更远，因此也包含这一行，但等级为第三。第三行确实也没有涉及anvils（按它们的产品名）。

**4.布尔文本搜索：**MySQL支持全文本搜索的另外一种形式，称为布尔方式（boolean mode）。以布尔方式，可以提供如下内容的细节：

- 要匹配的词；
- 要排斥的词（如果某行包含这个词，则不返回该行，即使它包含其他指定的词也是如此）；
- 排列提示（指定某些词比其他词更重要，更重要的词等级更高）;
- 表达式分组；
- 另外一些内容。

具体使用略，因为我感觉我用不到哈哈哈！

#### 使用视图

视图是虚拟的表。与包含数据的表不一样，视图只包含使用时动态检索数据的查询。

```sql
SELECT cust_name, cust_contact
FROM customers, orders, orderitems
WHERE customers.cust_id = orders.cust_id
    AND orderitems.order_num = orders.order_num
    AND prod_id = "TNT2";
```

将这个复杂的查询语句进行包装，包装成一个新的虚拟的表，然后基于这个表去查询数据，接下来就将这个查询进行简化：

**1.创建视图：**

```sql
CREATE VIEW productcustomers AS
SELECT cust_name, cust_contact, prod_id
FROM customers, orders, orderitems
WHERE customers.cust_id = orders.cust_id
    AND orderitems.order_num = orders.order_num;
```

通过CREATE VIEW来创建这个视图（虚拟的表），这个视图联结了三个表，返回了一些数据形成了虚拟的productcustomers视图（虚拟的表），后续可根据此视图进行数据的查询，比如如下代码：

**2.使用视图：**

```sql
SELECT cust_name, cust_contact
FROM productcustomers
WHERE prod_id = "TNT2";
```

以上代码可以检索出视图（虚拟表）productcustomers中的cust_name和cust_contact列，然后进行筛选。

**3.其他使用：**

这里仅列出核心的创建与使用，还有其他：用视图重新格式化检索出的数据、用视图过滤不想要的数据、使用视图与计算字段。

视图为虚拟的表。它们包含的不是数据而是根据需要检索数据的查询。视图提供了一种MySQL的SELECT语句层次的封装，可用来简化数据处理以及重新格式化基础数据或保护基础数据。

#### 使用索引

**1.索引：**索引是对数据库表中一列或多列的值进行排序的一种结构。MySQL索引的建立对于MySQL的高效运行是很重要的，索引可以大大提高MySQL的检索速度。索引只是提高效率的一个因素，如果你的MySQL有大数据量的表，就需要花时间研究建立最优秀的索引，或优化查询语句。

简单类比一下，数据库如同书籍，索引如同书籍目录，假如我们需要从书籍查找与 xx 相关的内容，我们可以直接从目录中查找，定位到 xx 内容所在页面，如果目录中没有 xx 相关字符或者没有设置目录（索引），那只能逐字逐页阅读文本查找，效率可想而知。

**优点**

- 索引大大减小了服务器需要扫描的数据量，从而大大加快数据的检索速度，这也是创建索引的最主要的原因。
- 索引可以帮助服务器避免排序和创建临时表
- 索引可以将随机IO变成顺序IO
- 索引对于InnoDB（对索引支持行级锁）非常重要，因为它可以让查询锁更少的元组，提高了表访问并发性
- 关于InnoDB、索引和锁：InnoDB在二级索引上使用共享锁（读锁），但访问主键索引需要排他锁（写锁）
- 通过创建唯一性索引，可以保证数据库表中每一行数据的唯一性。
- 可以加速表和表之间的连接，特别是在实现数据的参考完整性方面特别有意义。
- 在使用分组和排序子句进行数据检索时，同样可以显著减少查询中分组和排序的时间。
- 通过使用索引，可以在查询的过程中，使用优化隐藏器，提高系统的性能。

**缺点**

- 创建索引和维护索引要耗费时间，这种时间随着数据量的增加而增加
- 索引需要占物理空间，除了数据表占用数据空间之外，每一个索引还要占用一定的物理空间，如果需要建立聚簇索引，那么需要占用的空间会更大
- 对表中的数据进行增、删、改的时候，索引也要动态的维护，这就降低了整数的维护速度
- 如果某个数据列包含许多重复的内容，为它建立索引就没有太大的实际效果。
- 对于非常小的表，大部分情况下简单的全表扫描更高效；

**2.创建索引：**

使用 `CREATE INDEX` 语句：可以使用专门用于创建索引的 `CREATE INDEX` 语句在一个已有的表上创建索引，但该语句不能创建主键。例如，如果你想在 `mytable` 表的 `column1` 列上创建一个名为 `index1` 的索引，你可以使用以下语句：

```sql
CREATE INDEX index1 ON mytable (column1);
```

使用 `ALTER TABLE` 语句：你也可以使用 `ALTER TABLE` 语句在一个已有的表上创建索引。例如，如果你想在 `mytable` 表的 `column1` 列上创建一个名为 `index1` 的索引，你可以使用以下语句：

```sql
ALTER TABLE mytable ADD INDEX index1 (column1);
```

在创建表时指定索引：你还可以在创建表时指定索引。例如，如果你想在创建 `mytable` 表时，在 `column1` 列上创建一个名为 `index1` 的索引，你可以使用以下语句：

```sql
CREATE TABLE mytable (
    column1 INT,
    column2 VARCHAR(255),
    INDEX index1 (column1)
);
```

**选择索引：**

主键索引：一张表只能有一个主键索引，不允许重复、不允许为 NULL；

```java
 ALTER TABLE TableName ADD PRIMARY KEY(column_list); 
```

唯一索引：数据列不允许重复，允许为 NULL 值，一张表可有多个唯一索引，索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一。

```java
CREATE UNIQUE INDEX IndexName ON `TableName`(`字段名`(length));
# 或者
ALTER TABLE TableName ADD UNIQUE (column_list); 
```

普通索引：一张表可以创建多个普通索引，一个普通索引可以包含多个字段，允许数据重复，允许 NULL 值插入；

```java
CREATE INDEX IndexName ON `TableName`(`字段名`(length));
# 或者
ALTER TABLE TableName ADD INDEX IndexName(`字段名`(length));
```

全文索引：它查找的是文本中的关键词，主要用于全文检索。（篇幅较长，下文有独立主题说明）

**删除索引：**

```sql
DROP INDEX index_name ON table_name
```

#### 控制语句

在谈论控制语句之前先看看MySQL的变量！

**1.变量：**变量是表达式语句中最基本的元素，可以用来临时存储数据。在存储过程和函数中都可以定义和使用变量。用户可以使用 DECLARE 关键字来定义变量，定义后可以为变量赋值。这些变量的作用范围是 BEGIN...END 程序段中。

**定义变量：**

```sql
-- DECLARE var_name[,...] type [DEFAULT value]
```

- DECLARE 关键字是用来声明变量的；
- var_name 参数是变量的名称，这里可以同时定义多个变量；
- type 参数用来指定变量的类型；
- DEFAULT value 子句将变量默认值设置为 value，没有使用 DEFAULT 子句时，默认值为 NULL。

```sql
-- 声明一个变量xuefeng，默认值为Lns-XueFeng
DECLARE xuefeng TEXT DEFAULT "Lns-XueFeng";
```

**变量赋值：**

```sql
-- SET var_name = expr[,var_name = expr]...
```

- SET 关键字用来为变量赋值；
- var_name 参数是变量的名称；
- expr 参数是赋值表达式。

```sql
-- 为变量xuefeng赋值
SET xuefeng = "XueFeng";
```

注意：一个 SET 语句可以同时为多个变量赋值，各个变量的赋值语句之间用逗号隔开。

MySQL另外一种给变量赋值的方式，使用SELECT vol_name INTO var_name FROM table_name WHERE condition;

```sql
-- 将person_name表中id为1的哪一行的name值赋值给xuefeng
SELECT name INTO xuefeng
FROM person_name
WHERE per_id = 1;
```

**定义条件：**定义条件是指事先定义程序执行过程中遇到的问题，处理程序定义了在遇到这些问题时应当采取的处理方式和解决办法，保证存储过程和函数在遇到警告或错误时能继续执行，从而增强程序处理问题的能力，避免程序出现异常被停止执行。

```sql
-- 方法一：使用sqlstate_value
DECLARE can_not_find CONDITION FOR SQLSTATE '42S02';

-- 方法二：使用 mysql_error_code
DECLARE can_not_find CONDITION FOR 1146;
```

**2.IF语句：**

```sql
-- 语法格式如下：
IF search_condition THEN statement_list
    [ELSEIF search_condition THEN statement_list]...
    [ELSE statement_list]
END IF
```

```sql
IF age > 20 THEN SET @count1 = @count + 1;
    ELSEIF age = 20 THEN @count2 = count2 + 1;
    ELSE @count3 = @count3 + 1;
END IF;
```

**3.WHILE语句：**

```sql
[begin_label:] WHILE search_condition DO
    statement list
END WHILE [end label]
```

```sql
WHILE @count < 100 DO
    SET @count = @count + 1;
END WHILE;
```

另外还有其他的控制语句，比如：CASE语句、LOOP语句、LEAVE语句、ITERATE语句、REPEAT语句。

#### 存储过程

**1.存储过程：**存储过程简单来说，就是为以后的使用而保存的一条或多条MySQL语句的集合。可将其视为批文件，虽然它们的作用不仅限于批处理。

**2.创建存储过程：**

```sql
CREATE PROCEDURE productpricing()
DELIMITER $$
BEGIN
    SELECT Avg(prod_price) AS priceaverage
    FROM products;
END;$$
DELIMITER ;
```

此代码用CREATE PROCEDURE语句定义一个名为productpricing的存储过程；你会发现其形式和高级程序语言中的函数很像，但是这里有些不一样的是变量的传入与传出。

**3.使用存储过程：**MySQL称存储过程的执行为调用，因此MySQL执行存储过程的语句为CALL。CALL接受存储过程的名字以及需要传递给它的任意参数。

```sql
CALL productpricing(@pricelow, @pricehigh, @priceaverage);
```

执行上面的存储过程productpricing：

```sql
CALL productpricing();
```

这个语句会调用productpricing存储过程，执行里面的语句，这里是SELECT查询，将其显示出来。而在更多的时候是将查询结果存储在变量内，下面进行介绍。

**4.使用参数：**productpricing只是一个简单的存储过程，它简单地显示SELECT语句的结果。一般，存储过程并不显示结果，而是把结果返回给你指定的变量。

```sql
CREATE PROCEDURE productpricing(
    OUT pl DECIMAL(8, 2),
    OUT ph DECIMAL(8, 2),
    OUT pa DECIMAL(8, 2)
)
DELIMITER $$
BEGIN
    SELECT Min(prod_price)
    INTO pl
    FROM products;
    SELECT Max(prod_price)
    INTO ph;
    SELECT Avg(prod_price)
    INTO pa
    FROM products;
END;$$
DELIMITER ;
```

MySQL支持三种类型的参数：

- IN：传递给存储过程
- OUT：从存储过程传出
- INOUT：对存储过程传入和传出

存储过程的代码位于BEGIN和END语句内，如前所见，它们是一系列SELECT语句，用来检索值，然后保存到相应的变量（通过指定INTO关键字）。

```sql
CALL productpricing(@pricelow, @pricehigh, @priceaverage);
```

注意：所有MySQL的变量都必须以@开始。

这里传入了三个存储过程要求的三个参数。它们是存储过程将保存结果的3个变量的名字。

在调用时，这条语句并不显示任何数据。它返回以后可以显示（或在其他处理中使用）的变量。

```sql
SELECT @pricehigh, @pricelow, @priceaverage;
```

此时通过这条语句即可显示出相应的数据。

上面的例子并没有用到IN，并且也没有传入什么参数来定制化的操作，下面是另外一个例子来理解IN和OUT，并传入参数来根据参数做些查询。

```sql
CREATE PROCEDURE ordertotal(
   IN onumber INT,
   OUT ototal DECIMAL(8, 2)
)
DELIMITER $$
BEGIN
   SELECT Sum(item_price*quantity)
   FROM orderitems
   WHERE order_num = onumber
   INTO ototal;
END;$$
DELIMITER ;
```

onumber定义为IN，因为订单号被传入存储过程。ototal定义为OUT，因为要从存储过程返回合计。SELECT语句使用这两个参数，WHERE子句使用onumber选择正确的行，INTO使用ototal存储计算出来的合计。

```sql
CALL ordertotal(20005, @total);
SELECT @total;
```

**5.建立智能存储过程：**迄今为止使用的所有存储过程基本上都是封装MySQL简单的SELECT语句。虽然它们全都是有效的存储过程例子，但它们所能完成的工作你直接用这些被封装的语句就能完成（如果说它们还能带来更多的东西，那就是使事情更复杂）。只有在存储过程内包含业务规则和智能处理时，它们的威力才真正显现出来。

其实就是编写有逻辑的存储过程，使用诸如控制语句，布尔判断等，以此可以写出更加复杂的存储过程且通常更加的有用。

```sql
-- Name: ordertotal
-- Parameters: onumber = order number
--             taxable = 0 if not taxable, 1 if taxable
--             ototal  = order total variable
CREATE PROCEDURE ordertotal(
    IN onumber INT,
    IN taxable BOOLEAN,
    OUT ototal DECIMAL(8, 2)
) COMMENT "Obtain order total, optionally adding tax"
DELIMITER $$
BEGIN
    -- Declare variable for total
    DECLARE total DECIMAL(8, 2);
    -- Declare tax percentage
    DECLARE taxrate INT DEFAULT 6;
    
    -- Get the order total
    SELECT Sum(item_price*quantity)
    FROM orderitems
    WHERE order_num = onumber
    INTO total;
    
    -- Is this taxable?
    IF taxable THEN
    -- Yes, so add taxrate to the total
    SELECT total + (total/100*taxrate) INTO total;
    END IF;
    
    -- And finally, save to out variable
    SELECT total INTO ototal;
END;$$
DELIMITER ;
```

```sql
CALL ordertotal(20005, 0, @total);
SELECT @total;
```

**6.删除存储过程：**存储过程在创建之后，被保存在服务器上以供使用，直至被删除。

```
DROP PROCEDURE ordertotal;
```

这条语句删除刚创建的存储过程。请注意没有使用后面的()，只给出存储过程名。

```sql
DROP PROCEDURE IF EXISTS ordertotal;
```

**7.检查存储过程：**

为显示用来创建一个存储过程的CREATE语句，使用SHOW CREATE PROCEDURE语句：

```sql
SHOW CREATE PROCEDURE ordertotal;
```

为了获得包括何时、由谁创建等详细信息的存储过程列表，使用SHOW PROCEDURE STATUS：

```sql
SHOW PROCEDURE STATUS LIKE "ordertotal";
```

#### 使用游标

有时，需要在检索出来的行中前进或后退一行或多行。这就是使用游标的原因。游标（cursor）是一个存储在MySQL服务器上的数据库查询，它不是一条SELECT语句，而是被该语句检索出来的结果集。在存储了游标之后，应用程序可以根据需要滚动或浏览其中的数据。游标主要用于交互式应用，其中用户需要滚动屏幕上的数据，并对数据进行浏览或做出更改。

**1.使用游标：**

使用游标涉及几个明确的步骤。

- 在能够使用游标前，必须声明（定义）它。这个过程实际上没有检索数据，它只是定义要使用的SELECT语句。
- 一旦声明后，必须打开游标以供使用。这个过程用前面定义的SELECT语句把数据实际检索出来。
-  对于填有数据的游标，根据需要取出（检索）各行。
- 在结束游标使用时，必须关闭游标。

在声明游标后，可根据需要频繁地打开和关闭游标。在游标打开后，可根据需要频繁地执行取操作。

**2.创建游标：**MySQL游标只能用于存储过程（和函数）。

```sql
CREATE PROCEDURE processorders()
BEGIN
    DECLARE ordernumbers CURSOR
    FOR
    SELECT order_num FROM orders;
END;
```

DECLARE语句用来定义和命名游标，这里为ordernumbers。存储过程处理完成后，游标就消失（因为它局限于存储过程）。

**3.打开游标：**游标用OPEN CURSOR语句来打开：

```sql
OPEN ordernumbers;
```

在处理OPEN语句时执行查询，存储检索出的数据以供浏览和滚动。

**4.使用游标数据：**在一个游标被打开后，可以使用FETCH语句分别访问它的每一行。FETCH指定检索什么数据（所需的列），检索出来的数据存储在什么地方。它还向前移动游标中的内部行指针，使下一条FETCH语句检索下一行（不重复读取同一行）。

```sql
CREATE PROCEDURE processorders()
BEGIN
    DECLARE o INT;
    DECLARE ordernumbers CURSOR
    FOR 
    SELECT order_num FROM orders;
    
    OPEN ordernumbers;
    FETCH ordernumbers INTO o;
    CLOSE ordernumbers;
END;
```

其中FETCH用来检索当前行的order_num列（将自动从第一行开始）到一个名为o的局部声明的变量中。对检索出的数据不做任何处理。

```sql
CREATE PROCEDURE processorders()
BEGIN
	DECLARE done BOOLEAN DEFAULT 0;
    DECLARE o INT;
    DECLARE t DECIMAL(8, 2);
    
    DECLARE ordernumbers CURSOR
    FOR 
    SELECT order_num FROM orders;
    
    DECLARE CONTINUE HANDLER FOR SQLSTATE "02000" SET done=1;
    CREATE TABLE IF NOT EXISTS ordertotals
        (order_num INT, total DECIMAL(8, 2));
        
    OPEN ordernumbers
    REPEAT
        FETCH ordernumbers INTO o;
        CALL ordertotal(o, 1, t);
        INSERT INTO ordertotals(order_num, total) VALUES(o, t);
    UNTIL done END REPEAT;
    CLOSE ordernumbers;
END;
```

**5.关闭游标：**游标用CLOSE CURSOR语句来打开：

```sql
CLOSE ordernumbers;
```

CLOSE释放游标使用的所有内部内存和资源，因此在每个游标不再需要时都应该关闭。

#### 使用触发器

**1.触发器：**MySQL语句在需要时被执行，存储过程也是如此。但是，如果你想要某条语句（或某些语句）在事件发生时自动执行，怎么办呢？例如：

- 每当增加一个顾客到某个数据库表时，都检查其电话号码格式是否正确，州的缩写是否为大写；
- 每当订购一个产品时，都从库存数量中减去订购的数量；
- 无论何时删除一行，都在某个存档表中保留一个副本。

所有这些例子的共同之处是它们都需要在某个表发生更改时自动处理。这确切地说就是触发器。触发器是MySQL响应以下任意语句而自动执行的一条MySQL语句（或位于BEGIN和END语句之间的一组语句）：

- DELETE；
- INSERT；
- UPDATE；

其他MySQL语句不支持触发器。

**2.创建触发器：**

在创建触发器时，需要给出4条信息：

- 唯一的触发器名；
- 触发器关联的表；
- 触发器应该响应的活动（DELETE、INSERT或UPDATE）；
- 触发器何时执行（处理之前或之后）；

触发器用CREATE TRIGGER语句创建。

```sql
CREATE TRIGGER newproduct AFTER INSERT ON products
FOR EACH ROW SELECT "Product added";
```

以上SQL语句表示，创建一个newproduct触发器，在对products表执行了插入数据操作之后显示Product added。

触发器按每个表每个事件每次地定义，每个表每个事件每次只允许一个触发器。因此，每个表最多支持6个触发器（每条INSERT、UPDATE和DELETE的之前和之后）。单一触发器不能与多个事件或多个表关联，所以，如果你需要一个对INSERT和UPDATE操作执行的触发器，则应该定义两个触发器。

**3.使用触发器：**

**INSERT触发器**

INSERT触发器在INSERT语句执行之前或之后执行。需要知道以下几点：

- 在INSERT触发器代码内，可引用一个名为NEW的虚拟表，访问被插入的行；
- 在BEFORE INSERT触发器中，NEW中的值也可以被更新（允许更改被插入的值）；
- 对于AUTO_INCREMENT列，NEW在INSERT执行之前包含0，在INSERT执行之后包含新的自动生成值。

```sql
CREATE TRIGGER neworder AFTER INSERT ON orders
FOR EACH ROW SELECT NEW.order_num;
```

在插入一个新订单到orders表时，MySQL生成一个新订单号并保存到order_num中。触发器从NEW. order_num取得这个值并返回它。此触发器必须按照AFTER INSERT执行，因为在BEFORE INSERT语句执行之前，新order_num还没有生成。对于orders的每次插入使用这个触发器将总是返回新的订单号。

```sql
INSERT INTO orders(order_date, cust_id)
VALUES(Now(), 10001);
```

当这个SQL语句执行后，会触发neworder触发器，这里是显示出order_num。

**DELETE触发器**

DELETE触发器在DELETE语句执行之前或之后执行。需要知道以下两点：

- 在DELETE触发器代码内，你可以引用一个名为OLD的虚拟表，访问被删除的行；
- OLD中的值全都是只读的，不能更新。

```sql
CREATE TRIGGER deleteorder BEFORE DELETE ON orders
FOR EACH ROW
BEGIN 
    INSERT INTO archive_orders(order_num, order_date, cust_id)
    VALUES(OLD.order_num, OLD.order_date, OLD.cust_id);
END;
```

**UPDATE触发器**

UPDATE触发器在UPDATE语句执行之前或之后执行。需要知道以下几点：

- 在UPDATE触发器代码中，你可以引用一个名为OLD的虚拟表访问以前（UPDATE语句前）的值，引用一个名为NEW的虚拟表访问新更新的值；
- 在BEFORE UPDATE触发器中，NEW中的值可能也被更新（允许更改将要用于UPDATE语句中的值）；
- OLD中的值全都是只读的，不能更新。

```sql
CREATE TRIGGER updatevendor BEFORE UPDATE ON vendors
FOR EACH ROW SET NEW.vend_state = Upper(NEW.vend_state);
```

**4.删除触发器：**

```sql
DROP TRIGGER newproduct;
```

触发器不能更新或覆盖。为了修改一个触发器，必须先删除它，然后再重新创建。

#### 管理事务处理

**1.事务处理：**事务处理（transaction processing）可以用来维护数据库的完整性，它保证成批的MySQL操作要么完全执行，要么完全不执行。

事务处理是一种机制，用来管理必须成批执行的MySQL操作，以保证数据库不包含不完整的操作结果。利用事务处理，可以保证一组操作不会中途停止，它们或者作为整体执行，或者完全不执行（除非明确指示）。如果没有错误发生，整组语句提交给（写到）数据库表。如果发生错误，则进行回退（撤销）以恢复数据库到某个已知且安全的状态。

在使用事务和事务处理时，有几个关键词汇反复出现。下面是关于事务处理需要知道的几个术语：

- 事务（transaction）指一组SQL语句；
- 回退（rollback）指撤销指定SQL语句的过程；
- 提交（commit）指将未存储的SQL语句结果写入数据库表；
- 保留点（savepoint）指事务处理中设置的临时占位符（place-holder），你可以对它发布回退（与回退整个事务处理不同）。
