import sqlite3

'''
with sqlite3.connect('urok_11_27.db') as connection:  # это конструкция итератора, которая следит за закрытеем БД (стандартная конструкция)
    cursor = connection.cursor()  # Подключение к БД и создание объекта курсор для работы с SQL запросами
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
    # Запрос на создание (если такой нет) БД с внешним ключом, именем, и возрастом  
'''

class Database:  # создание класса для общения и изменения БД

    def __init__(self, db):  # основная конструкция в неё передаётся название файла БД
        self.connection = sqlite3.connect(db)  # подключение к БД
        self.cursor = self.connection.cursor()  # создание объекта общения

    def create_table(self):  # метод класса создающий БД
        with self.connection:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

    def add_user(self, name, age):  # метод добавляющий данные пользователя в БД
        with self.connection:
            self.cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
            # вопросами обозначаются места подстановки данных из кортежа
            # если кортеж с одним данным нужно поставить запятую, чтоб кортеж существовал: (Ivan, )

    def get_users_list(self):  # метод выводящий список пользователей
        with self.connection:
            return self.cursor.execute('SELECT * FROM users').fetchall()  # метод позваляющий собрать данные в список кортежей


    def get_user(self, user_id):  # медод получения данных пользователя по ID
        with self.connection:
            return self.cursor.execute('SELECT name, age FROM users WHERE id = ?', (user_id, )).fetchone()  # метод дающий кортеж с данными

    def update_user_age(self, user_id, age):  # медод изменения данных пользователя по ID в столбце age
        with self.connection:
            self.cursor.execute('UPDATE users SET age = ? WHERE id = ?', (age, user_id))

    def del_user(self, user_id):  # медод избавления от пользователя  по ID
        with self.connection:
            self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id, ))

    def del_all_users(self):  # медод избавления от пользователелей
        with self.connection:
            self.cursor.execute('DELETE FROM users')


if __name__ == '__main__':
    db = Database('urok_11_27.db')
    db.create_table()
    db.add_user('DIMA', 21)
    db.add_user('Ivan', 15)
    print(db.get_users_list())
    print(db.get_user(2))
    db.update_user_age(1, 1999)
    #db.del_user(2)
    print(db.get_users_list())
    #db.del_all_users()
    print(db.get_users_list())