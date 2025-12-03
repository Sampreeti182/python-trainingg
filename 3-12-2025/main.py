import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Chillichicken@1802',
    database='company_db'
)
cursor=connection.cursor()
cursor.execute('SELECT * FROM employees')
rows=cursor.fetchall()
for row in rows:
    print(row)