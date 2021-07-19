
# создаем отдельный класс для установки параметров для методов
# в данном конструкторе зададим все необходимые параметры
# дальше в качестве параметров во все основные методы будет передаваться уже лишь один объект этого класса

from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.name, self.header, self.footer)     # цель- увидеть физические имена объектов (см ролик 4_2 compare_lists)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name  # для сравнения НЕ физ адресов объектов, а ЛОГИЧЕСКОЕ сравнение
                                                                 # (см ролик 4_2 compare_lists)


    def id_or_max(self): #  вычисляет по группе ключ, используемый для сравнения
        if self.id: # если у группы есть id
            return int(self.id)   # есть вероятность что id передастся как str
        else:
            return maxsize    # константа, озн максимальное число, кот может исп в списках (очень удобно на практике
                              # использовать его как максимальное число для последующей сортировки по возрастанию или убыванию)