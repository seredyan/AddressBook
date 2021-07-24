

import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()        #  создаем указатель на данные в БД
    cursor.execute("select * from group_list")      # запрос на языке SQL
    for row in cursor.fetchall():         # извлекаем всю инфу с помощью метода fetchall()
        print(row)
finally:
    connection.close()
