
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()  # получаем новый список групп после создания новой группы
    assert len(old_groups) - 1 == len(new_groups)



# ## пробная альтернативная идея
# def test_delete_first_group(app):
#     app.group.check()
#     #app.group.delete_first_group()