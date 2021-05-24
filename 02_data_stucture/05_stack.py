# 用什么来实现栈？
# 先进后出
class Stack():
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty():
            return
        else:
            return self.__items.pop()

    def size(self):
        return len(self.__items)

    # 返回栈顶
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__items[-1]


if __name__ == "__main__":

    s = Stack()
    print(s.size())
    print(s.is_empty())
    s.pop()
    print(s.peek())

    s.push("zhangsan")
    s.push("lisi")
    s.push("wanger")
    print(s.pop())
    print(s.pop())
    print(s.pop())


    print(s.size())
    print(s.is_empty())
    print(s.peek())


