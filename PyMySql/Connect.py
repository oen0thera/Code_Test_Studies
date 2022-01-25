import pymysql
db = pymysql.connect(host='localhost',port=3306,user='oenothera',passwd='mint',charset='utf8')

cursor = db.cursor()
cursor.execute('use mysql')
cursor.execute('use ecommerce')
cursor.execute('show tables')
dt = cursor.fetchall()
