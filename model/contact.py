

from sys import maxsize

class Contact:

    def __init__(self, name=None, lastname=None, address=None, landline=None, mobile=None, workphone=None, second_landline=None,
                 all_phones_from_home_page=None, all_phones_from_view_page=None, email=None,  email2=None,  email3=None, id=None, all_emails_from_home_page=None,
                 all_emails_from_view_page=None):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.workphone = workphone
        self.second_landline = second_landline
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_phones_from_view_page = all_phones_from_view_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_emails_from_view_page = all_emails_from_view_page


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.name, self.address, self.email, self.email2, self.email3, self.landline, self.mobile, self.workphone, self.second_landline, self.all_phones_from_home_page,  self.all_emails_from_home_page) # цель- увидеть физические имена объектов (см ролик 4_2 compare_lists)
                                                                 # поменял порядок  name и lastname - как на веб приложении

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.name == other.name and self.address == other.address and self.all_phones_from_home_page == other.all_phones_from_home_page and self.all_emails_from_home_page == other.all_emails_from_home_page

        # для сравнения НЕ ФИЗ адресов объектов, а ЛОГИЧ сравнение
                                                                 # (см ролик 4_2 compare_lists)



    def id_or_max(self):  # вычисляет по контакту ключ, используемый для сравнения
        if self.id:
            return int(self.id)
        else:
            return maxsize