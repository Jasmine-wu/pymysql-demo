# 用什么来实现栈？列表
# 尾进头出
# 如何进的如何出
class Queue():
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        return self.__items.append(item)

    def dequeue(self):

        return self.__items.pop(0)

    def size(self):
        return len(self.__items)


if __name__ == "__main__":

    s = Queue()
    print(s.size())
    print(s.is_empty())
    print(s.dequeue())

    s.enqueue("zhangsan1")
    s.enqueue("zhangsan2")
    s.enqueue("zhangsan3")

    print(s.size())
    print(s.is_empty())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.size())



