import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Проверка роли пользователя в таблице GLAVadmin
    cursor.execute("SELECT * FROM GLAVadmin WHERE login=? AND password=?", (username, password))
    glav_admin = cursor.fetchone()

    if glav_admin:
        print(f"Вы вошли как Главный Администратор с логином {username}")
        create_admin_option = input("Вы хотите создать администратора? (да/нет): ")
        if create_admin_option.lower() == 'да':
            create_admin()
        conn.close()
        return

    # Проверка роли пользователя в таблице admins
    cursor.execute("SELECT * FROM admins WHERE login=? AND password=?", (username, password))
    admin = cursor.fetchone()

    if admin:
        print(f"Вы вошли как Администратор с логином {username}")
        create_user_option = input("Вы хотите создать пользователя? (да/нет): ")
        if create_user_option.lower() == 'да':
            create_user(admin=True)
        conn.close()
        return

    # Проверка роли пользователя в таблице users
    cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        print(f"Вы вошли как Пользователь с логином {username}")
        print("Вам доступно: доступно")
        conn.close()
        return

    print("Неверный логин или пароль.")
    conn.close()

# Создание нового админа (то что спрашивали)
def create_admin():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    login = input("Введите логин нового администратора: ")
    password = input("Введите пароль нового администратора: ")
    name = input("Введите имя нового администратора: ")
    email = input("Введите email нового администратора: ")
    phone = input("Введите телефон нового администратора: ")
    organization = input("Введите организацию нового администратора: ")

    cursor.execute("INSERT INTO admins (login, password, name, email, phone, ogranize) VALUES (?, ?, ?, ?, ?, ?)",
                   (login, password, name, email, phone, organization))
    conn.commit()
    conn.close()
    print("Администратор успешно создан.")

# Слабый но пример
def create_user(admin=False):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    login = input("Введите логин нового пользователя: ")
    password = input("Введите пароль нового пользователя: ")
    name = input("Введите имя нового пользователя: ")
    email = input("Введите email нового пользователя: ")
    phone = input("Введите телефон нового пользователя: ")
    role = input("Введите роль нового пользователя: ")

    if admin:
        role = 'admin'

    cursor.execute("INSERT INTO users (login, password, name, email, phone, role) VALUES (?, ?, ?, ?, ?, ?)",
                   (login, password, name, email, phone, role))
    conn.commit()
    conn.close()
    print("Пользователь успешно создан.")

# Пример использования функции для входа пользователя
username = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")
login(username, password)

# Видите какие то недочёты или ещё что, делайте предложения
