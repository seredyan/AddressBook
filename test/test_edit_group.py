

from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Second", header="edited", footer="finished")) # создаем объект класса с конструктором по умолчанию
    app.session.logout()
