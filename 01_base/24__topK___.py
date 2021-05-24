# 海量数据处理

import random
import time
n = 10000 * 1000
k = 1000
print(n)
def gen_num(n):
    for i in range(n):
        yield random.randint(0, n)
l = gen_num(n)
print(l)

start = time.time()
l = list(set(l))
result = l[-k:]
result.reverse()
print(time.time()-start)
