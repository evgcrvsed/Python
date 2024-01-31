class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_info(self):
        print(f'Имя: {self.name}, Номер: {self.phone}')

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return NotImplemented
        return self.name == other.name


class BusinessContact(Contact):
    def __init__(self, name, phone, company):
        super().__init__(name, phone)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f'Компания: {self.company}')


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            contact.display_info()
        print('')

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact # Выводим информацию этого контакта
        return None

    def remove_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            print(f'Контакт {contact.name} успешно удалён!\n')
            return
        print('Данного контакта нет!\n')


# Создаём телефонную книжку
phone_book = PhoneBook()

# Создаём классы контактов
contact_default_1 = Contact('Витя Широков', '+7 950 736 93 95')
contact_business_1 = BusinessContact('Иван Киселёв', '+7 904 303 89 10', 'Жировики')

# Добавляем их в нашу телефонную книжку
phone_book.add_contact(contact_default_1)
phone_book.add_contact(contact_business_1)

# Выводим все контакты
phone_book.display_contacts()

# Находим по имени контакт и удаляем его
contact_to_del = phone_book.find_contact('Витя Широков')
phone_book.remove_contact(contact_to_del)

# Выводим все контакты
phone_book.display_contacts()
