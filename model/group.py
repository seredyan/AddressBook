
# создаем отдельный класс для установки параметров для методов
# в данном конструкторе зададим все необходимые параметры
# дальше в качестве параметров во все основные методы будет передаваться уже лишь один объект этого класса

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id


    def __repr__(self):
        return "Group(" + str(self.name) + ", " + str(self.id) + ")"  # для дебагинга выводим результаты в консоль для наблюдения


