

# Python数据结构与算法

## 为什么要学习数据结构与算法？

## 1.How to ues ADT解决实际问题

先给出结论：算法+数据结构=程序

![6F86F14C-F0E7-4918-8DF6-C93951722EE9](/Users/lixuehong/Pictures/Photos Library.photoslibrary/originals/6/6F86F14C-F0E7-4918-8DF6-C93951722EE9.jpeg)

### 什么是算法？

计算机科学的研究对象是问题、解决问题的过程，以及通过该过程得到的解决方案。给定一个问题，计算机科学家的目标是开发一个能够逐步解决该问题的算法。算法是具有有限步骤的过程，依照这个过程便能解决问题。因此，算法就是解决方案。



### 什么是抽象？

抽象就是在研究问题时只留下你所认为的问题最本质的东西。

在研究问题解决过程的同时，计算机科学也研究抽象。抽象思维使得我们能分别从逻辑视角和物理视角来看待问题及其解决方案。



抽象举例：

试想你每天开车去上学或上班。作为车的使用者，你在驾驶时会与它有一系列的交互：坐进车里，插入钥匙，启动发动机，换挡，刹车，加速以及操作方向盘。从抽象的角度来看，这是从逻辑视角来看待这辆车，你在使用由汽车设计者提供的功能来将自己从某个地方运送到另一个地方。这些功能有时候也被称作接口。

另一方面，修车工看待车辆的角度与司机截然不同。他不仅需要知道如何驾驶，而且更需要知道实现汽车功能的所有细节：发动机如何工作，变速器如何换挡，如何控制温度，等等。这就是所谓的物理视角，即看到表面之下的实现细节。



我们在编写代码实现问题解决放的过程中绝不仅仅是从单一物理视角或者是单一逻辑视角去解决问题，而是两者兼并，比如在问题数学建模时可使用逻辑视角来梳理如何解决问题而不涉及具体底层实现，再上层构建完成后可以选择自己进行底层实现或是交给团队其他人进行实现，这是物理视角。正因为将抽象分为了抽象视角和物理视角，才实现了上层用户实现问题时只需要知道接口的功能与如何调用，而不需要知道底层实现，而下层用户则可以专注实现底层功能实现。



### 数据结构及抽象数据类型

为了控制问题及其求解过程的复杂度，计算机科学家利用抽象来帮助自己专注于全局，从而避免迷失在众多细节中。通过对问题进行建模，可以更高效地解决问题。模型可以帮助计算机科学家更一致地描述算法要用到的数据。

如前所述，过程抽象将功能的实现细节隐藏起来，从而使用户能从更高的视角来看待功能。数据抽象的基本思想与此类似。

抽象数据类型（有时简称为ADT）从逻辑上描述了如何看待数据及其对应运算而无须考虑具体实现。这意味着我们仅需要关心数据代表了什么，而可以忽略它们的构建方式。通过这样的抽象，我们对数据进行了一层封装，其基本思想是封装具体的实现细节，使它们对用户不可见，这被称为信息隐藏。抽象数据类型的实现常被称为数据结构，这需要我们通过编程语言的语法结构和原生数据类型从物理视角看待数据。正如之前讨论的，分成这两种不同的视角有助于为问题定义复杂的数据模型，而无须考虑模型的实现细节。这便提供了一个独立于实现的数据视角。由于实现抽象数据类型通常会有很多种方法，因此独立于实现的数据视角使程序员能够改变实现细节而不影响用户与数据的实际交互。用户能够始终专注于解决问题。



我们在对问题编写算法时亦可采用这种思维模式，先从逻辑视角对问题进行分析与描述，而将其中抽象的接口往后推，先不实现，专注于解决核心问题，在前者完成后，即可从物理视角对抽象数据类型进行底层实现，这个过程就是数据结构。这样我们就完成了问题的建模与程序的实现。



### 总结

深刻了解上诉概念以后我们不妨思考我们要如何对复杂的实际问题进行一步步的求解?

1. 对问题进行观察，得出我们需要实现的目标以及在实现目标过程中需要用到的抽象数据类型和相应的解决问题的算法。
2. 并且将其中的抽象数据类型进行后推，先描述其接口与功能而不着急实现，直接利用这些抽象数据类型进行核心算法的实现和对问题的建模。
3. 在问题建模与核心操作实现之后，即可对抽象数据类型进行底层实现，这一过程的实现就被称为数据结构。

例如日后我们要学习的小乌龟走迷宫：

1. 首先先确定了目标就是走出迷宫，而达到这一目标需要有一个迷宫地图（抽象数据类型），需要小乌龟具有四个方向行进，碰壁返回，避免重复走已经走过的路，判断当前是否为出口的能力，而对于小乌龟功能的实现则采用了递归算法（核心算法与操作）。
2. 描述完问题之后，将抽象数据类型迷宫地图的实现后推，先描述出其接口与功能。直接利用其接口与功能来实现小乌龟的具体功能（核心算法实现），它的具体实现就是定义一个函数，先判断是否碰壁，判断是否走到已走过的路，再使用四个递归来尝试四个方向前进。这基本就是核心算法实现。
3. 在核心算法实现之后，我们就开始着眼于实现刚刚后推的抽象数据类型迷宫地图和其他的一些细节进行实现，对于迷宫地图可通过定义一个类，其功能有：画迷宫地图，更新地图，实现索引实时取地图方格数据用来判断小乌龟当前状态…而在函数里面则还需要在小乌龟正确的行进之后更新地图，在小乌龟找到出口时递归压栈结束。
4. 最终完成这个实际问题的建模且此程序很明显就是由 抽象数据类型 +算法 组成。由于抽象数据类型的实现常被称为数据结构，因此 数据结构 + 算法 =程序。



## 2.衡量算法性能

### 引子

在日后的算法学习会遇到非常多的不同的算法，它们有的占用资源少但运行速度慢，有的占用资源多但运行速度快，有的则是中和其两者……因此，需要有一种概念表示来衡量它们算法性能的优劣，而直接测量出算法的运行时间又太过麻烦，不具备通用性，所以，大O记法应运而生。

### 大O记法

数量级（order of magnitude）常被称作大O记法（O指order），记作O(f(n))。它提供了步骤数的一个有用的近似方法。f(n)函数为T(n)函数中起决定性作用的部分提供了简单的表示。想象一下当程序运行的n无限大时n相对于n的平方即可忽略不计。

举个例子：

![EA328B22-D6FD-4548-9A2A-837D42A023BE](/Users/lixuehong/Pictures/Photos Library.photoslibrary/originals/E/EA328B22-D6FD-4548-9A2A-837D42A023BE.jpeg)



我们来计算一下图中的性能如何，从上往下分析代码，123行代码均为1，然后发现两个嵌套的循环为n(3n)，接着又遇到一个循环为2n，最后一行代码为1，整理可得T(n)=3n2次方+2n+4

可发现普通代码是1，循环是n，嵌套多少层循环就几次方，最后进行简化，在n无限大时，n的2次方占主导，因此时间复杂度为O(n2次方)



下面给出Python常用数据类型的时间复杂度；

### 列表常用操作时间复杂度

![034A1104-ABA9-4E9A-B79F-7BC348BC4DC3](/Users/lixuehong/Pictures/Photos Library.photoslibrary/originals/0/034A1104-ABA9-4E9A-B79F-7BC348BC4DC3.jpeg)

### 字典常用操作时间复杂度

![DBF11487-BC86-447C-8DE2-EA40C2F6F035_4_5005_c](/Users/lixuehong/Pictures/Photos Library.photoslibrary/resources/derivatives/masters/D/DBF11487-BC86-447C-8DE2-EA40C2F6F035_4_5005_c.jpeg)



