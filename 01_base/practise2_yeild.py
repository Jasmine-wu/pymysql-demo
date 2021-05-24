# 海量数据top K#
# 对于小数据量可以使用排序+切片，而对于海量数据，需要考虑服务器硬件条件。即要考虑时间效率，也要考虑内存占用，同时还要考虑数据特征。如果大量的重复数据，可以先用哈希进行去重来降低数据量。
# 这里我们使用生成器生成1000万个随机整数，求最大的1000个数，生成随机数的代码如下：
import heapq
import random
import time
# 文件读取
def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

# 斐波那契数列
# 除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
print(fab(5))
for n in fab(5):
    print(n)


# 生成海量数据,这里我们生成1000万个随机整数，求最大的1000个数
def gen_num(n):
    for i in range(n):
        yield random.randint(0, n)

def get_max(n):
    l = gen_num(1000)
    # 去重
    l = list(set(l))

    start = time.time()

    # 获取最大值Python自带的堆排库heapq。使用nlargest(k,l)可以取到l序列，最大的k个数
    result = heapq.nlargest(2,l)

    print("*"*50)
    print(result)
    print(time.time() - start)


if __name__ == '__main__':


    get_max(1000)


