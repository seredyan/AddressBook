
# создаем отдельный класс для установки параметров для методов
# в данном конструкторе зададим все необходимые параметры
# дальше в качестве параметров во все основные методы будет передаваться уже лишь один объект этого класса

class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer


class Address:

    def __init__(self, name, lastname, street, landphone, mobile, email):
        self.name = name
        self.lastname = lastname
        self.street = street
        self.landphone = landphone
        self.mobile = mobile
        self.email = email
