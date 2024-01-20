import time


class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = self.validate_age(age)
        self.email = email
        print(f'Person created.\n Name: {self.name},\n Age: {self.age},\n Email: {self.email}\n')

    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = self.validate_age(age)
    def set_email(self, email):
        self.email = email

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_email(self):
        return self.email

    @staticmethod
    def validate_age(age: int) -> int:
        """Validate and return the age if valid."""
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')
        if age <= 0:
            raise ValueError('Age must be greater than 0')
        return age


person = Person('Bebra', 12, 'bebra@gmail.com')


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = self.validate_price(price)
        self.quantity = quantity
        print(f'Product created.\n Name: {self.name},\n Price: {self.price},\n Quantity: {self.quantity}\n')

    def set_name(self, name):
        self.name = name
    def set_price(self, price):
        self.price = self.validate_price(price)
    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_quantity(self):
        return self.quantity

    @staticmethod
    def validate_price(price):
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be number')
        if price <= 0:
            raise ValueError('Price must be greater than 0')
        return price

product = Product('Apple', 99.99, 30)


# Создать класс "Book" с атрибутами "title", "author", "genre" и
# методами для чтения и записи данных всех трех атрибутов, а также реализовать валидацию для атрибута "genre":
# должно быть строкой
# не должно быть пустой строкой и должно содержать наименование только из указанного списка [“фантастика”, “драма”,  “проза”]
class Book:
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = self.validate_genre(genre)
        print(f'Book created.\n Title: {self.title},\n Author: {self.author},\n Genre: {self.genre}\n')

    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def set_genre(self, genre):
        self.genre = self.validate_genre(genre)

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_genre(self):
        return self.genre

    @staticmethod
    def validate_genre(genre):
        if not genre in ['Фантастика', 'Драма', 'Проза']:
            raise ValueError('Invalid genre')
        return genre

book = Book('Bebra', 'Albert Bebroвич', 'Драма')
