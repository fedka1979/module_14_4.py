import sqlite3


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL         
        )
    ''')
    connection.commit()


def add_product(prod_id, title, description, price):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    check_product = cursor.execute("SELECT * FROM Products WHERE id=?", (prod_id,))

    if check_product.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES('{prod_id}', '{title}', '{description}', '{price}')
''')
    connection.commit()


def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    all_prod = cursor.execute("SELECT * FROM Products").fetchall()
    connection.commit()
    connection.close()
    return all_prod


initiate_db()

add_product(1, "Ламинирование", " Заметный эффект: выраженный изгиб, насыщенный цвет, густота,"
                                " длина для коротких и объем для тонких ресниц.", 1200)
add_product(2, "Классика", "Плюс классики в том, что макияж держится долго, глаза выглядят ярко,"
                           " подчеркнуто, но при этом естественно.", 1200)
add_product(3, "Наращивание уголков глаз", "Экономия времени. Процедура занимает в среднем 40"
                                           " минут, в то время как полное наращивание может занимать 1,5–2,5 часа. "
            , 1200)
add_product(4, "3D", "Экономия времени на утренний и вечерний макияж. Больше не понадобится "
                     "использовать тушь, можно отказаться даже от карандаша для подводки глаз. ", 1600)