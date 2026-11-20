import csv
import psycopg2

from config import PASSWORD

files = {
    'customers_data.csv': 'customers',
    'employees_data.csv': 'employees',
    'orders_data.csv': 'orders'
}

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=PASSWORD
)

cur = conn.cursor()

for file_name, table_name in files.items():

    with open(f'north_data/{file_name}', mode='r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            placeholders = ', '.join(['%s'] * len(row))

            query = f'INSERT INTO {table_name} VALUES ({placeholders})'

            cur.execute(query, row)

conn.commit()

cur.close()
conn.close()