## 3.栈及其Python实现



### 什么是线性数据结构？

栈、队列、双端队列和列表都是有序的数据集合，其元素的顺序取决于添加顺序或移除顺序。一旦某个元素被添加进来，它与前后元素的相对位置将保持不变。这样的数据集合经常被称为线性数据结构。



### 什么是栈？

栈有时也被称作“下推栈”。它是有序集合，添加操作和移除操作总发生在同一端，即“顶端”，另一端则被称为“底端”。



栈中的元素离底端越近，代表其在栈中的时间越长，因此栈的底端具有非常重要的意义。最新添加的元素将被最先移除。这种排序原则被称作LIFO（last-in first-out），即后进先出。它提供了一种基于在集合中的时间来排序的方式。最近添加的元素靠近顶端，旧元素则靠近底端。



为了更加形象的描述它，我来举一个例子，假如你现在手里有五本书abcde，你需要将手中的书按照abncd的顺序一本一本的放到桌子上，并且后放的书只能放到上一本书的上面，即a最先放到桌子上，b随后放在a上，c放在b上，d放在c上，e放在d上且为最后一本书，处在整堆书的最上方，其实这就是栈，它们相对位置不变，且最先放的书在最底下，最后放的书在最上面，取出的时候也只能从最上面的书开始一本一本的往外取，而且取出的顺序和放入时正好相反，为edcba，因此，最先放的书最后取出，最后放的书会被最先取出。



### Python实现栈ADT

栈是元素的有序集合，添加操作与移除操作都发生在其顶端。栈的操作顺序是LIFO，它支持以下操作。



❏ Stack()创建一个空栈。它不需要参数，且会返回一个空栈。



❏ push(item)将一个元素添加到栈的顶端。它需要一个参数item，且无返回值。



❏ pop()将栈顶端的元素移除。它不需要参数，但会返回顶端的元素，并且修改栈的内容。



❏ peek()返回栈顶端的元素，但是并不移除该元素。它不需要参数，也不会修改栈的内容。



❏ isEmpty()检查栈是否为空。它不需要参数，且会返回一个布尔值。



❏ size()返回栈中元素的数目。它不需要参数，且会返回一个整数。

假

```python
# 栈的Python实现, 以列表的右边边为栈顶

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # 朝栈顶添加元素

    def pop(self):
        self.stack.pop()  # 删除栈顶元素

    def peek(self):
        return self.stack[-1]  # 返回栈顶元素

    def isEmpty(self):
        return self.stack == []  # 判断栈是否为空

    def size(self):
        return len(self.stack)  # 返回栈元素数量


s = Stack()
print(s)
print(s.isEmpty())
s.push(3)
print(s.stack)
s.push(2)
print(s.stack)
s.push(1)
print(s.stack)
s.pop()
print(s.stack)
print(s.peek())
print(s.size())
```



## 4.队列及其Python实现



### 什么是队列？

队列是有序集合，添加操作发生在“尾部”，移除操作则发生在“头部”。新元素从尾部进入队列，然后一直向前移动到头部，直到成为下一个被移除的元素。



最新添加的元素必须在队列的尾部等待，在队列中时间最长的元素则排在最前面。这种排序原则被称作FIFO（first-in first-out），即先进先出，也称先到先得。



老规矩我们来举一个现实中的例子，假设你早上起床出门要去买包子，但是店家明确挂牌说明请排队用餐，因此你只能跑到队伍的尾部进行排队，你看着头部的人一个个买完走人，心情越来越舒畅，因为你在漫长的等待之后终于来到了头部，拿着香喷喷的包子去上班了，走之前还不忘瞅瞅新来的进入队列尾部的觅食者。

我们来总结这个过程，新来的买包子的只能从队列尾部进入，最终从头部出去。假设队列人数不变，那么每一个人其实从新来到买完包子等待的时间都是一致的，并且在队列中呆的时间最久的总是头部的那个人，呆的最短的则是尾部的那个人。这就是队列，即添加操作发生在队列尾部，移除操作发生在队列头部，并且遵循先进先出的规则。



### Python实现队列抽象类型

队列是元素的有序集合，添加操作发生在其尾部，移除操作则发生在头部。队列的操作顺序是FIFO，它支持以下操作。



❏ Queue()创建一个空队列。它不需要参数，且会返回一个空队列。



❏ enqueue(item)在队列的尾部添加一个元素。它需要一个元素作为参数，不返回任何值。



❏ dequeue()从队列的头部移除一个元素。它不需要参数，且会返回一个元素，并修改队列的内容。



❏ isEmpty()检查队列是否为空。它不需要参数，且会返回一个布尔值。



❏ size()返回队列中元素的数目。它不需要参数，且会返回一个整数。



```python
# 队列的Python实现，列表的右边是头部

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)  # 朝队列尾部添加元素

    def dequeue(self):
        self.queue.pop()  # 移除队列头部的元素

    def isEmpty(self):
        return self.queue == []  # 判断队列是否为空

    def size(self):
        return len(self.queue)


q = Queue()
print(q)
print(q.isEmpty())
q.enqueue(1)
print(q.queue)
q.enqueue(2)
print(q.queue)
q.enqueue(3)
print(q.queue)
q.dequeue()
print(q.queue)
print(q.size())
```



## 5.双端队列及其Python实现



### 什么是双端队列？

与栈和队列不同的是双端队列的限制非常少，因为双端队列的前端和后端均可进行添加和移除操作，它就好像是栈和队列的结合体。我认为它存在的意义就是为了让我们使用者灵活的进行使用而不必拘束于前面两种数据结构的规则，如何添加和移除全凭我们自己以及需要。

![67F60A9A-0109-4810-A606-527680EF8772_4_5005_c](/Users/lixuehong/Pictures/Photos Library.photoslibrary/resources/derivatives/masters/6/67F60A9A-0109-4810-A606-527680EF8772_4_5005_c.jpeg)

上图是由Python数据对象组成的双端队列



### Python实现双端队列ADT

双端队列是元素的有序集合，其任何一端都允许添加或移除元素。双端队列支持以下操作。



❏ Deque()创建一个空的双端队列。它不需要参数，且会返回一个空的双端队列。



❏ addFront(item)将一个元素添加到双端队列的前端。它接受一个元素作为参数，没有返回值。



❏ addRear(item)将一个元素添加到双端队列的后端。它接受一个元素作为参数，没有返回值。



❏ removeFront()从双端队列的前端移除一个元素。它不需要参数，且会返回一个元素，并修改双端队列的内容。



❏ removeRear()从双端队列的后端移除一个元素。它不需要参数，且会返回一个元素，并修改双端队列的内容。



❏ isEmpty()检查双端队列是否为空。它不需要参数，且会返回一个布尔值。



❏ size()返回双端队列中元素的数目。它不需要参数，且会返回一个整数。



```python
# 双端队列Python实现，左边为前端，右边为后端

class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addRear(self, item):
        self.deque.append(item)

    def removeFront(self):
        self.deque.pop(0)

    def removeRear(self):
        self.deque.pop()

    def isEmpty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)


d = Deque()
print(d)
print(d.isEmpty())
d.addFront(3)
print(d.deque)
d.addFront(2)
print(d.deque)
d.addFront(1)
print(d.deque)
d.addRear(3)
print(d.deque)
d.addRear(2)
print(d.deque)
d.addRear(1)
print(d.deque)
d.removeFront()
d.removeRear()
print(d.deque)
print(d.size())
```

