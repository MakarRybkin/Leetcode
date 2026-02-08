"""
Сложность в среднем O(logn) в худшем 0(n^2), по памяти O(logn) в этой реализации
Быстрая сортировка
Выбирает рандомное pivot и ставит все элементы меньше его левее. Потом
делает рекурсивно это в правой части и в левой от pivot.
"""

import random

def quicksort(arr, low, high):
    if low < high:
        # Выбираем случайный pivot и меняем его с последним элементом
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Разделяем массив и получаем новый индекс pivot
        pi = partition(arr, low, high)

        # Рекурсивно сортируем левую и правую части
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [5, 2, 9, 1, 5, 6]
quicksort(arr, 0, len(arr) - 1)
print(arr)
