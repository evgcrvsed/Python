import json


def get_settings():
    """Возвращаем все данные из файла"""
    with open('Library/books.json', 'r', encoding='utf=8') as file:
        data = json.load(file)
        return data
