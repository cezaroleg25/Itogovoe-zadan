def is_monotonic(nums):
    increasing = decreasing = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False
    return increasing or decreasing

# Ввод данных от пользователя
if __name__ == '__main__':
    input_str = input("Введите элементы массива через пробел: ")
    nums = list(map(int, input_str.split()))
    result = is_monotonic(nums)
    print(f"Массив {nums} {'является' if result else 'не является'} монотонным")