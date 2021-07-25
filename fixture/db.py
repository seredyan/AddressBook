
import pymysql.cursors
from model.group import Group



class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
                                                        # autocommit озн что кэш после кажд запроса сбрасывается (роли 7_4)


    def get_group_list(self): #  загруж из БД инфу о группах и контактах
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



    def destroy(self):
        self.connection.close()
