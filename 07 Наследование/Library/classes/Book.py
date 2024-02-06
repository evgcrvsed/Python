class Book:
    __slots__ = ['_name', '_author', '_year_of_publication', '_genre', '_count']

    def __init__(self, name: str = None, author: str = None, year_of_publication: int = None, genre: str = None, count: int = 0):
        self._name = name
        self._author = author
        self._year_of_publication = year_of_publication
        self._genre = genre
        self._count = count

    def add_count(self, count):
        self._count += count

    def reduce_count(self, count):
        if self._count >= count:
            self._count -= count
        else:
            raise 'столько экземпляров книги нет!'

    @property
    def get_count(self):
        return self._count

    @property
    def get_genre(self):
        return self._genre

    def __str__(self):
        return f'Экземпляр книги:\n' \
               f' Название: {self._name},\n' \
               f' Автор: {self._author},\n' \
               f' Год издания: {self._year_of_publication},\n' \
               f' Жанр: {self._genre},\n' \
               f' Имеется в наличии библиотеки: {self._count} штук.\n'