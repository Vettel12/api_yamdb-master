import csv
import sqlite3

# Подключиться к базе данных SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Вывести существующие таблицы
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
#print(cursor.fetchall())

# Вывести названия столбцы в таблице 'api_category'
cursor.execute("PRAGMA table_info('api_user')")
print(cursor.fetchall())

# Вывести содержимое таблицы 'api_category'
cursor.execute("SELECT * FROM api_category")
#print(cursor.fetchall())

def import_csv(csv_file_path, table_name):
    # Открыть CSV-файл для чтения
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Прочитать заголовок CSV
        header = next(reader)

        # Получить имена столбцов
        column_names = header

        # Создать SQL-запрос INSERT с динамическими столбцами
        insert_query = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(['?'] * len(column_names))})"

        # Вставить данные из CSV в таблицу
        for row in reader:
            try:
                cursor.execute(insert_query, row)
            except sqlite3.IntegrityError as e:
                print(f"Ошибка вставки: {e}")
                # Проверить, если ошибка вызвана дубликатом
                if 'UNIQUE constraint failed' in str(e):
                    print(f"Дубликатная запись: {row}")

# Пример использования - импорт двух CSV-файлов
import_csv('data/category.csv', 'api_category')
import_csv('data/comments.csv', 'api_comment')
import_csv('data/genre.csv', 'api_genre')
import_csv('data/genre_title.csv', 'api_title_genre')
import_csv('data/review.csv', 'api_review')
import_csv('data/titles.csv', 'api_title')
import_csv('data/users.csv', 'api_user')

# Сохранить изменения и закрыть соединение
conn.commit()
conn.close()