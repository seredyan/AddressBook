

from sys import maxsize

class Contact:

    def __init__(self, name=None, lastname=None, address=None, landline=None, mobile=None, email=None, id=None):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.name)     # цель- увидеть физические имена объектов (см ролик 4_2 compare_lists)
                                                                 # поменял порядок  name и lastname - как на веб приложении

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.name == other.name   # для сравнения не физ адресов объектов, а логич сравнение
                                                                 # (см ролик 4_2 compare_lists)



    def id_or_max(self):  # вычисляет по контакту ключ, используемый для сравнения
        if self.id:
            return int(self.id)
        else:
            return maxsize