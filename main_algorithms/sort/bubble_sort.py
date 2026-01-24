"""
Сложность O(n^2)

Переставляет i и i+1 эелемент и в итоге прохода по всему массиву справа остается max элемент
и так нужно n раз пройтись

Лучше использовать quick_sort
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

my_list = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(my_list))