def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Ввод данных от пользователя
if __name__ == '__main__':
    n = int(input("Введите количество чисел Фибоначчи для генерации: "))
    print(f"Первые {n} чисел Фибоначчи:")
    for num in fib(n):
        print(num)