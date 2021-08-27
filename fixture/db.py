
import pymysql.cursors
from model.group import Group
from model.contact import Contact



class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
                                                        # autocommit озн что кэш после кажд запроса сбрасывается (роли 7_4)


    def get_group_list(self): #  загруж из БД инфу о группах
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row   #  присвоится значения сразу в 4 переменные, каждой из них присвотся соотв эл-т кортежа
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list




    def get_contact_list(self):  # загруж из БД инфу о контактах
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row  # присвоится значения сразу в 4 переменные, каждой из них присвотся соотв эл-т кортежа
                list.append(Contact(id=str(id), name=firstname, lastname=lastname, address=address, landline=home, mobile=mobile, workphone=work, email=email, email2=email2, email3=email3, second_landline=phone2))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()
