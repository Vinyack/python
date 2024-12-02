from collections import defaultdict

def process_sales(data):
    # Используем вложенный defaultdict для хранения товаров и их количества для каждого покупателя
    sales = defaultdict(lambda: defaultdict(int))
    
    # Обработка каждой записи в данных
    for entry in data:
        buyer, product, quantity = entry.split()
        quantity = int(quantity)
        sales[buyer][product] += quantity  # Суммируем количество товара для каждого покупателя

    # Формирование вывода в требуемом формате
    result = []
    for buyer in sorted(sales):  # Сортируем покупателей в лексикографическом порядке
        result.append(f"{buyer}:")
        for product in sorted(sales[buyer]):  # Сортируем товары в лексикографическом порядке
            result.append(f"  {product} {sales[buyer][product]}")
    
    return "\n".join(result)

# Пример данных

data = [
    "Ivanov paper 10",
    "Petrov pens 5",
    "Ivanov marker 3",
    "Ivanov paper 7",
    "Petrov envelope 20",
    "Ivanov envelope 5"
]

# Вывод результата
print(process_sales(data))