## 6.链表及其Python实现

Python为我们内置了强大的列表，更准确的说这个列表是无序列表，而无序列表只需要存储元素之间的相对位置即可，而不需要在连续的内存空间中维护这些位置信息，那么我们要如何自己去实现无序列表呢？答案就是利用链表来实现无序列表。



### 什么是链表？

链表就好像一条链子，它将随机存储在内存中的元素通过一个个节点连接起来，在节点中只存储两个信息，一个是元素本身，另一个是指向下一节点的信息。链表有一个头部和一个尾部，头部是元素进入的地方，尾部一大特点则是指向信息为None，代表着没有下一节点，也就是没有下一元素了。当我们去实现链表时，除了需要实现Node类，还需要明白链表添加元素的规则与栈类似，这对后面实现链表帮助很大。



### 链表如何发挥作用？

![17](/Users/lixuehong/Downloads/17.png)

以上图元素集合为例，这些元素的位置看上去都是随机的。如果可以为每一个元素维护一份信息，即下一个元素的位置（见下图），那么这些元素的相对位置就能通过指向下一个元素的链接来表示。

![31（尼）](/Users/lixuehong/Downloads/31（尼）.png)

需要注意的是，必须指明列表中第一个元素的位置。一旦知道第一个元素的位置，就能根据其中的链接信息访问第二个元素，接着访问第三个元素，依此类推。指向链表第一个元素的引用被称作头。最后一个元素需要知道自己没有下一个元素。



### Python实现链表

1.要实现链表，首先需要实现其中的抽象数据结构-节点。

节点（node）是构建链表的基本数据结构。每一个节点对象都必须持有至少两份信息。首先，节点必须包含列表元素，我们称之为节点的数据变量。其次，节点必须保存指向下一个节点的引用。



Node类：

![temp](/Users/lixuehong/Downloads/temp.png)

Node类是存储链表节点信息的数据结构，其存储着元素和下一元素指向，下面是Node类支持的操作。



❏ Node()创建一个初始值，它接受一个参数，且会返回一个包含元素和指向的节点对象。



❏ getData(item)将一个元素添加到节点之中，它接受一个元素作为参数，没有返回值。



❏ getNext()得到当前节点下一指向，它不接受参数，返回指向下一节点。



❏ setData(item)设置元素信息，它接受一个元素作为参数，没有返回值。



❏ setNext()设置指向下一节点，它不接受参数，返回指向下一节点。



注意：先介绍了Node并不是让你在日常编程中就一定是先实现这种抽象数据类型，而是在链表那边以及定义和思考好了需要哪些抽象类或方法之后并将目标实现相关核心代码逻辑实现后，可先对相关类进行实现。



UnorderList类：

![IMG_3468](/Users/lixuehong/Downloads/IMG_3468.png)

无序列表是元素的集合，其中每一个元素都有一个相对于其他元素的位置。以下是无序列表支持的操作。

❏ List()创建一个空列表。它不需要参数，且会返回一个空列表。



❏ add(item)假设元素item之前不在列表中，并向其中添加item。它接受一个元素作为参数，无返回值。



❏ remove(item)假设元素item已经在列表中，并从其中移除item。它接受一个元素作为参数，并且修改列表。



❏ search(item)在列表中搜索元素item。它接受一个元素作为参数，并且返回布尔值。



❏ isEmpty()检查列表是否为空。它不需要参数，并且返回布尔值。



❏ length()返回列表中元素的个数。它不需要参数，并且返回一个整数。



❏ append(item)假设元素item之前不在列表中，并在列表的最后位置添加item。它接受一个元素作为参数，无返回值。



❏ index(item)假设元素item已经在列表中，并返回该元素在列表中的位置。它接受一个元素作为参数，并且返回该元素的下标。



❏ insert(pos, item)假设元素item之前不在列表中，同时假设pos是合理的值，并在位置pos处添加元素item。它接受两个参数，无返回值。



❏ pop()假设列表不为空，并移除列表中的最后一个元素。它不需要参数，且会返回一个元素。



❏ pop(pos)假设在指定位置pos存在元素，并移除该位置上的元素。它接受位置参数，且会返回一个元素。

```python
# 无序列表:链表Python实现 链表头部和尾部要格外注意


class Node:
    def __init__(self, initData):
        self.data = initData  # 初始化节点
        self.next = None  # 设置尾部下一节单引用为None

    def getData(self):
        return self.data  # 得到节点元素

    def getNext(self):
        return self.next  # 得到节点指向

    def setNext(self, item):
        self.next = item  # 设置节点引用

    def setData(self, data):
        self.data = data  # 设置节点元素


class UnderList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)  # 新建节点
        node.setNext(self.head)  # 设置节点指向
        self.head = node  # 改变公共变量head的值，记录这个节点，方便新添加的节点可指向上一节点

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        while current.getData() != item:
            current = current.getNext()
            if current.getData() == item:
                return True
            if current.next == None:   # 这俩if语句作用是每遇到一个节点都判断一下它的值和引用
                return False

    def remove(self, item):
        current = self.head
        while current.getData() != item:
            frontCurrent = current
            current = current.getNext()
            rearCurrent = current.getNext()   # 建立两个外部引用分别指向当前节点的上下节点
            if current.getData() == item:
                frontCurrent.setNext(rearCurrent)   # 这一步很重要，移除的操作其实就是把当前节点从连接里剔除，连接前后节点即可

                return True

    def append(self, item):
        itemNode = Node(item)
        itemNode.setNext(None)   # 因为item总是添加到链表尾部，所以总为指向引用None
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
            if current.getNext() == None:
                current.setNext(itemNode)

                return True

    def insert(self, num, item):
        itemNode = Node(item)
        current = self.head
        frontCurrent = None  # 建立两个外部引用分别指向当前节点的上下节点
        count = 0
        while count < num:
            frontCurrent = current
            current = current.getNext()
            count = count + 1
        if num == 0:
            itemNode.setNext(current)   # 如果是插入第一个元素则直接连接
        else:
            frontCurrent.setNext(itemNode)   # 将当前节点的前节点连接插入的，插入的连接当前
            itemNode.setNext(current)

    def index(self, item):
        current = self.head
        count = 0
        while current.getData() != item:
            current = current.getNext()
            count = count + 1

        return count

    def pop(self, index):   #负数弹出和删除还没实现
        current = self.head
        count = 0
        if count == index:
            frontCurrent = current
            currentData = current.getData()
            self.head = current.getNext
            frontCurrent.setNext(None)
            return currentData

        while count < index:
            frontCurrent = current
            current = current.getNext()
            rearCurrent = current.getNext()   # 建立两个外部引用分别指向当前节点的上下节点
            currentData = current.getData()
            count = count + 1

            if count == index:
                frontCurrent.setNext(rearCurrent)
                return currentData


l = UnderList()
print(l.isEmpty())
l.add(1)
l.add(2)
l.add(3)
print(l.length())
print(l.search(0))
print(l.remove(1))
print(l.search(1))
l.append(4)
print(l.search(4))
l.insert(1,0)
print(l.index(0))
poped = l.pop(1)
print(poped)

```

## 7.递归算法浅谈

### 什么是递归？

递归是解决问题的一种方法，它将问题不断地分成更小的子问题，直到子问题可以用较简单直接的方法解决。

### 举个例子

假设我们需要计算n个数的相加的和，如果从递归的角度要如何解决呢？

