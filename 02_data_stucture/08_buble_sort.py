
# O（n^2）
#  冒泡排序的优化: [1,2,3,4] 顺序排列，则跳出循环
#  优化以后:O(n)
def bubble_sort(items):
    n = len(items)
    # 控制循环多少次
    count = 0
    for i in range(0, n-1):
        #  每次循环到哪里
        for j in range(n-1-i):
            if items[j] > items[j+1]:
                items[j+1], items[j] = items[j], items[j+1]
                # 发生了交换就+1
                count += 1
        # 如果一次也没交换，说明数据是顺序排列的
        if count == 0:
            return items
    return items

print(bubble_sort([1,2,3,4,5,6]))
print(bubble_sort([100, 44, 2, 100, 7, 8, 1, 0, 22]))