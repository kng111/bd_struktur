import sqlite3

def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Создание таблицы главных администраторов
    cursor.execute('''CREATE TABLE IF NOT EXISTS GLAVadmin (
                    id INTEGER PRIMARY KEY,
                    login TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    ogranize TEXT NOT NULL
                    )''')

    # Создание таблицы администраторов
    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                    id INTEGER PRIMARY KEY,
                    login TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    ogranize TEXT NOT NULL
                    )''')

    # Создание таблицы пользователей
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    login TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    role TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()

def create_glav_admin(login, password, name, email, phone, ogranize):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO GLAVadmin (login, password, name, email, phone, ogranize) VALUES (?, ?, ?, ?, ?, ?)", 
                       (login, password, name, email, phone, ogranize))
        conn.commit()
        print("Главный администратор успешно создан.")
    except sqlite3.IntegrityError:
        print("Ошибка: Главный администратор с таким логином уже существует.")

    conn.close()

def create_admin(login, password, name, email, phone, ogranize):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO admins (login, password, name, email, phone, ogranize) VALUES (?, ?, ?, ?, ?, ?)", 
                       (login, password, name, email, phone, ogranize))
        conn.commit()
        print("Администратор успешно создан.")
    except sqlite3.IntegrityError:
        print("Ошибка: Администратор с таким логином уже существует.")

    conn.close()

def create_user(login, password, name, email, phone, role='no'):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (login, password, name, email, phone, role) VALUES (?, ?, ?, ?, ?, ?)", 
                       (login, password, name, email, phone, role))
        conn.commit()
        print("Пользователь успешно создан.")
    except sqlite3.IntegrityError:
        print("Ошибка: Пользователь с таким логином уже существует.")

    conn.close()

# Создание структуры базы данных
create_database()

# Пример использования функций для создания главного администратора, администратора и пользователей
create_glav_admin('glav_admin', 'password123', 'Главный Администратор', 'admin@example.com', '123456789', 'организация')
create_admin('admin1', 'password123', 'Администратор 1', 'admin1@example.com', '987654321', 'организация')
create_user('user1', 'password123', 'Пользователь 1', 'user1@example.com', '555555555', 'logist')
