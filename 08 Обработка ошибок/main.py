# Реализуйте класс Rectangle, представляющий прямоугольник.
# В классе должны быть атрибуты width и height,
# а также методы calculate_area (вычисление площади) и calculate_perimeter (вычисление периметра).
# Создайте собственный класс исключения InvalidDimensionsError,
# который будет возбуждаться при создании прямоугольника с неположительной шириной или высотой.
class InvalidDimensionsError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise InvalidDimensionsError("Ширина и высота прямоугольника должны быть положительными числами.")
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return (self._width + self._height) * 2


try:
    rectangle = Rectangle(1, 10)
    print("Площадь прямоугольника:", rectangle.calculate_area())
    print("Периметр прямоугольника:", rectangle.calculate_perimeter())
except InvalidDimensionsError as e:
    print("Ошибка:", e)
