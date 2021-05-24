# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
# 时间复杂度：不同机器上运行相同的程序执行时间是不一样的，所以不能用执行时间衡量，用时间复杂度：运算步骤的数量

# 时间复杂度： 描述算法的执行效率
import time

# emum 枚举法 :最笨的方法
start_time = time.time()
for a in range(0, 1000):
    for b in range(0, 1000):
        c = 1000 - a - b
        if a + b + c == 1000 and a ^ 2 + b ^ 2 == c ^ 2:
            print("a, b, c :%d, %d ,%d" % (a, b, c))
T = 1000 * 1000 * 3
# 时间复杂度（运算的步骤），n（解决问题的规模）
# T(n) = n^2 * 3; T(n)这个函数就叫时间复杂度
# 时间复杂度的大O表示法
# g(n) = n^2 , g(n)是T(n)的渐进函数（去掉系数）; g(n)这个函数时间复杂度的大O表示法，记为：O(n^2)
end_time = time.time()
time = end_time - start_time
print("running time is : %d" % (time))
print("time complexity is %d", T)

# 我们通常所说的时间复杂度，指的是最坏时间复杂度。

# 数据结构：数据的组织方式
# name
# age
# hometown

[
    ("zhangsan", 24, "beijing"),
    ("zhangsan", 24, "beijing"),
    ("zhangsan", 24, "beijing"),
]

[
    {
        "name": "zhangsan",
        "age": "14",
        "hometown": "beijing",

    }
]

{
    "zhangsan": {
    "age": 14,
    "hometown": "biejing"
    }
}
