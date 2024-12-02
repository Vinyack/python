# Функция для проверки строки на палиндром
def is_palindrome(s):
    # Удаляем пробелы и переводим строку в нижний регистр
    cleaned_str = ''.join(s.split()).lower()
    # Сравниваем строку с её обратной версией
    return cleaned_str == cleaned_str[::-1]

# Функция для подсчёта количества слов в строке
def count_words(s):
    # Разделяем строку на слова и возвращаем их количество
    return len(s.split())

# Функция для подсчёта количества уникальных цифр в числе
def count_unique_digits(n):
    # Преобразуем число в строку и создаём множество уникальных цифр
    unique_digits = set(str(n))
    # Возвращаем количество уникальных цифр
    return len(unique_digits)

# Основной код
if __name__ == "__main__":
    # Задача 1: Проверка на палиндром
    print("Задача 1: Проверка на палиндром")
    palindrome_input = input("Введите строку для проверки: ")
    is_palindrome_result = is_palindrome(palindrome_input)
    print(f"Строка: \"{palindrome_input}\" - палиндром: {is_palindrome_result}")

    # Задача 2: Подсчёт слов
    print("\nЗадача 2: Подсчёт слов")
    sentence_input = input("Введите строку для подсчёта слов: ")
    word_count_result = count_words(sentence_input)
    print(f"Количество слов в строке: {word_count_result}")

    # Задача 3: Подсчёт различных цифр
    print("\nЗадача 3: Подсчёт различных цифр")
    number_input = input("Введите натуральное число: ")

    # Проверяем, является ли введённое значение натуральным числом
    if number_input.isdigit():
        unique_digit_count_result = count_unique_digits(number_input)
        print(f"Количество различных цифр в числе {number_input}: {unique_digit_count_result}")
    else:
        print("Ошибка: Введено не натуральное число.")
