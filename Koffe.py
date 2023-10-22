# Приложение книжный магазин:
# Программа должна:

# хранить данные в бд +
# поиск книг по названию +
# поиск книг по авторам +
# сортировка книг по ценам +
# добавлять, удалять, редактировать данные в бд +

# Для пользователя: +
# список желаемого +
# корзина товара +
# учет продаж +
# учет сотрудников и их продаж +





import sqlite3

# Подключение к базе данных
def connect_db():
    conn = sqlite3.connect('bookstore.db')
    cursor = conn.cursor()
    return conn, cursor

# Создание таблиц
def create_tables():
    conn, cursor = connect_db()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            BookID INTEGER PRIMARY KEY,
            Title TEXT,
            Author TEXT,
            Price float CHECK (LENGTH(SUBSTR(Price, INSTR(Price, '.') + 1)) <= 2)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Sales (
            SaleID INTEGER PRIMARY KEY,
            BookID INTEGER,
            SaleDate DATE,
            Quantity INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            EmployeeID INTEGER PRIMARY KEY,
            FirstName TEXT,
            LastName TEXT,
            Salary float CHECK (LENGTH(SUBSTR(Price, INSTR(Price, '.') + 1)) <= 2)
        )
    ''')

    conn.commit()
    conn.close()
    
    
    
    
    

# Добавление книги
def add_book(title, author, price):
    conn, cursor = connect_db()
    
    cursor.execute('INSERT INTO Books (Title, Author, Price) VALUES (?, ?, ?)', (title, author, price))
    
    conn.commit()
    conn.close()

# Удаление книги по ID
def delete_book(book_id):
    conn, cursor = connect_db()
    
    cursor.execute('DELETE FROM Books WHERE BookID = ?', (book_id,))
    
    conn.commit()
    conn.close()

# Редактирование книги
def edit_book(book_id, title, author, price):
    conn, cursor = connect_db()
    
    cursor.execute('''
        UPDATE Books
        SET Title = ?,
            Author 
            Price = ?= ?,
        WHERE BookID = ?
    ''', (title, author, price, book_id))
    
    conn.commit()
    conn.close()

# Поиск книги по названию
def search_books_by_title(title):
    conn, cursor = connect_db()
    
    cursor.execute('SELECT * FROM Books WHERE Title LIKE ?', ('%' + title + '%',))
    
    books = cursor.fetchall()
    
    conn.close()
    
    return books

# Поиск книги по автору
def search_books_by_author(author):
    conn, cursor = connect_db()
    
    cursor.execute('SELECT * FROM Books WHERE Author LIKE ?', ('%' + author + '%',))
    
    books = cursor.fetchall()
    
    conn.close()
    
    return books

# Сортировка книг по ценам
def sort_books_by_price():
    conn, cursor = connect_db()
    
    cursor.execute('SELECT * FROM Books ORDER BY Price')
    
    books = cursor.fetchall()
    
    conn.close()
    
    return books

# Добавление продажи
def add_sale(book_id, sale_date, quantity):
    conn, cursor = connect_db()
    
    cursor.execute('INSERT INTO Sales (BookID, SaleDate, Quantity) VALUES (?, ?, ?)', (book_id, sale_date, quantity))
    
    conn.commit()
    conn.close()

# Добавление сотрудника
def add_employee(first_name, last_name, salary):
    conn, cursor = connect_db()
    
    cursor.execute('INSERT INTO Employees (FirstName, LastName, Salary) VALUES (?, ?, ?)', (first_name, last_name, salary))
    
    conn.commit()
    conn.close()
    
def fire_employee(first_name, last_name):
    conn, cursor = connect_db()
    
    cursor.execute('DELETE FROM Employees WHERE FirstName = ? AND LastName = ?', (first_name, last_name,))
    
    conn.commit()
    conn.close()
    
    



# Главное меню
def main_menu():
    while True:
        print(f"Книжный магазин\n"
                f"1. Добавить книгу\n"
                f"2. Удалить книгу\n"
                f"3. Редактировать книгу\n"
                f"4. Поиск книги по названию\n"
                f"5. Поиск книги по автору\n"
                f"6. Сортировка книг по ценам\n"
                f"7. Добавить продажу\n"
                f"8. Добавить сотрудника\n"
                f"9. Уволить сотрудников\n"
                f"10. Выход")
#Функцию показа не стал добавлять, тк все есть в бд
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            price = float(input("Введите цену: "))
            add_book(title, author, price)
            
        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            delete_book(book_id)
            
        elif choice == '3':
            book_id = int(input("Введите ID книги для редактирования: "))
            title = input("Введите новое название книги: ")
            author = input("Введите нового автора: ")
            price = float(input("Введите новую цену: "))
            edit_book(book_id, title, author, price)
            
        elif choice == '4':
            title = input("Введите часть названия для поиска: ")
            books = search_books_by_title(title)
            for book in books:
                print(book)
                
        elif choice == '5':
            author = input("Введите часть автора для поиска: ")
            books = search_books_by_author(author)
            for book in books:
                print(book)
                
        elif choice == '6':
            books = sort_books_by_price()
            for book in books:
                print(book)
                
        elif choice == '7':
            book_id = int(input("Введите ID книги для продажи: "))
            sale_date = input("Введите дату продажи (гггг-мм-дд): ")
            quantity = int(input("Введите количество проданных экземпляров: "))
            add_sale(book_id, sale_date, quantity)
            
        elif choice == '8':
            first_name = input("Введите имя сотрудника: ")
            last_name = input("Введите фамилию сотрудника: ")
            salary = float(input("Введите зарплату сотрудника: "))
            add_employee(first_name, last_name, salary)
            
        elif choice == '9':
            first_name = input("Введите имя сотрудника: ")
            last_name = input("Введите фамилию сотрудника: ")
            fire_employee(first_name, last_name)
            
        elif choice == '10':
            break
        else:
            print("Неправильный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    create_tables()
    main_menu()
    
    


#Друг скинул вариант через лямбду, но он оказался не рабочим, мне его в падлу фиксить -_-. Но пусть висит тут)

#         options = {
#     '1': ('Добавить книгу', lambda: add_book(input("Введите название книги: ")), input("Введите автора: "), float(input("Введите цену: "))),
#     '2': ('Удалить книгу', lambda: delete_book(int(input("Введите ID книги для удаления: "))),
#     '3': ('Редактировать книгу', lambda: edit_book(int(input("Введите ID книги для редактирования: ")), input("Введите новое название книги: "), input("Введите нового автора: "), float(input("Введите новую цену: "))),
#     '4': ('Поиск книги по названию', lambda: print_books(search_books('Title', input("Введите часть названия для поиска: "))),
#     '5': ('Поиск книги по автору', lambda: print_books(search_books('Author', input("Введите часть автора для поиска: "))),
#     '6': ('Сортировка книг по ценам', lambda: print_books(sort_books_by_price())),
#     '7': ('Добавить продажу', lambda: add_sale(int(input("Введите ID книги для продажи: ")), input("Введите дату продажи (гггг-мм-дд): "), int(input("Введите количество проданных экземпляров: "))),
#     '8': ('Добавить сотрудника', lambda: add_employee(input("Введите имя сотрудника: ")), input("Введите фамилию сотрудника: "), float(input("Введите зарплату сотрудника: "))),
#     '9': ('Выход', lambda: exit())
#     }
    
#     while True:
#         print("Книжный магазин")
#         for key, value in options.items():
#             print(f"{key}. {value[0]}")
#         choice = input("Выберите действие: ")
        
#         if choice in options:
#             options[choice][1]()
#         else:
#             print("Неправильный ввод. Пожалуйста, выберите действие из списка.")

# def print_books(books):
#     for book in books:
#         print(book)

 