class Book:
    def __init__(self, name, author, style):
        self.name = name
        self.author = author
        self.style = style


book = Book('Чипи чипи', 'Артур Пирожков', 'Романтика')
# print(f'название - {book.name},\nавтор - {book.author},\nжанр - {book.style}\n')


class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


bank_user = Bank('Надежда Ивановна', 1000)
# print(f'владелец карты - {bank_user.owner},\nбаланс - {bank_user.balance}\n')


# Реализуйте класс для управления системой бронирования отелей. Класс Бронь должен содержать информацию о госте,
# дате заезда и выезда, типе номера.
# Методы должны позволять бронировать, отменять бронь и проверять доступность номеров на определенные даты.
class Hotel:
    def __init__(self):
        self.busyDates = [4]
        self.users = {}

    def isBusy(self, date_start: int, date_end: int):
        busy_dates = []
        for i in range(date_start, date_end + 1):
            if i in self.busyDates:
                busy_dates.append(i)

        if len(busy_dates) == 0:
            print(f'Ваши даты свободны!')
            return False
        else:
            print(f'Числа {busy_dates} заняты! Выберите другое!')
            return True
        pass

    def toFreeByName(self, name: str):
        print(f'Имя {name} записано на даты: {", ".join(map(str, self.users[name]["dates"]))}.')
        for el in self.users[name]['dates']:
            self.busyDates.remove(el)
        del self.users[name]
        print(f'Имя {name} больше никуда не записано.\n')
        pass

    def tryToReserve(self, user: object, date_start=-1, date_end=31):
        if not 1 <= date_start <= 30 and 1 <= date_end <= 30:
            print('Неверная дата! Введите день приезда и день выезда!')
            return
        elif date_start > date_end:
            print('Дата въезда больше, чем дата выезда...')
            return

        if date_end - date_start > 7:
            print('Въезжать более чем на 7 дней нельзя!')
            return

        if self.isBusy(date_start, date_end):
            print(f'Введите новые даты')
            return

        self.users[user['name']] = {
            'dates': [],
            'old': user['old'],
        }

        added_dates = []
        for i in range(date_start, date_end + 1):
            added_dates.append(i)
            self.busyDates.append(i)
            self.users[user['name']]['dates'].append(i)
        print(f'Дни под номером {", ".join(map(str, added_dates))} записаны на имя {user["name"]}!\n')
        pass


hotel = Hotel()
user = {
    'name': 'Bebra',
    'old': '20'
}
hotel.tryToReserve(user, 5, 10)
hotel.tryToReserve(user, 5, 10)
hotel.toFreeByName('Bebra')
user = {
    'name': 'Bebra',
    'old': '20'
}
hotel.tryToReserve(user, 5, 10)
print(hotel.busyDates)
