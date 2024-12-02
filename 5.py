def calculate_strikes(N, K, parties):
    # Инициализируем список дней, чтобы отслеживать забастовки (сначала все False)
    days = [False] * (N + 1)  # Индексы от 1 до N включительно

    # Обрабатываем каждую партию
    for a, b in parties:
        day = a
        while day <= N:
            # Забастовки учитываются только в будние дни (1 - Понедельник, 6 - Суббота, 7 - Воскресенье)
            if day % 7 != 6 and day % 7 != 0:  # Игнорируем Субботу и Воскресенье
                days[day] = True
            day += b  # Переходим к следующему дню забастовки для этой партии

    # Подсчитываем количество дней забастовок
    return sum(days)

# Ввод данных
N, K = map(int, input("Введите N и K: ").split())
parties = []
for _ in range(K):
    a, b = map(int, input("Введите a и b для партии: ").split())
    parties.append((a, b))

# Вычисляем и выводим результат
result = calculate_strikes(N, K, parties)
print("Число забастовок:", result)
