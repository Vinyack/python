import pandas as pd
from collections import Counter
import statistics

def analyze_string(input_string):
    # Задача 1: Разница между средним количеством согласных и гласных
    vowels = set("аеёиоуыэюяaeiouy")
    consonants = set("бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz")
    
    vowel_count = sum(1 for char in input_string.lower() if char in vowels)
    consonant_count = sum(1 for char in input_string.lower() if char in consonants)
    avg_difference = abs(vowel_count - consonant_count)
    
    # Задача 5: Квадратичное отклонение частоты символов
    char_frequencies = Counter(input_string)
    total_chars = len(input_string)
    frequencies = [count / total_chars for count in char_frequencies.values()]
    variance = statistics.variance(frequencies) if len(frequencies) > 1 else 0

    # Задача 9: Квадратичное отклонение между ASCII кодами
    ascii_codes = [ord(char) for char in input_string]
    reversed_ascii_codes = ascii_codes[::-1]
    differences = [(ascii_codes[i] - reversed_ascii_codes[i])**2 for i in range(len(ascii_codes) // 2)]
    ascii_variance = statistics.mean(differences) if differences else 0

    # Задача 10: Среднее количество "зеркальных" троек
    mirror_count = 0
    for i in range(len(input_string) - 2):
        if input_string[i] == input_string[i + 2]:
            mirror_count += 1
    avg_mirror_triples = mirror_count / (len(input_string) - 2) if len(input_string) > 2 else 0

    return {
        "Строка": input_string,
        "Разница между согласными и гласными": avg_difference,
        "Квадратичное отклонение частоты символов": variance,
        "Квадратичное отклонение ASCII кодов": ascii_variance,
        "Среднее количество зеркальных троек": avg_mirror_triples,
    }

if __name__ == "__main__":
    print("Введите строки для анализа. Для завершения ввода оставьте строку пустой.")
    strings = []
    while True:
        line = input("Введите строку: ")
        if not line:  # Пустая строка завершает ввод
            break
        strings.append(line)

    # Анализ строк
    results = [analyze_string(s) for s in strings]
    df = pd.DataFrame(results)

    # Сортировка и вывод результатов для каждой задачи
    tasks = [
        "Разница между согласными и гласными",
        "Квадратичное отклонение частоты символов",
        "Квадратичное отклонение ASCII кодов",
        "Среднее количество зеркальных троек",
    ]

    for task in tasks:
        print(f"\nРезультаты для задачи: {task}")
        sorted_df = df.sort_values(by=task)
        print(sorted_df[["Строка", task]].to_string(index=False))
