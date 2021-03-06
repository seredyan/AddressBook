
from pony.orm import *
from _datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders

class ORMFixture:  # Ролик 7_7

    db = Database() # объект, на основании которого строится привязка (в виде наборов классов)

    class ORMGroup(db.Entity): # привязываем этот класс к БД ч/з db.Entity, т.е этот класс опис разл объекты, кот будут сохр в эту БД
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True) # ролик 7_8
                                        # table="address_in_groups" т.е ук связь контактов и групп



    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True) # ролик 7_8



    # выше -структура таблиц
    # ниже - привязка к БД

    def __init__(self, host, name, user, password):  #(ролик 7_7)
        self.db.bind('mysql', host=host, database=name, user=user, password=password)#, conv=decoders)  # это несмотря на то, что установлен pymysql
        self.db.generate_mapping()   # начинается сопоставление св-в описанных выше классов с таблицами и полями этих таблиц
        sql_debug(True)  # выводит реальный запрос на языке SQL который генерирует Pony ORM



## ниже - ф-ии, кот получают СПИСКИ объектов

    def convert_groups_to_model(self, groups):  # ролик 7_7   будет в виде списка, пригодного для дальнейшей работы
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))



    def convert_contacts_to_model(self, contacts):  # ролик 7_7   будет в виде списка, пригодного для дальнейшей работы
        def convert(contact):
            return Contact(id=str(contact.id), name=contact.name, lastname=contact.lastname)

        return list(map(convert, contacts))




    @db_session   # для групп  ролик 7_7
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))


    @db_session  # для контактов   ролик 7_7
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):  # зд group - объект модельного типа  # ролик 7_8
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]   #  извлекаем группу с заданным id
        return self.convert_contacts_to_model(orm_group.contacts)  # преобразуем объекты типа orm_group.contacts в модельный объекты


    @db_session
    def get_contacts_not_in_group(self, group):  # зд group - объект модельного типа   # ролик 7_8
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
        # выбираем все контакты, у которых список групп не содержит заданную группу (если контакт связан с группой, то он в эту выборку не попадет)



















