
import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re



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
                list.append(Contact(id=str(id), name=firstname, lastname=lastname, address=address, all_phones_from_home_page=merge_phones_like_on_home_page(home, mobile, work, phone2), all_emails_from_home_page=merge_emails_like_on_home_page(email, email2, email3)))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()



def merge_phones_like_on_home_page(phone1, phone2, phone3, phone4):
    merge_phones = " ".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [phone1, phone2, phone3, phone4]))))
    return merge_phones.split()


def merge_emails_like_on_home_page(email1, email2, email3):
    merge_emails = " ".join(filter(lambda x: x != "", map(lambda x: clear_emails(x), filter(lambda x: x is not None, [email1, email2, email3]))))
    return merge_emails.split()


def clear(s):
    return re.sub("[() -]", "", s)

def clear_emails(s):
    return re.sub("[ ]", "", s)


