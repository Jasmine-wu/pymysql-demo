# 快速排序
# 递归:
#     出口
#     推导

# 选择一个基准数，把数列分为大于这个基准数和小于它的两部分，然后再在这部分重复以上动作,直到只剩一个元素
#  最差的情况就是每一次取到的元素就是数组中最小/最大的 O(n^2),也就是冒泡
#  最优：O（nlogn）
#  平均：O(nlogn)
def quick_sort(l: list):
    if len(l) <= 1:
        return l

    # 选择一个基准数
    base = l[0]
    # 注意
    low,high,equal = [],[],[base]
    for item in l[1:]:
        if item > base:
            high.append(item)
        if item < base:
            low.append(item)
        if item == base:
            equal.append(item)
    return quick_sort(low) + equal + quick_sort(high)

if __name__ == '__main__':
    l = [1, 2, 3, 4, 111, 6, 222, 9, 0, 0, 0, 44]
    print(quick_sort(l))