且听我慢慢道来，根据上面递归的描述，我们能不能把这个问题分解成更小的子问题呢？我们将n个数的加和分成n和n-1个数的加和，先算n-1个数的加和，但是n-1仍然太复杂，那么我们在分，分成n-2个数的加和，直至分到只有两个数的加和，此时就可以将它俩直接相加得出结果，然后一步一步回溯，得出n个数的相加结果。

**递归三原则：**

- 递归算法必须有基本情况。
- 递归算法必须改变其状态并向基本情况靠近。
- 递归算法必须递归地调用自己。

我们在设计递归算法解决问题时必须遵守上述三原则。

### 递归如何实现的？

此时你可能疑问，上面我举的例子里面提到把问题一直分解到可以直接解决的子问题，然后回溯，开始一步一步利用已经解决的简单子问题解决相对于刚解决的较复杂的问题，直至解决整个复杂问题，那么这个回溯是如何实现的呢？

答案就是当你在算法里面设置了某一递归调用自己的语句时，一旦Python执行到哪一行递归调用语句，它不会立刻就将其return返回，而是分配栈帧给它，即将它附近的局部变量均存储到一个黑盒子里面并入栈，然后当再一次递归调用时，再将新的局部变量存储到另一个黑盒子里面并入栈，直至最后一次递归调用将其局部变量们存入栈顶，而后开始取栈，此时就会开始执行return返回，得出问题结果。

因此在用递归解决问题时，记住递归与栈的关系，一般来说可以用递归解决很多复杂问题。

### 树的递归实现

```python
import turtle as t


def tree(n):
    if n > 5:
        t.forward(n)
        t.right(20)
        tree(n-15) #在所有此递归调用全部压入栈之后运行下面的代码
        t.left(40)
        tree(n-10)
        t.right(20)
        t.backward(n)



if __name__ == '__main__':
    t.penup()
    t.right(90)
    t.forward(150)
    t.pendown()
    t.left(170)
    tree(100)   # 递归画分支
    t.mainloop()
```

### 谢尔金斯三角形

```python
import turtle as t

'''
递归最最最重要的思想就是：将一个问题分解为几个基本问题
比如这个例子，
对于最开始的大三角形要分隔出三个小三角形（连接各先中点）那三个小三角形就分别对应着三个递归去解决
只是因为代码执行顺序为从上到下，所以会先一直解决其中一个小三角形，而那个小三角形也会被分解为三个更小的三角形，
分别由三个递归去解决，以此类推，直到不满足基本条件，退出压栈，开始往回取栈...慢慢的解决另外两个小三角形，
直到全部解决完成，不满足递归条件退出
'''

#根据新得出的三个中点连线
def drawTran(points):
    t.up()
    t.goto(points[0])
    t.pendown()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])

#算出新的内三角形的三个点
def getMid(p1,p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree):
    drawTran(points)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                    degree - 1)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                    degree - 1)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                    degree - 1)


t.setup(1200,1700)
myPoints = [(300,-100), (0,300), (-300,-100)]
sierpinski(myPoints,6)
t.mainloop()
```

## 8.搜索与排序

### 顺序与二分搜索

提示：Python提供了运算符in，通过它可以方便地检查元素是否在列表中。

**顺序搜索**

顾名思义，顺序搜索就是按照某一规则下的顺序逐个遍历元素，在Python中即通过循环来对可迭代对象中的元素进行逐一访问。

每一种算法都有其存在的意义，顺序搜索的时间复杂度为O(n)（最坏情况），你可能觉得n级复杂度很慢啊！但是你忽略了根据具体需要来选择相应的算法，如果遍历量不大，选择顺序搜索即可快速写出代码，并且速度仍可观，但当数据量特别大时，选用顺序搜索显然不是明智之举。

**代码实现**

```python
li = [3, 4, 2, 1, 0, 9, 8, 7, 5, 6]
value = int(input("请输入需要查找的数字："))
for i in li:
    if i == value:
        return True
    return False
```

**二分搜索**

上面说的是无序列表的情况，那么如果列表是有序的呢？

当列表是有序的时候，显然我们可以通过有序的特性做一些优化，由此引出二分法思想，我们通过每一次去中，然后与所需搜索的值进行比较，如果大于需搜索的值则可以判定我们要查询的值可能在列表左半部分，然后在再左半部分进行去中，继续进行比较，直到找到值或者没有这个值。我们谈论的是普通情况，并没有对特殊情况，比如列表最大的元素要是都没有所需找的值大，显然可以直接判定我们要找的值不在列表中。

那么，二分搜索它的性能如何呢？二分搜索每一次都排除一半，即，其时间复杂度为O(logn)，比顺序搜索好上一些。

**二分搜索代码实现**

```python
# 二分实现
def divsearch(value, li):
    fd = 0   # 左指针
    bk = len(li) - 1   # 右指针
    if value < li[fd] or value > li[bk]:
        return False
    elif value == li[fd] or value == li[bk]:
        return True
    else:
        while True:
            if value > li[(bk + fd)//2]:
                fd = (bk + fd)//2
            elif value < li[(bk + fd)//2]:
                bk = (bk + fd)//2
            else:
                if value == li[(bk + fd)//2]:
                    return True
                else:
                    return False

print(divsearch(7, li=[1, 2, 3, 4, 5, 6, 7, 8, 9]))
```

通过上面的描述，不知你是否注意到通过不断的二分，其实就是分而治之的思想，而分而治之则可用递归来进行实现，每一次二分都是此问题规模的缩小版，而形式一样。

**递归实现二分搜索代码**

```python
# 递归实现
def recur_search(value, li):
    fd = 0
    bk = len(li)
    if value > li[bk-1] or value < li[fd]:
        print(None)
        return False

    if len(li) >= 1:
        if value > li[(bk+fd)//2]:
            recur_search(value, li[(bk+fd)//2:bk])
        if value < li[(bk+fd)//2]:
            recur_search(value, li[fd:(bk+fd)//2])
        if value == li[(bk+fd)//2]:
            print(True)
    else:
        print(None)


recur_search(8, li=[1, 2, 3, 4, 5, 6, 7, 8, 9])
```

### 究极牛皮的散列

**引入**

我们在前面分别介绍了面对无序列表时用的顺序搜索和面对有序列表时的二分搜索。根据需要可以自由选择哪一个算法来实现搜索。但是以上搜索算法均不是常数阶，我们想追求一种最快速的搜索算法，而这种算法的实现依靠的就是我们今天的主角-散列！

那么散列的原理我们简要说明一下，后续再一个个详细讨论。如果我们要想构建一个常数阶速度的算法，那么就要实现这么一种设想，假设我们要查询一个元素，那么远在查询之前就做了的事情就是将一元素进行了映射，将映射到值存储到了一个元素集合中。然后，当我们要搜索一个元素是否在元素集合中时，只需要将这个元素进行映射，然后利用得出的映射值直接进行查询操作。

而要实现以上操作，就需要通过散列构建一个时间复杂度为O(1)的数据结构。还需要构建一个散列函数来映射元素。最后尽可能的解决其中的冲突问题。



**散列表**

散列表是元素集合，其中的元素以一种便于查找的方式存储。散列表中的每个位置通常被称为槽，其中可以存储一个元素。槽用一个从0开始的整数标记，例如0号槽、1号槽、2号槽，等等。初始情形下，散列表中没有元素，每个槽都是空的。可以用列表来实现散列表，并将每个元素都初始化为Python中的特殊值None。

![IMG_3538.png](IMG_3538.png)

**散列函数**

散列函数将散列表中的元素与其所属位置对应起来。对散列表中的任一元素，散列函数返回一个介于0和m -1之间的整数。

