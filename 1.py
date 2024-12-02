from math import gcd
from functools import reduce

# Функция для вычисления наименьшего общего кратного (НОК)
def lcm(x, y):
    return x * y // gcd(x, y)

# Функция проверки на взаимную простоту
def is_coprime(a, b):
    return gcd(a, b) == 1

# Функция для нахождения количества чётных чисел, не взаимно простых с данным
def find_even_not_coprime(numbers, given):
    return sum(1 for num in numbers if num % 2 == 0 and not is_coprime(num, given))

# Функция для нахождения максимальной цифры числа, не делящейся на 3
def max_digit_not_divisible_by_3(n):
    return max((int(digit) for digit in str(n) if int(digit) % 3 != 0), default=-1)

# Функция для нахождения произведения максимального числа и суммы цифр
def product_of_max_and_sum(numbers, given):
    # Нахождение НОД всех чисел в списке
    min_gcd = reduce(gcd, numbers)
    
    # Нахождение максимального числа, удовлетворяющего условиям
    max_non_coprime = max(
        (num for num in numbers if not is_coprime(num, given) and num % min_gcd != 0), 
        default=None
    )
    
    # Сумма цифр числа, которые меньше 5
    sum_of_digits_less_than_5 = sum(int(digit) for digit in str(given) if int(digit) < 5)
    
    # Возвращаем произведение, если найдено подходящее число, иначе None
    return max_non_coprime * sum_of_digits_less_than_5 if max_non_coprime is not None else None

# Основной код
if __name__ == "__main__":
    given_number = 30
    numbers = [10, 20, 25, 50, 15, 6, 12]

    # Задача 1: Найти количество чётных чисел, не взаимно простых с заданным числом
    count_even_not_coprime = find_even_not_coprime(numbers, given_number)
    print(f"Количество чётных чисел, не взаимно простых с {given_number}: {count_even_not_coprime}")

    # Задача 2: Найти максимальную цифру числа, не делящуюся на 3
    max_digit = max_digit_not_divisible_by_3(given_number)
    print(f"Максимальная цифра числа {given_number}, не делящаяся на 3: {max_digit}")

    # Задача 3: Найти произведение максимального числа и суммы цифр
    result_product = product_of_max_and_sum(numbers, given_number)
    print(f"Произведение: {result_product}")
