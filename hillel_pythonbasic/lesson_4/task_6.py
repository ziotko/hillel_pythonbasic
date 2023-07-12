def count_elements(nums):
    count = 0

    for i in range(1, len(nums) - 1):
        if nums[i] <= nums[i - 1] or nums[i] <= nums[i + 1]:
            continue
        count += 1

    return count


numbers = [1, 3, 2, 5, 4, 7, 6]
result = count_elements(numbers)
print("Количество элементов, которые больше двух своих соседей:", result)
