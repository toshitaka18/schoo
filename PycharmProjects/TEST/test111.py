import mysql.connector as mydb
conn = mydb.connect(
    host='localhost',
    port='3306',
    user='root',
    password='freshers@2020',
    database='freshers_schema'
)

print(conn.is_connected()) #DBに接続されていればTRUE

cur = conn.cursor()
sql = "SELECT * from items"
cur.execute(sql)

for row in cur:
    print(row)