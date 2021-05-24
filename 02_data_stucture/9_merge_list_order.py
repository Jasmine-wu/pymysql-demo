# 合并两个有序列表，并保持有序#
# 常见的解法有两种：
#
# 连接 + 排序，时间复杂度度为O((m+n)log2(m+n))
# 两个队列根据大小依次弹出，时间复杂度度约为O(m+n)
# 依次出队列的逻辑为：
#
# 队列1为空，队列2不为空，从队列2弹出一个数据
# 队列2为空，队列1不为空，从队列1弹出一个数据
# 两个都不为空，判断两个对队列顶端哪个小，从哪个列表弹出一个数据


def merge_list_order(l1, l2):
    result = []
    n = len(l1) + len(l2)
    for i in range(0,n):
        # 如果l1不为空，且l2为空
        if l1 and not l2:
            result.append(l1.pop())
        # 如果l2不为空，且l1为空
        elif l2 and not l1:
            result.append(l2.pop())
        else:
            if l1[-1] > l2[-1]:
                result.append(l1.pop())
            else:
                result.append(l2.pop())
    result.reverse()
    return result


list3 = [100,3,99,5, 6,8,10,12,14]
list3.sort(reverse=True)
print(list3)
list3.reverse()
print(list3)


if __name__ == '__main__':
    list1 = [1,5,7,9]
    list2 = [2,3,4,5, 6,8,10,12,14]
    print(merge_list_order(list1, list2))
