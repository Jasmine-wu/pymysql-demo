# L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]，用一行代码得出 [11, 1, 2, 3, 5]
# 列表去重(不考虑顺序)set()

def test1():
    L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
    print(list(set(L)))


# 考虑顺序(用set()优化not in，not in的效率比in要差)
def test2():
    L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
    s = set()
    result = []
    for item in L:
        if item in s:
            continue
        s.add(item)
        result.append(item)
    print(result)


# 一串字母数字组合的字符串，找出相同的字母或数字，并按照个数排序。
def test3():
    l = [1, 2, 3, 'a', 'b', 'c', 1, 2, 'a', 'b', 3, 'c', 'd', 'a', 'b', 1]
    set1 = set(l)
    result = [(item, l.count(item)) for item in set1]
    print(result)
    result.sort(key=lambda x:x[1], reverse=False)
    print(result)


# L = [1, 2, 3, 4, 5]，L[10:]的结果是？
# L = [1, 2, 3, 4, 5]
# print(L[10:]) # 空数组

# L= [1, 2, 3, 5, 6]，如何得出 '12356'？
# L= [1, 2, 3, 5, 6]
# s = ''
# for i in L:
#     s = s + str(i)
# print(s)


def testlambda(n):
    return lambda a: a * n


if __name__ == '__main__':

    print(testlambda(5)(10))
    test3()



# 7、列表和字典有什么区别？
# （1）获取元素的方式不同。列表通过索引值获取，字典通过键获取。
# （2）数据结构和算法不同。字典是hash算法，搜索的速度特别快。
# （3）占用的内存不同。

# 9、进程、线程有什么区别？什么情况下用进程？什么情况下用线程？
# 答：（1）区别：
#
# ① 地址空间和其它资源（如打开文件）：进程之间相互独立，同一进程的各线程之间共享。某进程内的线程在其它进程不可见。
# ② 通信：进程间通信 IPC，线程间可以直接读写进程数据段（如全局变量）来进行通信——需要进程同步和互斥手段的辅助，以保证数据的一致性。
# ③ 调度和切换：线程上下文切换比进程上下文切换要快得多。
# ④ 在多线程操作系统中，进程不是一个可执行的实体。

# 11、写一段代码，ping 一个 ip地址，并返回成功、失败的信息
# 答： 使用 subProcess 模块的 Popen 方法(使用简单，具体用法，这里不展开)。
# 12、说说接口测试的流程，介绍一下 request 有哪些内容。
# 答：
# （1）流程：获取接口文档，依据文档设计接口参数，获取响应，解析响应，校验结果，判断测试是否通过。
# （2）request 内容：
#
# ① 封装了各种请求类型，get、post 等；
# ② 以关键字参数的方式，封装了各种请求参数，params、data、headers、token 等；
# ③ 封装了响应内容，status_code、json()、cookies、url 等；
# ④ session 会话对象，可以跨请求。
