def binary_search(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        # Считаем середину.
        # (low + high) // 2 может вызвать переполнение в некоторых языках,
        # поэтому вариант ниже считается более безопасным:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid  # Нашли!
        elif nums[mid] < target:
            low = mid + 1  # Ищем в правой половине
        else:
            high = mid - 1  # Ищем в левой половине

    return -1  # Не нашли
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))