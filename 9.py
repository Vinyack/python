import math

# Базовый класс для фигур
class Shape:
    def __init__(self, identifier, coordinates):
        if not isinstance(identifier, str):
            raise ValueError("Identifier должен быть строкой.")
        if len(coordinates) < 3:
            raise ValueError("Фигура должна иметь минимум 3 вершины.")
        self.identifier = identifier
        self.coordinates = coordinates  # Список кортежей (x, y)

    def move(self, dx, dy):
        """Перемещение фигуры на вектор (dx, dy)."""
        self.coordinates = [(x + dx, y + dy) for x, y in self.coordinates]

    def is_intersect(self, other):
        """Проверка пересечения двух фигур."""
        if not isinstance(other, Shape):
            raise TypeError("Аргумент должен быть экземпляром класса Shape.")
        return any(self._point_inside(p, other) for p in self.coordinates) or \
               any(self._point_inside(p, self) for p in other.coordinates)

    def _point_inside(self, point, shape):
        """Определение, находится ли точка внутри фигуры (алгоритм Ray Casting)."""
        x, y = point
        n = len(shape.coordinates)
        inside = False
        px, py = shape.coordinates[-1]
        for i in range(n):
            sx, sy = shape.coordinates[i]
            if ((sy > y) != (py > y)) and (x < (px - sx) * (y - sy) / (py - sy) + sx):
                inside = not inside
            px, py = sx, sy
        return inside

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.identifier}, coords={self.coordinates})"

# Класс для треугольников
class Triangle(Shape):
    def __init__(self, identifier, coordinates):
        if len(coordinates) != 3:
            raise ValueError("Треугольник должен иметь ровно 3 вершины.")
        super().__init__(identifier, coordinates)

# Класс для пятиугольников
class Pentagon(Shape):
    def __init__(self, identifier, coordinates):
        if len(coordinates) != 5:
            raise ValueError("Пятиугольник должен иметь ровно 5 вершин.")
        super().__init__(identifier, coordinates)

# Пример использования
if __name__ == "__main__":
    try:
        # Создание объектов
        triangle = Triangle("T1", [(0, 0), (1, 0), (0, 1)])
        pentagon = Pentagon("P1", [(0, 0), (2, 0), (2, 2), (1, 3), (0, 2)])

        print("Начальные фигуры:")
        print(triangle)
        print(pentagon)

        # Перемещение треугольника
        triangle.move(1, 1)
        print("\nПосле перемещения треугольника:")
        print(triangle)

        # Проверка пересечения
        intersect = triangle.is_intersect(pentagon)
        print("\nФигуры пересекаются:" if intersect else "\nФигуры не пересекаются")

        # Обработка ошибок
        try:
            invalid_triangle = Triangle("T2", [(0, 0), (1, 0)])  # Ошибка
        except ValueError as e:
            print("\nОшибка при создании треугольника:", e)

    except Exception as e:
        print("Общая ошибка:", e)
