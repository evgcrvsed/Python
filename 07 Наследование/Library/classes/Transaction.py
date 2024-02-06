import time


class Transaction:
    def __init__(self, user):
        self._user = user
        self._transactions = []

    def add_transaction(self, do):
        self._transactions.append(f'User {self._user.get_name} {do}! Время: {round(time.time())}')

    def show_history(self):
        for item in self._transactions:
            print(item)
