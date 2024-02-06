class Library:
    __slots__ = ['_books', '_users', '_name', '_books_count']

    def __init__(self, name: str = None, books: dict = None):
        self._name = name
        self._books = books
        self._users = []
        self._books_count = self.count_books_all()

    def add_user(self, user):
        self._users.append(user)

    def add_book(self, book):
        self._books[book.get_genre].append(book)
        print('Книга возвращена!')
        pass

    def remove_book(self, user, genre, id):
        for index, book in enumerate(self._books[genre]):
            if index + 1 == id:
                print(index + 1)
                print(f'Наличие: {book.get_count}')
                if book.get_count > 0:
                    book.reduce_count(1)
                    user.add_book(book)
                    print('Вы взяли книгу!')
                    print(book)
                    break
                else:
                    print(f'Данной книги нет в наличии!')

    def show_books(self):
        text = 'Какой жанр книг вас интересует?'
        for index, genre in enumerate(self._books):
            text += f'\n {index + 1} {genre}'

        inpt = input(f'{text}\nВведите номер: ')
        print()
        match inpt:
            case '1':
                genre = 'Fantasy'
            case '2':
                genre = 'ScienceFiction'
            case '3':
                genre = 'Romance'
            case '4':
                genre = 'Mystery'
            case '5':
                genre = 'Adventure'
        print(f'У нас есть {self.count_books_by_genre(genre)} книг этого жанра!')
        self.show_books_by_genre(genre)
        return ''

    def show_books_by_genre(self, genre):
        for genr in self._books:
            if genr != genre:
                continue
            for index, book in enumerate(self._books[genre]):
                print(f'Индекс книги: {index + 1}')
                print(book)

    def count_books_all(self):
        books_count = 0
        for genre in self._books:
            books_count += len(self._books[genre])
        self._books_count = books_count
        return self._books_count

    def count_books_by_genre(self, genre):
        for genr in self._books:
            if genr == genre:
                return len(self._books[genr])
        return None
        pass

    def __str__(self):
        return f"Библиотека: '{self._name}', У нас {self._books_count} разных книг!"