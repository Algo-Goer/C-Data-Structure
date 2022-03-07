def binary_search(list, item):
    low = 0
    high = len(list) - 1  # low和high用于跟踪要在其中查找的列表的部分
    while low <= high:    # 只要范围没有缩小到只包含一个元素
        mid = (low + high) / 2  # 就检查中间元素
        guess = list[mid]
        if guess == item:   # 找到了元素
            return mid
        if guess > item:  # 猜的数字大了
            high = mid - 1
        else:
            low = mid + 1
    return None  # 没有指定元素

# test
my_list = [1, 3, 5, 7, 9]

print binary_search(my_list, 3) # 索引从0开始,第2个位置的索引为1
print binary_search(my_list, -1) # None