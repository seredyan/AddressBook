import random

from model.group import Group



def test_delete_some_group(app, db, check_ui):
    if db.get_group_list() == []:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    selected_group = random.choice(old_groups)
    app.group.delete_group_by_id(selected_group.id)
    new_groups = db.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)

    old_groups.remove(selected_group)
    assert old_groups == new_groups

    if check_ui: # доп проверка корректного отображения данных в UI
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)








 




#  #  данные собираются с UI
# def test_delete_some_group_UI(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     app.group.delete_group_by_index(index)
#
#     assert len(old_groups) - 1 == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index:index+1] = []     # удаляем эелемент с индексом index+1
#     assert old_groups == new_groups


# ## пробная альтернативная идея
# def test_delete_first_group(app):
#     app.group.check()
#     #app.group.delete_first_group()