比如我们有一个、26、93、17、77和31组成的集合，我们对上述的数进行取余数，那么余数和元素构成映射。

![IMG_3540.png](IMG_3540.png)

而我们只需要将这些余数存入散列表的十一个槽中。

![IMG_3541.png](IMG_3541.png)

当我们需要搜索目标元素时，仅需使用散列函数计算出该元素的槽编号，并查看对应的槽中是否有值。因为计算散列值并找到相应位置所需的时间是固定的，所以搜索操作的时间复杂度是O(1)。如果一切正常，那么我们就已经找到了常数阶的搜索算法。

因为我们的目标是创建这样一个散列函数：冲突数最少，计算方便，元素均匀分布于散列表中。因此不局限于取余，只要能满足上述条件即可。这里介绍几个优化取余函数的方法，折叠法和平方取中法。值得一提的是我们可以对字符进行取序数词，然后相加取余，这样做有一个缺点就是遇到异序词取余结果相同，此时只需要把相应字符的权重乘上即可。



**什么是冲突？**

可能你已经看出来了，只有当每个元素的散列值不同时，这个技巧才有用。如果集合中的下一个元素是44，它的散列值是0（44%11==0），而77的散列值也是0，这就有问题了。散列函数会将两个元素都放入同一个槽，这种情况被称作冲突，也叫“碰撞”。

**如何处理冲突？**

当两个元素被分到同一个槽中时，必须通过一种系统化方法在散列表中安置第二个元素。这个过程被称为处理冲突。

- 线性探测法：当遇到两个元素被分到同一槽中时，可以直接通过顺序遍历散列表直至找到一个空槽来放置散列值。但是这样做有一个隐患，就是会造成元素聚集现象，这对使用链表法会造成极大的不利。因此我们一般会设置一个加三的步长进行再散列操作。
- 平方探测法：平方探测法是线性探测法的变形，它将步长均平方，然后进行再散列操作放置元素来避免聚集现象，以免对后续放置元素造成麻烦。
- 链接法：我们在前面有学过链表，其实它在这里可以和散列结合起来进行搭配。之前每一个槽就存入一个元素，但是我们换个思路，我们把每一个槽放一个链表，相同散列值的都放到一个链表里面，这样就解决了槽不够用的问题（但是在元素过多时会损失速度）。当需要执行查询操作时，只需要将计算出其散列值，对应查询到指定槽，而后顺序遍历链表查看值是否存在。

![IMG_3546.png](IMG_3546.png)



**实现映射抽象数据类型：**

前面说了散列表，散列函数，那么他们的抽象数据类型要如何实现呢？

字典是最有用的Python集合之一。第1章说过，字典是存储键-值对的数据类型。键用来查找关联的值，这个概念常常被称作映射。

映射抽象数据类型定义如下。它是将键和值关联起来的无序集合，其中的键是不重复的，键和值之间是一一对应的关系。映射支持以下操作。

❏ Map()创建一个空的映射，它返回一个空的映射集合。

❏ put(key, val)往映射中加入一个新的键-值对。如果键已经存在，就用新值替换旧值。

❏ get(key)返回key对应的值。如果key不存在，则返回None。

❏ del通过del map[key]这样的语句从映射中删除键-值对。

❏ len()返回映射中存储的键-值对的数目。

❏ in通过key in map这样的语句，在键存在时返回True，否则返回False。

使用字典的一大优势是，给定一个键，能很快找到其关联的值。为了提供这种快速查找能力，需要能支持高效搜索的实现方案。虽然可以使用列表进行顺序搜索或二分搜索，但用前面描述的散列表更好，这是因为散列搜索算法的时间复杂度可以达到O(1)。

```python
```

### 排序实现思想讨论

**排序定义：**

排序是指将集合中的元素按某种顺序排列的过程。比如，一个单词列表可以按字母表或长度排序；一个城市列表可以按人口、面积或邮编排序。

**算法选择：**

排序算法的效率与待处理元素的数目相关。对于小型集合，采用复杂的排序算法可能得不偿失；对于大型集合，需要尽可能充分地利用各种改善措施。

在讨论具体的算法之前，先思考如何分析排序过程。首先，排序算法要能比较大小。为了给一个集合排序，需要某种系统化的比较方法，以检查元素的排列是否违反了顺序。在衡量排序过程时，最常用的指标就是总的比较次数。其次，当元素的排列顺序不正确时，需要交换它们的位置。交换是一个耗时的操作，总的交换次数对于衡量排序算法的总体效率来说也很重要。

### 交换-冒泡排序

冒泡排序多次遍历列表。它比较相邻的元素，将不合顺序的交换。每一轮遍历都将下一个最大值放到正确的位置上。本质上，每个元素通过“冒泡”找到自己所属的位置。

即，每排完一次序都排好一个最大值，在经过n趟之后所有元素均排好序。

![IMG_3549.png](IMG_3549.png)



但是在这个过程中，其实非常有可能是早已经排好序，但是冒泡排序仍然在继续，导致浪费计算资源切效率下降，因此我们需要判断一次遍历之后舒服有进行交换元素，如果没有，则可判定已经排好了序，从而节省资源提升效率，但是仍然无法改变冒泡排序时间复杂度仍是O(n平方)。

**代码实现**

```python
# 第一版
def bubble_sort(li):
    for i in range(len(li)-1): #第i趟
        for j in range(len(li)-i-1): #j为指针，指向第j个无序区的元素
            if li[j] > li[j+1]: #如果前一个数比后一个数大
                li[j],li[j+1] = li[j+1],li[j] #就交换位置
        print(li) #显示每一趟排序后的列表
        

li = [3,5,2,1,7,9,8,4]
bubble_sort(li)


# 改进版，当已经排序好时，无需在进行剩下的趟数的排序
def bubble_sort(li):
    for i in range(len(li)-1):   # n次遍历，逐步缩小排序范围
        exchange = False   # 用来标识本次遍历是否有进行排序替换，如果没有排序证明已然有序
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return   # 没进行排序便退出循环

        
print("改进版:")
li = [3,5,2,1,7,9,8,4]
bubble_sort(li)
```

### 交换-选择排序

核心思想：

选择排序在冒泡排序的基础上做了改进，每次遍历列表时只做一次交换。要实现这一点，选择排序在每次遍历时寻找最大值，并在遍历完之后将它放到正确位置上。



选择排序的时间复杂度仍然是O(n平方)，但是实现思路则是不断的将最大值和后面的交换。

![IMG_3550.png](IMG_3550.png)



**代码实现**

```python
'''
选择排序:
将最左侧元素假设为最小，而后逐步遍历i,len(li)找出一个个相对于第i个数的最小值并与之交换
与冒泡排序的区别:冒泡排序数判断每相邻元素是否交换，选择排序则是第i个数与i,len(li)中最小数交换
即:
一趟记录最小的数放到第一个元素的位置
在一趟排序记录列表无序区最小的数，放到第二个位置
...
关键点:有序区和无序区，无序区最小数的位置
'''


def select_sort(li):
    for i in range(len(li)-1): #i表示第i趟
        min_loc = i #假设第一个数是最小的
        for j in range(i+1,len(li)): #在遍历右边的无序区
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i],li[min_loc] = li[min_loc],li[i] #第i趟遍历完成找到无序区最小数与第i个数交换
        print(li)
    return li

li = [3,2,4,1,6,5,8,7,9]
select_sort(li)
#print(select_sort(li))
```

### 子列表-插入排序

插入排序的时间复杂度也是O(n2)，但原理稍有不同。它在列表较低的一端维护一个有序的子列表，并逐个将每个新元素“插入”这个子列表。

