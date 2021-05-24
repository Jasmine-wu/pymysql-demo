
# 两个栈实现一个队列

class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def put(self, item):
        self.stack1.append(item)

    def get(self):
        if len(self.stack1) == 0:
            return None

        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        value = self.stack2.pop()

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return value


if __name__ == '__main__':

    queue = Queue()
    for i in range(0,10):
        queue.put(i)
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())

