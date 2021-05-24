class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# 单向循环列表，尾节点next指向头节点
# 单向列表，尾节点next指向空

class Single_cycle_link_list():
    # node默认值为空，因为可以是空列表，不传节点
    def __init__(self, node=None):
        # 如果空列表，列表里没有头节点
        self.__head = node
        if node:
            # 只有一个节点的情况：头节点指向node节点，并且node节点的next指向自己
            node.next = node

    # 头节点
    def is_empty(self):
        return self.__head is None

    def length(self):
        # 从头节点一个一个往后遍历计数
        # 注意特殊情况：
        # 1.空列表的处理
        # 2. 列表中只有一个节点的处理
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        # 移动游标遍历，并打印元素
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环：尾节点指向头节点时退出循环，但尾节点元素未打印
        print(cur.elem)

    def add(self, item):
        # 头部添加节点
        # 新节点指向原头节点,头节点指向新节点
        node = Node(item)

        # 如果列表一开始是空列表
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 列表不为空
            # 先来新节点next指向原头节点，保证原头节点不丢失
            node.next = self.__head

            # 设置游标用于遍历节点
            cur = self.__head

            # 找到原尾节点next指向新节点
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node

            #  把新节点设置为头节点
            self.__head = node

    def append(self, item):
        # 尾部添加元素
        # 游标移动到尾节点后面,把节点的next指向append过来的节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 跳出循环cur就是尾节点了
            # 尾节点next指向插入node，并将插入node的next指向头节点
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        #  找到插入的前一个节点,把前节点原指向的next给新节点
        # 新节点就指向了原前节点的后一个节点
        # 把前节点的next指向新节点
        #  另外还要处理过界问题

        if pos <= 0:
            # 头插
            self.add(item)
        elif pos > self.length() - 1:
            # 尾插
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            # 找到插入的前一个节点
            while count < pos - 1:
                pre = pre.next
                count += 1
            # 把前节点原指向的next给新节点，新节点就指向了原前节点的后一个节点
            node.next = pre.next
            # 把前节点的next指向新节点
            pre.next = node

    def remove(self, item):
        # 要有来个游标cur当前节点,pre前节点
        # cur指向头节点
        # pre是头节点之前的节点，最开始为None
        # 对头节点进行特殊处理
        # 尾节点进行特殊处理

        # 几种情况：空列表，列表只有一个节点，删除的刚好是头节点，其他情况
        # 空列表
        if self.is_empty():
            return

        cur = self.__head
        pre = None

        #
        while cur.next != self.__head:
            if cur.elem == item:
                # 如果item是头节点元素
                if cur == self.__head:
                    #  删除原头节点
                    self.__head = cur.next
                    #  找尾节点
                    cur2 = self.__head
                    while cur2.next != self.__head:
                        cur2 = cur2.next

                    # 退出循环，找到尾节点
                    # 尾节点next指向新头节点
                    cur2.next = self.__head

                else:
                    # 删除当前节点
                    pre.next = cur.next
                # 找到删除的节点跳出整个函数
                return
            else:
                pre = cur
                cur = cur.next

        # 退出循环，cur指向尾节点
        if cur.elem == item:
            # 如果列表只有一个节点
            if cur == self.__head:
                # 删除当前节点
                self.__head = None
            else:
                pre.next = cur.next

    def research(self, item):
        # 空列表
        if self.is_empty():
            return False

        # 查找元素是否存在
        cur = self.__head
        # cur.next != self.__head 这里会漏掉尾节点
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next

        # 循环退出对尾节点进行处理
        if cur.elem == item:
            return True

        return False

if __name__ == "__main__":
    sll = Single_cycle_link_list()
    print(sll.is_empty())
    print(sll.length())

    sll.append(10)
    print(sll.is_empty())
    print(sll.length())

    sll.append(11)
    sll.append(12)
    sll.append(13)

    sll.add(59)
    sll.add(60)

    sll.insert(-1, -1)
    sll.insert(0, 0)
    sll.insert(100, 100)

    print(sll.length())
    sll.travel()

    print(sll.research(-1))
    print(sll.research(1000))

    sll.remove(0)
    sll.travel()

    sll.remove(100)
    sll.travel()