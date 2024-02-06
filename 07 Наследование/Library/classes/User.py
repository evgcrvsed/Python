from random import randint


class User:
    def __init__(self, name: str):
        self._name = name
        self._id = randint(900000, 999999)
        self._books_taken = []

    def add_book(self, book: object):
        self._books_taken.append(book)

    def return_book(self):
        inpt = int(input(f'Какой индекс книги хотите вернуть: ')) - 1
        book = self._books_taken[int(inpt)]
        self._books_taken.pop(int(inpt))
        return book

    def show_taken_books(self):
        for i, book in enumerate(self._books_taken):
            print(f'Индекс книги: {i + 1}')
            print(book)

    @property
    def get_name(self):
        return self._name

    def __str__(self):
        return f'{self._name}, id={self._id}'
