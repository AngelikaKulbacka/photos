import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-E73EMHE9;DATABASE=CMS;')

cursor = conn.cursor()
cursor.execute('select * from users')

for row in cursor.fetchall():
    print(row)