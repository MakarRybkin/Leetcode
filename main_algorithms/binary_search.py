"""
 Сложность O(log(n))

 Находит число в отсортированном массиве
 или находит граничное значение когда условие(другая функция) выполняется или не
 выполняется например в 000001111

 Обычно используется в комбинауии с другим алгоритмом
"""

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid # в этой задаче возвращает индекс массива, где находится target
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return False
test_case1 = [1,4,5,6,7]
print(binary_search(test_case1, 5)) # возвращает index = 2
print(binary_search(test_case1, 100)) # возвращает False, 100 в массиве нет

"""
Встроенный модуль
"""
import bisect
def contains(nums, target):
    index = bisect.bisect_left(nums, target) # ищет место для вставки target как можно левее
    if index < len(nums):
        return nums[index] == target
    return False
print(contains(test_case1, 100))
