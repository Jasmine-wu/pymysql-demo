
# 选择排序
#  找到最小值下标，跟items[j]交换
def select_sort(items):
    n = len(items)
    for j in range(0,n-1):
        min_index = j
        for i in range(j+1, n):
            if items[min_index] > items[i]:
                min_index = i
        items[j], items[min_index] = items[min_index], items[j]
    return items

print(select_sort([10, 5, 4, 1, 8, 444, 22, 44, 378]))