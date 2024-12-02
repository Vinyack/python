def calculate_min_cost_delivery(N, V, points):
    # points - список кортежей (расстояние, количество пробирок)
    # Сортируем точки по расстоянию
    points.sort()
    
    # Вычисляем суммарное количество пробирок
    total_samples = sum(count for _, count in points)
    
    # Ищем позицию медианы
    cumulative_samples = 0
    for distance, count in points:
        cumulative_samples += count
        # Позиция медианы находится, когда набралась половина пробирок
        if cumulative_samples >= (total_samples + 1) // 2:
            optimal_position = distance
            break

    # Считаем минимальную стоимость для оптимального положения лаборатории
    min_cost = sum(abs(distance - optimal_position) * count for distance, count in points)
    
    return min_cost

# Ввод данных
N = int(input("Введите количество пунктов приёма N: "))
V = int(input("Введите вместимость контейнера V: "))
points = []
for _ in range(N):
    distance, count = map(int, input("Введите расстояние и количество пробирок через пробел: ").split())
    points.append((distance, count))

# Вычисляем и выводим результат
result = calculate_min_cost_delivery(N, V, points)
print("Минимальная стоимость доставки:", result)
