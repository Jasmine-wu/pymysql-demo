class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Single_link_list():
    # node默认值为空，因为可以是空列表，不传节点
    def __init__(self, node=None):
        # 如果空列表，列表里没有头节点
        self.__head = node

    # 头节点
    def is_empty(self):
        return self.__head is None

    def length(self):
        # 从头节点一个一个往后遍历计数
        # 注意特殊情况，空列表的处理cur is not None

        # 如果是空列表，返回0
        if self.is_empty():
            return 0
        cur = self.__head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        # 移动游标遍历，并打印元素
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        # 头部添加节点
        # 新节点指向原头节点,头节点指向新节点
        node = Node(item)
        # 先来新节点指向原头节点，保证原头节点不丢失
        node.next = self.__head
        self.__head = node

    def append(self, item):
        # 尾部添加元素
        # 游标移动到尾节点后面,把节点的next指向append过来的节点
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

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

        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 如果item是头节点元素
                if cur == self.__head:
                    #  删除头节点
                    self.__head = cur.next
                else:
                    # 删除当前节点
                    pre.next = cur.next
                # 找到删除的节点就跳出循环
                break
            else:
                pre = cur
                cur = cur.next

    def research(self, item):
        # 查找元素是否存在
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    sll = Single_link_list()
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