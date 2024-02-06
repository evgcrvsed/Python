from libs.init import library, user, transaction # Создаём библиотеку
print(library)
print(user)


while True:
    print('=' * 80)
    print('1 - Показать книги')
    print('2 - Взять книгу по genre и id')
    print('3 - Посмотреть взятые книги пользователя')
    print('4 - Вернуть книгу')
    print('5 - Посмотреть историю пользователя')
    choice = input('Введите тип операции: ')
    print('')

    match choice:
        case '1':
            library.show_books()
            transaction.add_transaction('посмотрел книги')
        case '2':
            inpt_1 = input(f'Введите жанр: ')
            library.show_books_by_genre(inpt_1)
            transaction.add_transaction(f'посмотрел книги жанра {inpt_1}')
            inpt_2 = input(f'Введите id, чтобы взять книгу: ')
            transaction.add_transaction(f'взял книгу жанра {inpt_1}')
            library.remove_book(user, inpt_1, int(inpt_2))
        case '3':
            transaction.add_transaction(f'посмотрел книги которые взял')
            user.show_taken_books()
        case '4':
            transaction.add_transaction(f'вернул взятую книгу')
            user.show_taken_books()
            book = user.return_book()
            library.add_book(book)
        case '5':
            transaction.add_transaction(f'посмотрел историю')
            transaction.show_history()
        case '6':
            pass
        case _:
            print(f'Программа завершена!')
            break


