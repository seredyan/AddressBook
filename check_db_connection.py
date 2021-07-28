

import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

dbase = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



# # db groups connection
# try:
#     l = dbase.get_group_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass   # dbase.destroy()   # orm фвтоматически закроет соединение с БД



# # db contacts connection
# try:
#     contacts = dbase.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     pass   #dbase.destroy()



#
# # db contacts_in_group  connection
# try:
#     l = dbase.get_contacts_in_group(Group(id="1003"))
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass   # dbase.destroy()   # orm фвтоматически закроет соединение с БД


# db contacts_in_group  connection
try:
    l = dbase.get_contacts_not_in_group(Group(id="1003"))  # выдать все контакты, не входящие в эту группу
    for item in l:
        print(item)
    print(len(l))
finally:
    pass   # dbase.destroy()   # orm фвтоматически закроет соединение с БД
