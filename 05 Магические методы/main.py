# Создайте класс Book, представляющий книгу.
# Реализуйте магические методы сравнения (==, !=, <, >, <=, >=) на основе сравнения года издания книги.
# Книги сравниваются по году издания.

class Book:
    def __init__(self, year):
        self.year = year

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year == other.year

    def __ne__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year < other.year

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year <= other.year

    def __gt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year > other.year

    def __ge__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.year >= other.year

    def __str__(self):
        return str(self.year) # Что будет возвращаться при написании класса


book1 = Book(2000)
book2 = Book(2003)

print(f'Равны ли классы: {book1 == book2} ({book1} == {book2})')
print(f'Не равны ли классы: {book1 != book2} ({book1} != {book2})')
print(f'Меньше ли у первого класса: {book1 < book2} ({book1} < {book2})')
print(f'Больше ли у первого класса: {book1 > book2} ({book1} > {book2})')
print(f'Меньше или равно у первого класса: {book1 <= book2} ({book1} <= {book2})')
print(f'Больше или равно у первого класса: {book1 >= book2} ({book1} >= {book2})')
