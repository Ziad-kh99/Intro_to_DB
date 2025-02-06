import mysql.connector


try:
    db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'P@$$w0rd',
            database = 'alx_book_store'
    )
except Exception as e:
    print('Can not connect to MySQL Server')
    print(f'Error: {e}')
    exit()

cursor = db.cursor()

sql = '''
CREATE DATABASE IF NOT EXISTS alx_book_store;
'''

try:
    cursor.execute(sql)
except:
    print('Something went wrong')
else:
    print('Database \'alx_book_store\' created successfully')

cursor.close()
db.close()

