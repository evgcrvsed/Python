import sqlite3 as sq


class DataBase:
    def __init__(self, patch: str):
        self._patch = patch

    def create_table(self):
        self.get_cursor.execute("""CREATE TABLE IF NOT EXISTS Data (
                                           user_telegram_id INT NOT NULL,
                                              
                                           user_redirected BOOL DEFAULT False
                                           )""")
        return

    def set_is_user_redirected_true(self, user_telegram_id: int):
        self.get_cursor.execute('UPDATE Data SET user_redirected = ? WHERE user_telegram_id = ?;',(True, user_telegram_id)).connection.commit()

    def is_user_redirected(self, user_telegram_id: str) -> bool:
        result = self.get_cursor.execute("SELECT user_redirected FROM Data WHERE user_telegram_id = ?",
                                         (user_telegram_id,), ).fetchone()
        if result[0] == 0:
            return False
        else:
            return True

    def add_user(self, user_telegram_id: str):
        user_data = self.get_cursor.execute("SELECT * FROM Data WHERE user_telegram_id = ?", (user_telegram_id,),).fetchone()
        if user_data is None:
            # Создаём нового юзера если его нет в бд
            self.get_cursor.execute('INSERT INTO Data (user_telegram_id) VALUES (?);', (user_telegram_id,)).connection.commit()

            print(f'Бота запустил новый пользователь {user_telegram_id}')
            return True

    @property
    def get_cursor(self):
        with sq.connect(self._patch) as con:
            return con.cursor()