![IMG_3551.png](IMG_3551.png)



首先假设位置0处的元素是只含单个元素的有序子列表。从元素1到元素n-1，每一轮都将当前元素与有序子列表中的元素进行比较。在有序子列表中，将比它大的元素右移；当遇到一个比它小的元素或抵达子列表终点时，就可以插入当前元素。



**代码实现**

```python
'''
插入排序:
初始时手里（有序区）只有一张牌
每次从（无序区）摸一张牌，插入到自己手里已有牌的正确位置
'''

'''
def f_sort(li):
    for i in range(1,len(li)): #从无序区摸的牌
        j = i - 1 #手里的牌
        while j >= 0 and li[j] > li[i]: 
            li[j],li[j+1] = li[j+1],li[j] #交换
            j -= 1 
        print(li)
    return li
'''

def insert_sort(li):
    for i in range(1,len(li)): #从无序区摸的牌
        tmp = li[i] #给摸的牌记录下来
        j = i - 1 #手里的牌
        while j >= 0 and li[j] > tmp: #遍历手牌选择插入点
                        #当j大于等于0(防止小于零取到列表末尾的...)且...
            #li[j],li[j+1] = li[j+1],li[j]
            li[j+1] = li[j]#则li[j]右移一位
            j -= 1 #此时j-1，用于下一次的判断
        li[j+1] = tmp #循环遍历判断完插入点后，将tmp插入到插入点
        print(li)
    return li


li = [3,4,5,2,1,6,8,7,9]
print(insert_sort(li))
```

### 子列表-希尔排序

希尔排序也称“递减增量排序”，它对插入排序做了改进，将列表分成数个子列表，并对每一个子列表应用插入排序。如何切分列表是希尔排序的关键——并不是连续切分，而是使用增量i（有时称作步长）选取所有间隔为i的元素组成子列表。

在所有子列表排好序之后，再将子列表进行排序。



以图5-18中的列表为例，这个列表有9个元素。如果增量为3，就有3个子列表，每个都可以应用插入排序，结果如图5-19所示。尽管列表仍然不算完全有序，但通过给子列表排序，我们已经让元素离它们的最终位置更近了。

![IMG_3552.png](IMG_3552.png)

![IMG_3553.png](IMG_3553.png)



图5-20展示了最终的插入排序过程。由于有了之前的子列表排序，因此总移动次数已经减少了。本例只需要再移动4次。

![IMG_3554.png](IMG_3554.png)



如前所述，如何切分列表是希尔排序的关键。代码清单5-13中的函数采用了另一组增量。先为个子列表排序，接着是个子列表。最终，整个列表由基本的插入排序算法排好序。图5-21展示了采用这种增量后的第一批子列表。

![IMG_3555.png](IMG_3555.png)



**代码实现**

```python
```

### 分治策略-归并排序

不知你是否还记得之前学习的递归算法以及分治策略思想。仔细观察所需排序的列表，我们可以从分治思想出发，将列表一分为二，二分四，四分八…直至基本情况。



现在我们要研究的第一个算法是归并排序，它是递归算法，每次将一个列表一分为二。如果列表为空或只有一个元素，那么从定义上来说它就是有序的（基本情况）。如果列表不止一个元素，就将列表一分为二，并对两部分都递归调用归并排序。当两部分都有序后，就进行归并这一基本操作。归并是指将两个较小的有序列表归并为一个有序列表的过程。图5-22a展示了示例列表被拆分后的情况，图5-22b给出了归并后的有序列表。

![IMG_3556.png](IMG_3556.png)



**代码实现**

```python
```

### 分治策略-快速排序

归并排序一样，快速排序也采用分治策略，但不使用额外的存储空间。不过，代价是列表可能不会被一分为二。出现这种情况时，算法的效率会有所下降。

快速排序算法首先选出一个基准值。尽管有很多种选法，但为简单起见，本节选取列表中的第一个元素。基准值的作用是帮助切分列表。在最终的有序列表中，基准值的位置通常被称作分割点，算法在分割点切分列表，以进行对快速排序的子调用。

在图5-23中，元素54将作为第一个基准值。从前面的例子可知，54最终应该位于31当前所在的位置。下一步是分区操作。它会找到分割点，同时将其他元素放到正确的一边——要么大于基准值，要么小于基准值。

![IMG_3557.png](IMG_3557.png)



分区操作首先找到两个坐标——leftmark和rightmark——它们分别位于列表剩余元素的开头和末尾，如图5-24所示。分区的目的是根据待排序元素与基准值的相对大小将它们放到正确的一边，同时逐渐逼近分割点。图5-24展示了为元素54寻找正确位置的过程。

![IMG_3558.png](IMG_3558.png)



首先加大leftmark，直到遇到一个大于基准值的元素。然后减小rightmark，直到遇到一个小于基准值的元素。这样一来，就找到两个与最终的分割点错序的元素。本例中，这两个元素就是93和20。互换这两个元素的位置，然后重复上述过程。

当rightmark小于leftmark时，过程终止。此时，rightmark的位置就是分割点。将基准值与当前位于分割点的元素互换，即可使基准值位于正确位置，如图5-25所示。分割点左边的所有元素都小于基准值，右边的所有元素都大于基准值。因此，可以在分割点处将列表一分为二，并针对左右两部分递归调用快速排序函数。

![IMG_3559.png](IMG_3559.png)



**代码实现**

```python
'''
快速排序思路：
    取一个元素p（第一个元素），使元素p归位
    列表被p分为两部分，左边都比p小，右边都比p大
    递归完成排序
    def quick_sort(data,left,right):
        mid = partition(data,left,right)
        quick_sort(data,left,mid-1) #左半边递归排序
        quick_sort(data,mid+1,right) #右半边递归排序
'''


def partition(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp: #从右边找出比tmp小的数
            right -= 1 #往左走一步
        li[left] = li[right] #把右边的值写到左边空位上
        print(li,'right')
        while left < right and li[left] <= tmp: #从z左边找出比tmp小的数
            right += 1  # 往右走一步
        li[right] = li[left]  # 把左边的值写到右边空位上
        print(li, 'left')
    li[left] = tmp #把tmp归位
    return left

def quick_sort(li,left,right):
    if left < right: #至少两个元素
        mid = partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)


li = [3,5,4,2,1,8,7,9,6]
print(quick_sort(li,0,len(li)-1))
```



## 9.树

在学习了栈和队列等线性数据结构和了解了递归之后我们便可以来学习另外一个非常重要且影响深远的数据结构-树。

### 什么是树？

字面理解它外观还就是现实世界中的树，可以联想一下我们之前利用递归算法实现的树，只不过这个数据结构的“树”是倒着来的。

例如我们天天使用的windows系统其文件目录就是依靠了树这个数据结构来实现的。

![IMG_3649.png](IMG_3649.png)

再比如我在爬虫过程中经常打交道的前端三件套中的html，其语法结构也是依靠树这一世界结构来实现的。

![IMG_3650.png](IMG_3650.png)

### 术语及其定义

**节点**

节点是树的基础部分。它可以有自己的名字，我们称作“键”。节点也可以带有附加信息，我们称作“有效载荷”。有效载荷信息对于很多树算法来说不是重点，但它常常在使用树的应用中很重要。

**边**

边是树的另一个基础部分。两个节点通过一条边相连，表示它们之间存在关系。除了根节点以外，其他每个节点都仅有一条入边，出边则可能有多条。

**根节点**

根节点是树中唯一没有入边的节点。在第一张图中，/就是根节点。

**路径**

