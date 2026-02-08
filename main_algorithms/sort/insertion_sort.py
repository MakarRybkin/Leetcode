"""
Сортировка вставками
Берет число из начального массива и вставляет его в новый отсорттрованный,
идя с конца.

Сложность по времени O(n^2) по памяти O(1)
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [5, 2, 9, 1, 5, 6]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
