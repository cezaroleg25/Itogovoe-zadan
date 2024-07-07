def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in reversed(s):
        value = roman[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

# Ввод данных от пользователя
if __name__ == '__main__':
    roman_numeral = input("Введите римское число: ")
    result = roman_to_int(roman_numeral)
    print(f"Значение {roman_numeral} в десятичной системе: {result}")