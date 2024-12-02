from collections import Counter

# Задача 6: Циклический сдвиг элементов массива влево на три позиции
def shift_left(arr, positions=3):
    return arr[positions:] + arr[:positions]

# Задача 18: Найти элементы, расположенные перед первым минимальным элементом массива
def elements_before_first_min(arr):
    min_index = arr.index(min(arr))
    return arr[:min_index]

# Задача 30: Определить, является ли элемент по указанному индексу локальным максимумом
def is_local_maximum(arr, index):
    if index <= 0 or index >= len(arr) - 1:
        return False, None  # Не имеет соседей слева или справа для сравнения
    if arr[index] > arr[index - 1] and arr[index] > arr[index + 1]:
        return True, arr[index]  # Возвращаем True и значение локального максимума
    return False, None

# Задача 42: Найти все элементы, которые меньше среднего арифметического элементов массива
def elements_less_than_average(arr):
    avg = sum(arr) / len(arr)
    return [x for x in arr if x < avg], avg

# Задача 54: Построить список из элементов, встречающихся в исходном списке более трех раз
def elements_more_than_three_times(arr):
    counts = Counter(arr)
    return [elem for elem, count in counts.items() if count > 3]

# Функция для выполнения всех задач
def execute_all_tasks(arr):
    tasks_results = {}
    tasks_results["Задача 6: Циклический сдвиг влево"] = shift_left(arr)
    tasks_results["Задача 18: Элементы перед первым минимальным"] = elements_before_first_min(arr)
    if len(arr) > 2:
        is_max, value = is_local_maximum(arr, index=1)
        tasks_results["Задача 30: Локальный максимум (индекс 1)"] = f"{is_max}, значение: {value}" if is_max else "Локального максимума нет"
    else:
        tasks_results["Задача 30: Локальный максимум (индекс 1)"] = "Недостаточно данных"
    less_than_avg, avg = elements_less_than_average(arr)
    tasks_results[f"Задача 42: Элементы меньше среднего (среднее: {avg:.2f})"] = less_than_avg
    tasks_results["Задача 54: Элементы более 3 раз"] = elements_more_than_three_times(arr)
    return tasks_results

# Основная функция main
def main():
    try:
        arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
        results = execute_all_tasks(arr)
        for task, result in results.items():
            print(f"{task}: {result}")
    except ValueError:
        print("Ошибка ввода! Убедитесь, что вы вводите числовые значения.")

# Вызов функции main, если скрипт запускается напрямую
if __name__ == "__main__":
    main()
