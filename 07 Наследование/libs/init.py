from random import randint, choice
from libs.functions import get_settings

from Library.classes.Book import Book
from Library.classes.Library import Library
from Library.classes.User import User
from Library.classes.Transaction import Transaction

books_data = get_settings()

# Закупаемся книгами
books = {'Fantasy': [],
         'ScienceFiction': [],
         'Romance': [],
         'Mystery': [],
         'Adventure': []}
# Fantasy
for i in range(1, randint(2, 10)):
    book = Book(choice(books_data['Fantasy']['titles']), choice(books_data['Fantasy']['authors']), randint(1800, 2023), 'Fantasy', randint(1, 4))
    books['Fantasy'].append(book)

# Science Fiction (Научная фантастика)
for i in range(1, randint(2, 10)):
    book = Book(choice(books_data['ScienceFiction']['titles']), choice(books_data['ScienceFiction']['authors']), randint(1800, 2023), 'ScienceFiction', randint(1, 4))
    books['ScienceFiction'].append(book)

# Romance (романтика)
for i in range(1, randint(2, 10)):
    book = Book(choice(books_data['Romance']['titles']), choice(books_data['Romance']['authors']), randint(1800, 2023), 'Romance', randint(1, 4))
    books['Romance'].append(book)

# Mystery (Детектив)
for i in range(1, randint(2, 10)):
    book = Book(choice(books_data['Mystery']['titles']), choice(books_data['Mystery']['authors']), randint(1800, 2023), 'Mystery', randint(1, 4))
    books['Mystery'].append(book)

# Adventure (Приключение)
for i in range(1, randint(2, 10)):
    book = Book(choice(books_data['Adventure']['titles']), choice(books_data['Adventure']['authors']), randint(1800, 2023), 'Adventure', randint(1, 4))
    books['Adventure'].append(book)

# Создаём экземпляр библиотеки
library = Library('Книжное Колесо', books)

# Создаём экземпляр пользователя
user_name = input('Введите имя пользователя: ')
user = User(user_name)

# Экземпляр транкзаций
transaction = Transaction(user)