路径是由边连接的有序节点列表。比如，哺乳纲→食肉目→猫科→猫属→家猫就是一条路径。

**子节点**

一个节点通过出边与子节点相连。在图2中，log/、spool/和yp/都是var/的子节点。



**父节点**

一个节点是其所有子节点的父节点。在图2中，var/是log/、spool/和yp/的父节点。

**兄弟节点**

具有同一父节点的节点互称为兄弟节点。文件系统树中的etc/和usr/就是兄弟节点。

子树

一个父节点及其所有后代的节点和边构成一棵子树。

**叶子节点**

叶子节点没有子节点。比如，图1中的人和黑猩猩都是叶子节点。

**层数**

节点n的层数是从根节点到n的唯一路径长度。在图1中，猫属的层数是5。由定义可知，根节点的层数是0。

**高度**

树的高度是其中节点层数的最大值。图1中的树高度为2。

### 树的两种定义

**定义一：树由节点及连接节点的边构成。**

树有以下属性：

❏ 有一个根节点；

❏ 除根节点外，其他每个节点都与其唯一的父节点相连；

❏ 从根节点到其他每个节点都有且仅有一条路径；

❏ 如果每个节点最多有两个子节点，我们就称这样的树为二叉树。

![IMG_3651.png](IMG_3651.png)

**看到定义一与相应的图片我想你应该要联想到链表。**



**定义二**、一棵树要么为空，要么由一个根节点和零棵或多棵子树构成，子树本身也是一棵树。每棵子树的根节点通过一条边连到父树的根节点。下图展示了树的递归定义。从树的递归定义可知，图中的树至少有4个节点，因为三角形代表的子树必定有一个根节点。这棵树或许有更多的节点，但必须更深入地查看子树后才能确定。

![IMG_3652.png](IMG_3652.png)

**我想，看到此图你应该要联想到列表实现。**



### 二叉树的链表实现

```python
# 二叉树的链表实现

class BinaryTree:
    def __init__(self, rootvbj):
        self.key = rootvbj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)

        else:
            newLeft = BinaryTree(newNode)
            newLeft.leftChild = self.leftChild
            self.leftChild = newLeft

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)

        else:
            newRight = BinaryTree(newNode)
            newRight.rightChild = self.rightChild
            self.rightChild = newRight

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootValue(self, value):
        self.key = value

    def getRootValue(self):
        return self.key


r = BinaryTree(rootvbj='a')   # 创建二叉树
r.insertLeft('b')   # 插入左子树
r.insertRight('c')   # 插入右子树

print(r)   # 二叉树对象
print(r.getLeftChild())   # 左子树对象
print(r.getRightChild())   # 右子树对象

print(r.getRootValue())   # 根值
print(r.getLeftChild().key)   # 左子树值
print(r.getRightChild().key)   # 右子树值

```



### 二叉树的嵌套列表实现

```python
# 嵌套列表实现二叉树

class BinaryTree:
    def __init__(self, value):
        self.root = [value, [], []]

    def insertLeft(self, BinaryTree):
        if self.root[1] is []:
            self.root[1] = BinaryTree
        else:
            leftTree = self.root.pop(1)  # 将根下的大左子树弹出
            newBinaryTree = BinaryTree  # 新生成一个二叉树
            newBinaryTree.root[1] = leftTree  # 将弹出的大左子树插入到新二叉树左子树
            self.root.insert(1, newBinaryTree.root)  # 将新左子树类的root插入到根的左子树

    def insertRight(self, BinaryTree):
        if self.root is []:
            self.root[2] = BinaryTree
        else:
            rightTree = self.root.pop(2)  # 将根下的大右子树弹出
            newBinaryTree = BinaryTree  # 新生成一个二叉树
            newBinaryTree.root[2] = rightTree  # 将弹出的大右子树插入到新二叉树右子树
            self.root.insert(2, newBinaryTree.root)  # 将新右子树插入到根的右子树

    def getLeftChild(self):
        return self.root[1]

    def getRightChild(self):
        return self.root[2]

    def setRootValue(self, value):
        self.root[0] = value

    def getRootValue(self):
        return self.root[0]


r = BinaryTree(value='a')  # 生成二叉树
print(r.root)
newLeft = BinaryTree(value='b')  # 生成二叉树的左子树
r.insertLeft(newLeft)  # 插入左子树
print(r.root[1])
newRight = BinaryTree(value='c')  # 生成二叉树的右子树
r.insertRight(newRight)  # 插入右子树
print(r.root[2])

print(r.root)

newLeft = BinaryTree(value='d')
r.insertLeft(newLeft)
print(r.root)

```

### 二叉树的应用

**利用二叉树处理全括号表达式。**

我们可以将((7 + 3) ∗ (5-2))这样的数学表达式表示成解析树，如下图1所示。这是完全括号表达式，乘法的优先级高于加法和减法，但因为有括号，所以在做乘法前必须先做括号内的加法和减法。树的层次性有助于理解整个表达式的计算次序。在计算顶层的乘法前，必须先计算子树中的加法和减法。加法（左子树）的结果是10，减法（右子树）的结果是3。利用树的层次结构，在计算完子树的表达式后，只需用一个节点代替整棵子树即可。应用这个替换过程后，便得到如图下图2所示的简化树。

![IMG_3653.png](IMG_3653.png)

![IMG_3654.png](IMG_3654.png)

着重观察表达式的优先顺序，而后利用树特有的层级结构来对全括号表达式进行解析。



**那么问题来了**

❏ 如何根据完全括号表达式构建解析树；

❏ 如何计算解析树中的表达式；

❏ 如何将解析树还原成最初的数学表达式。



构建解析树的第一步是将表达式字符串拆分成标记列表。需要考虑4种标记：左括号、右括号、运算符和操作数。我们知道，左括号代表新表达式的起点，所以应该创建一棵对应该表达式的新树。反之，遇到右括号则意味着到达该表达式的终点。我们也知道，操作数既是叶子节点，也是其运算符的子节点。此外，每个运算符都有左右子节点。



**有了上述信息，便可以定义以下4条规则：**

(1) 如果当前标记是(，就为当前节点添加一个左子节点，并下沉至该子节点；

(2) 如果当前标记在列表['+', '-', '/', '＊']中，就将当前节点的值设为当前标记对应的运算符；为当前节点添加一个右子节点，并下沉至该子节点；

(3) 如果当前标记是数字，就将当前节点的值设为这个数并返回至父节点；

(4) 如果当前标记是)，就跳到当前节点的父节点。



例如利用树将表达式(3 + (4 ∗ 5))进行解析。

![IMG_3655.png](IMG_3655.png)

根据上图来对构建过程有一个清晰直观的理解。

(a) 创建一棵空树。

(b) 读入第一个标记(。根据规则1，为根节点添加一个左子节点。

(c) 读入下一个标记3。根据规则3，将当前节点的值设为3，并回到父节点。

(d) 读入下一个标记+。根据规则2，将当前节点的值设为+，并添加一个右子节点。新节点成为当前节点。

(e) 读入下一个标记(。根据规则1，为当前节点添加一个左子节点，并将其作为当前节点。

(f) 读入下一个标记4。根据规则3，将当前节点的值设为4，并回到父节点。

(g) 读入下一个标记＊。根据规则2，将当前节点的值设为＊，并添加一个右子节点。新节点成为当前节点。

(h) 读入下一个标记5。根据规则3，将当前节点的值设为5，并回到父节点。

(i) 读入下一个标记)。根据规则4，将＊的父节点作为当前节点。

(j) 读入下一个标记)。根据规则4，将+的父节点作为当前节点。因为+没有父节点，所以工作完成。

