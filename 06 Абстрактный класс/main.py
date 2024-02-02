# Создайте базовый класс "Школьный предмет" с общими характеристиками (например, название, уровень сложности).
# Затем создайте подклассы для различных предметов, таких как "Математика" и "Литература",
# добавляя уникальные свойства и методы для каждого предмета.
# Реализуйте методы для вычисления средней оценки по предмету.
from abc import ABC, abstractmethod
from random import randint


class SchoolSubject(ABC):
    total_score = []

    def __init__(self, teacher_name: str = None, difficult: int = 0, score: list = None):
        self.teacher_name = teacher_name
        self.difficult = difficult
        self.score = score
        self.total_score.extend(score)

    def __str__(self):
        return f'Учитель: {self.teacher_name}, ' \
               f'Сложность: {self.difficult}/10, ' \
               f'Оценки: {", ".join(map(str, self.score))}, ' \
               f'Средний бал: {self.class_average()}.'

    def class_average(self):
        total_score = sum(self.score)
        return round(total_score / len(self.score), 1)

    @classmethod
    def total_average_score(cls):
        if not cls.total_score:
            return None

        total_score = sum(cls.total_score)
        average_score = total_score / len(cls.total_score)
        return round(average_score, 1)


class Mathematics(SchoolSubject):
    def __init__(self, teacher_name, difficult, score, tasks_solved: int = 0):
        super().__init__(teacher_name, difficult, score)
        self.tasks_solved = tasks_solved

    def __str__(self):
        return super().__str__() + f'\nРешено задач: {self.tasks_solved}'

    def calculate(self):
        self.tasks_solved += 1
        a, b = randint(0, 10) - 5, randint(0, 10) - 5
        c = a + b
        print(f'Была решена 1 задача! ({a} + {b} = {c})')


class Literature(SchoolSubject):
    def __init__(self, teacher_name, difficult, score, books_read: int = 0):
        super().__init__(teacher_name, difficult, score)
        self.books_read = books_read

    def __str__(self):
        return super().__str__() + f'\nПрочитано книг: {self.books_read}'

    def book_read(self):
        self.books_read += 1
        print(f'Была прочитана 1 книга!')


print('=' * 90)
# Создаём экземпляры классов
math = Mathematics('Ваня Киселёв', 8, [3, 4, 3, 5, 2], 7)
literature = Literature('Витя Широков', 2, [5, 4, 5, 3, 5, 2, 5], 5)

# Выводим информацию о предметах
print(f'Класс математики:\n{math}\n')
print(f'Класс литературы:\n{literature}\n')

# Вызываем метод у класса
math.calculate()
literature.book_read()

# Средняя оценка всех классов
print('')
average = SchoolSubject.total_average_score()
print(f'Средняя оценка всех предметов: {average}')
print('=' * 90)


# Разработайте систему классов для управления рестораном.
# Создайте базовый класс "Блюдо" с общими характеристиками (например, название, цена).
# Затем создайте подклассы для различных типов блюд, таких как "Завтрак" и "Ужин", добавляя специфичные свойства и методы.
# Реализуйте метод для расчета общей стоимости заказа.
class Food(ABC):
    gain = 0

    def __init__(self, name: str = None, price: float = None, calories: int = None, cooking_time: int = None):
        self.name = name
        self.price = price
        self.calories = calories
        self.cooking_time = cooking_time

    def make_order(self, wallet):
        if not wallet >= self.price:
            return False, wallet
        Food.add_gain(self.price)
        wallet -= self.price
        return True, round(wallet), f'Вы успешно заказали "{self.name}" за {self.price}$.\nЗаказ будет готов через {self.cooking_time} минут.\n'

    def __str__(self):
        return f'Блюда: {self.name}\n' \
               f'Цена: {self.price}$\n' \
               f'Калории: {self.calories}\n' \
               f'Время готовки: {self.cooking_time}м\n'

    @classmethod
    def add_gain(cls, price):
        """"Фиксируем прибыль"""
        cls.gain += price


class Breakfast(Food):
    def __init__(self, name, price, calories, cooking_time):
        super().__init__(name, price, calories, cooking_time)

    def add_apple(self):
        self.name += ', яблоко'
        self.price += 1


class Lunch(Food):
    def __init__(self, name, price, calories, cooking_time):
        super().__init__(name, price, calories, cooking_time)

    def add_cocktail(self):
        self.name += ', коктейль'
        self.price += 5


class Dinner(Food):
    def __init__(self, name, price, calories, cooking_time):
        super().__init__(name, price, calories, cooking_time)

    def add_beer(self):
        self.name += ', пиво'
        self.price += 2


# У меня 100 ДЕНЕГ
print('=' * 90)
wallet = 100
print(f'У меня {wallet}$, что бы заказать?\n')

# Создаём класс завтрака и добавляем дополнительное яблоко
print(f'Код: 1')
breakfast = Breakfast('Бекон с яйцами', 9.99, 200, 20)
breakfast.add_apple()
print(breakfast)

# Создаём класс обеда и добавляем дополнительный коктейль
print(f'Код: 2')
lunch = Lunch('Супчик и компотик', 19.99, 600, 5)
lunch.add_cocktail()
print(lunch)

# Создаём класс обеда и добавляем дополнительный коктейль
print(f'Код: 3')
dinner = Dinner('Запечённая курица', 29.99, 1000, 10)
dinner.add_beer()
print(dinner)
print('=' * 90)

# Управление
print(f'Вы не выйдете отсюда пока не потратите все деньги)')
while True:
    choice = input(f'\nУкажите код блюда: ')
    match choice:
        case '1':
            result = breakfast.make_order(wallet)
        case '2':
            result = lunch.make_order(wallet)
        case '3':
            result = dinner.make_order(wallet)
        case _:
            result = False, wallet
            print(f'Такого кода нет, вы ушли из ресторана..')
            break

    wallet = result[1]
    if result[0]:
        print(f'У вас осталось {wallet}$')
        print(result[2])
    elif result[0] == False:
        print(f'У вас недостаточно средств! {wallet}')

print(f'Ресторан заработал с вас {Food.gain}$')


# Создайте базовый класс "Сотрудник" с общими характеристиками (например, имя, зарплата).
# Затем создайте подклассы для различных типов сотрудников, таких как "Менеджер" и "Разработчик",
# добавляя уникальные свойства и методы для каждого типа.
# Реализуйте методы для подсчета общей зарплаты и вычисления премии.
class Employee(ABC):
    def __init__(self, name: str = None, salary: int = None):
        self.name = name
        self.salary = salary

    def calculating_salaries(self):
        return f'Зарабатывая {self.salary} в час за 7 дней вы получите {self.salary}$ * 7 * 12 = {self.salary * 7 * 12}$.'

    @abstractmethod # Надо переопределить в экземпляре класса
    def work(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary, sales):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        self.sales = sales

    def work(self):
        self.sales += 1
        return f'Менеджер сделал 1 продажу!'


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.name = name
        self.salary = salary
        self.fixed_bugs = 0

    def work(self):
        self.fixed_bugs += 1
        return f'Разработчик {self.name} пофиксил 1 баг!'


manager = Manager('Ваня', 10, 3)
dev = Developer('Женёк', 60)
print('=' * 90)
print(manager.work())
print(dev.work())
print('=' * 90)
print(manager.calculating_salaries())
print(dev.calculating_salaries())
print('=' * 90)
