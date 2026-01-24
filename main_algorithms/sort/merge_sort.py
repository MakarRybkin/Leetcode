"""
Сложность O(nlog(n))

Разделяем массив наполовину пока не получится только по одному элементу в массиве



Неплохая сортировка на собеседовании, но в проде timsort

"""

def merge_sort(arr):
    """ Разделяет массив рекурсивно"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    """ Сливает все в один массив с помошью сравнений по двум указателям"""
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    elif j < len(right):
        merged.extend(right[j:])
    return merged


print(merge_sort([5, 4, 3,8,234, 2, 1]))