在构建解析树的过程中，需要追踪当前节点及其父节点。可以通过getLeftChild与getRightChild获取子节点，但如何追踪父节点呢？一个简单的办法就是在遍历这棵树时使用栈记录父节点。每当要下沉至当前节点的子节点时，先将当前节点压到栈中。当要返回到当前节点的父节点时，就将父节点从栈中弹出来。



至此，利用树和栈即可完成解析树的Python实现。

### 解析树的Python实现

```python
# 二叉解析树的Python实现

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # 朝栈顶添加元素

    def pop(self):
        return self.stack.pop()  # 删除栈顶元素

    def peek(self):
        return self.stack[-1]  # 返回栈顶元素

    def is_empty(self):
        return self.stack == []  # 判断栈是否为空

    def size(self):
        return len(self.stack)  # 返回栈元素数量


class BinaryTree:
    def __init__(self, rootvbj):
        self.key = rootvbj
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)

        else:
            newLeft = BinaryTree(newNode)
            newLeft.leftChild = self.leftChild
            self.leftChild = newLeft

    def insert_right(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)

        else:
            newRight = BinaryTree(newNode)
            newRight.rightChild = self.rightChild
            self.rightChild = newRight

    def get_left_child(self):
        return self.leftChild

    def get_right_child(self):
        return self.rightChild

    def set_root_value(self, value):
        self.key = value

    def get_root_value(self):
        return self.key


# 输入必须为全括号表达式,例如(3+(4-2))
def build_parse_tree(fp_exp):
    fp_list = list(fp_exp)
    print(fp_list)
    stack = Stack()
    etree = BinaryTree('')
    stack.push(etree)
    current_tree = etree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/)':
            current_tree.set_root_value(eval(i))
            parent = stack.pop()   # 利用栈来达到从子节点上升至父节点
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_value(i)
            current_tree.insert_right(i)
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = stack.pop()
        else:
            raise ValueError('错误的操作：' + i)
    return etree


fp = '(3+(4-1))'
etree = build_parse_tree(fp)
print("根节点：" + etree.key)
left_tree = etree.get_left_child()
right_tree = etree.get_right_child()
print("左子节点" + str(left_tree.key), "右子节点：" + str(right_tree.key))

right_left_tree = right_tree.get_left_child()
right_right_tree = right_tree.get_right_child()
print("左子节点" + '无', "右子节点："
      + str(right_left_tree.key) + " " + str(right_right_tree.key))


>>>['(', '3', '+', '(', '4', '-', '1', ')', ')']
>>>根节点：+
>>>左子节点3 右子节点：-
>>>左子节点无 右子节点：4 1
```

## 10.图

这次来讨论一下“图”这个数据结构。相比于“树”这个数据结构来说，图是一种更加通用的数据结构，我们可以把树看做是图的一种特殊情况。

### 那么什么是图呢？

在给图下定义之前我们先来联系现实实际问题，以更好的具像的理解图。

![IMG_3786.jpeg](IMG_3786.jpeg)

比如上图为我建立的一个简单的从起始位置到终点位置的路线图。通过分析上图我们可以得出如下结果：



**1.图由许多顶点构成，每一个顶点都可以携带某些信息，并彼此连接。**

**2.图中的一个个顶点是由一个个边连接而成，上图中的边是无方向的，意思就是两边方向都可。而有向边则只能单向流通。此外边上还可携带从一个顶点到另一个顶点所需的花费，即权重。**



下面我们再观察一副图，以此来了解更多图的概念。

![IMG_3788.jpeg](IMG_3788.jpeg)

通过观察上图我们会发现这一次比上次多了许多信息，多了从一个顶点到另一个顶点的花费，这里指的是两个站台之间的距离。另外发现边变成了有向边，只能从一个顶点到另外一个顶点，这是的实际意思是你的公交车所可以停靠的站点。由此我们可以得出一些结论：



**1.通过从起点出发选择一辆公交车，此公交车会经过n个站点最终到达终点，这一过程我们称之为路径，这里因为边是有向的，所以路径是有向路径。**

**2.通过走一条路径，发现起点就是终点时我们称这个路径为环。另外没有环的图被称为无环图，没有环的有向图被称为有向无环图，简称为DAG。**



由此我们基本了解了图的基本组成和概念。接下来就需要抽象的表示它们。在此之前我们先了解一下顶点集和边集。简单来说就是将图中的所有顶点表示在一个集合里面，将所有边表示在一个集合里面。比如下图

![IMG_3789.png](IMG_3789.png)



### 图的抽象数据类型：

❏ Graph()新建一个空图。

❏ addVertex(vert)向图中添加一个顶点实例。

❏ addEdge(fromVert, toVert)向图中添加一条有向边，用于连接顶点fromVert和toVert。

❏ addEdge(fromVert, toVert, weight)向图中添加一条带权重weight的有向边，用于连接顶点fromVert和toVert。

❏ getVertex(vertKey)在图中找到名为vertKey的顶点。

❏ getVertices()以列表形式返回图中所有顶点。

❏ in通过vertex in graph这样的语句，在顶点存在时返回True，否则返回False。



通过邻接矩阵或者邻接表来实现图。

这两种实现中因为顶点点稀疏性导致邻接矩阵花费过大基本不用，因此采用邻接表来实现。

### 图的Python实现

```python
# 图的Python实现

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectTo = {}

    def add_neighbor(self, vertex, weight=0):
        self.connectTo[vertex] = weight

    def __str__(self):
        return str(self.id) + ' connectTo: ' \
            + str([x.id for x in self.connectTo])

    def get_all_connections(self):
        return self.connectTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connectTo[nbr]


# 使用邻接表实现，出于现实问题大多数为稀疏性导致如果使用邻接矩阵会过于浪费资源
class Graph:
    def __init__(self):
        self.vertLi = {}  # id:vertex
        self.vertexCount = 0

    def add_vertex(self, key):
        """
        添加顶点，输入为id-值，输出为顶点对象
        :param key: 输入值
        :return:
        """
        new_vertex = Vertex(key)
        self.vertLi[key] = new_vertex
        self.vertexCount = self.vertexCount + 1
        return new_vertex

    def add_edge(self, fr, to, cost=0):
        """
        向图中添加边，输入为起始顶点值，终点顶点值，完成链接
        :param fr: 起始id-值
        :param to: 终点id-值
        :param cost: 指向耗费
        :return:无
        """
        if fr not in self.vertLi:
            self.add_vertex(fr)
        if to not in self.vertLi:
            self.add_vertex(to)
        self.vertLi[fr].add_neighbor(self.vertLi[to], cost)

    def get_vertex(self, vert_key):
        if vert_key in self.vertLi:
            return self.vertLi[vert_key]
        return None

    def get_all_vertexes(self):
        return self.vertLi.keys()

    def __contains__(self, item):
        return item in self.vertLi

    def __iter__(self):
        return iter(self.vertLi.values())


g = Graph()   # 创建图
for i in range(6):   # 创建五个顶点对象
    g.add_vertex(i)
print(g.vertLi)

# 可以自己将上述顶点在自定义连接，然后再来进行连接操作
g.add_edge(0, 1, 5)
g.add_edge(0, 5, 2)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 9)
g.add_edge(3, 4, 7)
g.add_edge(3, 5, 3)
g.add_edge(4, 0, 1)
g.add_edge(5, 4, 8)
g.add_edge(5, 2, 1)

# 显示图中每一个顶点的连接指向
for v in g:
    for i in v.get_all_connections():
        print(v.get_id(), i.get_id())

```

