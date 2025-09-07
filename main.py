from shapes import Circle, Triangle, calculate_area

# Создание фигур
circle = Circle(7)
triangle = Triangle(7, 4, 5)

# Вычисление площадей
print(f"Площадь круга: {calculate_area(circle)}")
print(f"Площадь треугольника: {calculate_area(triangle)}")

# Проверка прямоугольного треугольника
if triangle.is_right_angled():
    print("Треугольник прямоугольный")
else: print("Треугольник не прямоугольный")