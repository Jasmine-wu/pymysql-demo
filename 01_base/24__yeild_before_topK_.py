# 生成器
#  函数返回值关键字是yeild而不是return，那么这个函数就是一个生成器函数
# 以 list 容器为例，在使用该容器迭代一组数据时，必须事先将所有数据存储到容器中，才能开始迭代；
# 而生成器却不同，它可以实现在迭代的同时生成元素。
import random
import time
import heapq


def generator():
    print("开始执行")
    for i in range(0, 10):
        print("执行，", i)
        yield i  # next执行到到这里程度就停止了，且程序
        print("yeild后执行", i)
# print(generator()) # 生成器
# yield 关键字出现的时候程序就已经暂停执行了，整个函数成了一个生成器函数。
# 调用生成器函数，Python 解释器也不会执行函数中的代码，它只会返回一个生成器（对象）
# 所以调用generator()也没有出现打印:执行， 0，更没有打印，开始执行
# 当调用__next__整个生成器函数才开始执行，或者使用for循环
# 碰到yeild运行停止，且记住了这个位置，下次__next__会从这个位置开始继续执行

g = generator() # 啥也没打印
g.__next__()
# 开始执行
# 执行， 0
g.__next__()
# yeild后执行 0
# 执行， 1
g.__next__()
# yeild后执行 1
# 执行， 2

# 可以使用list或者tuple直接将生成器能生成的值存储成列表和元祖的形式
a = generator()
al = list(a)
print(al)

# ==================== 生成海量数据1000w
n = 10000 * 100
k = 10000


def gen(n):
    for i in range(n):
        yield random.randint(0, n)

# 不考虑内存取前10000个数据
start = time.time()
data = list(gen(n))
piece = data[:k]
print(time.time() - start)

# 使用python自带的堆排可以节省一点内存
start = time.time()
# 取最大的k个数
result = heapq.nlargest(k, data)
print(time.time() - start)


# ============= 大文件按块读取=====
# 1KB = = 2^10B= 1024B
# 1MB = 1024KB = 1024 * 1024
# 1GB = 1024MB = 1024 * 1024 * 1024

def read_file(file_path, size=1024 * 1024):
    with open(file_path, 'r', encoding="utf-8") as f:
        while True:
            block = f.read(size)
            if block:
                yield block
            else:
                return

for i in read_file():
    # 把大文件分成1M的小文件,对小的文件进行字符串统计:

    # 统计某个字符出现了次数
    l = list(set(i))
    # count = l.count("www.baidu.com")
    # result = [(item, l.count(item)) for item in l]


