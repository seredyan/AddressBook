

from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="Name edited")) # создаем объект класса с конструктором по умолчанию



def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="header edited"))
