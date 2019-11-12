def insert_sort(data_list):
    # get the length of data list
    length = len(data_list)
    for i in range(1, length):
        # previous index
        j = i - 1
        # if current value is less than previous value, then move to previous
        if data_list[i] < data_list[j]:
            temp = data_list[i]
            data_list[i] = data_list[j]
            # continue to move previous
            j -= 1
            while j >= 0 and data_list[j] > temp:
                data_list[j + 1] = data_list[j]
                j -= 1
            # until find the proper place for current value
            data_list[j + 1] = temp
    # return the sorted list from minimum to maximum
    return data_list


def shell_sort(data_list):
    # get the length of data list
    length = len(data_list)
    gap = length // 2
    while gap >= 1:
        # insert sort
        for j in range(gap, length):
            i = j
            while i - gap >= 0:
                if data_list[i] < data_list[i - gap]:
                    data_list[i], data_list[i - gap] = data_list[i - gap], data_list[i]
                    i -= gap
                else:
                    break
        # decrease the gap
        gap //= 2
    # return the sorted list from minimum to maximum
    return data_list


def bubble_sort(data_list):
    # get the length of data list
    length = len(data_list)
    for i in range(0, length - 1):
        for j in range(0, length - 1 - i):
            # compare near two elements and swap them
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    # return the sorted list from minimum to maximum
    return data_list


def quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    # left is smaller than base, while right is bigger than base
    left, right = [], []
    # base element
    base = data_list.pop()
    # partition of original list
    for data in data_list:
        if data < base:
            left.append(data)
        else:
            right.append(data)
    # return the sorted list from minimum to maximum
    return quick_sort(left) + [base] + quick_sort(right)


def select_sort(data_list):
    # get the length of data list
    length = len(data_list)
    for i in range(0, length):
        for j in range(i + 1, length):
            if data_list[i] > data_list[j]:
                data_list[i], data_list[j] = data_list[j], data_list[i]
    # return the sorted list from minimum to maximum
    return data_list


def adjust_heap(data_list, index, length):
    lchild = 2 * index + 1
    rchild = 2 * index + 2
    maxi = index
    if index < length // 2:
        if lchild < length and data_list[lchild] > data_list[maxi]:
            maxi = lchild
        if rchild < length and data_list[rchild] > data_list[maxi]:
            maxi = rchild
        if maxi != index:
            data_list[maxi], data_list[index] = data_list[index], data_list[maxi]
            adjust_heap(data_list, maxi, length)


def build_heap(data_list):
    # get the length of data list
    length = len(data_list)
    for i in range(0, length // 2)[::-1]:
        adjust_heap(data_list, i, length)


def heap_sort(data_list):
    # get the length of data list
    length = len(data_list)
    build_heap(data_list)
    for i in range(0, length)[::-1]:
        data_list[0], data_list[i] = data_list[i], data_list[0]
        adjust_heap(data_list, 0, i)
    return data_list


def merge(left_list, right_list):
    result = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    result += left_list[i:]
    result += right_list[j:]
    return result


def merge_sort(data_list):
    # get the length of data list
    length = len(data_list)
    if length <= 1:
        return data_list
    mid = length // 2
    left_list = merge_sort(data_list[:mid])
    right_list = merge_sort(data_list[mid:])
    return merge(left_list, right_list)
