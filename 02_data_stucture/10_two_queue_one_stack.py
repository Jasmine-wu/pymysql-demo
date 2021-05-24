# 两个队列实现一个栈#
# 队列是先入先出，栈是先入后出。
# 使用两个队列实现栈的方式有很多种，主要分为优化入栈和优化出栈两种，以下为优化入栈的一种实现方法。
# 入栈时直接存入队列q1
# 出栈时，将q1中元素依次放入q2, 直到最后一个元素，弹出元素，然后将q2中元素重新依次放回q1
import queue


class Stack():
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, item):
        self.q1.put(item)

    def pop(self):
        # q1放入q2，除了最后一个
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        #至此，q1只剩了最后一个数，因为队列是先进先出，get()弹出的是前面数
        value = self.q1.get()

        #此时q1为nil,如果q2不为空，继续把q2给q1，为了下次下次pop
        while not self.q2.empty():
            self.q1.put(self.q2.get())

        return value


if __name__ == '__main__':
    s = Stack()
    for i in [1, 2, 3, 4, 5, 6, 7]:
        s.push(i)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())



    # 队列是先入先出 get()队列最开始入队列的数
    # q1 = queue.Queue()
    # for i in [1, 2, 3, 4, 5, 6, 7]:
    #     q1.put(i)
    # print(q1.queue)
    # print(q1.get())
    # print(q1.queue)
    # print(q1.qsize())
