class Snowflake:
    def __init__(self, size: int, shape: str):
        self.__size = size
        self.__shape = shape

    def change_size(self, new_size: int):
        self.__size = new_size

    def change_shape(self, new_shape: str):
        self.__shape = new_shape


class SantaClaus:
    def __init__(self, name: str, old: int, gifts_count: int):
        self.__name = name
        self.__old = old
        self.__gifts_count = gifts_count

    def give_gifts(self, value):
        if self.__gifts_count < value:
            print(f'У Санты всего {self.__gifts_count} подарков, он не может отправить {value} штук!\n'
                  f'Не хватает {abs(self.__gifts_count - value)} штук!')
            return
        self.__gifts_count -= value
        print(f'Санта отправил {value} подарков!\nОсталось: {self.__gifts_count} штук.')

    def update_age(self, new_age):
        if new_age < 30:
            print('Санта никак не может быть моложе 30 лет.')
            return
        self.__old = new_age
        print(f'Возраст Санты: {self.__old}')


class ChristmasTree:
    def __init__(self, height, decorations_count):
        self.__height = height
        self.__decorations_count = decorations_count

    def decorate_tree(self, new_decorations):
        self.__decorations_count += new_decorations
        print(f'Дерево украшено на {new_decorations} больше.\nВсего {self.__decorations_count} игрушек.\n')

    def grow_tree(self, new_height):
        self.__height += abs(new_height)
        print(f'Дерево выросло на {abs(new_height)} см.\nВысота: {self.__height} см.\n')
