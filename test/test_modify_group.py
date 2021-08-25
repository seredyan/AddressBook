

from model.group import Group
import random
from random import randrange


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    selected_group = random.choice(old_groups)
    index = old_groups.index(selected_group)
    modified_group = Group(name="Name edited")
    modified_group.id = selected_group.id
    app.group.modify_group_by_id(selected_group.id, modified_group)  # создаем объект класса с конструктором по умолчанию

    new_groups = db.get_group_list()

    old_groups[index] = modified_group  # делаем замену групп (но id не изменится, тк мы его сохранили выше) это чтобы assert совпадал
    assert old_groups == new_groups
    # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)  # сравнение соответствия физичского НАЛИЯЧИЯ той или иной группы

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    # # итог этого теста свидетельствуют, что id у групп сохранились и несмотря на то что порядок групп при модификации
    # # поменялся, мы эти группы отсортировали и теперь у них правильное соотвтсвие по id и именам (благодаря modified_group.id = old_groups[0].id)



def test_modify_group_header(app,  db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    selected_group = random.choice(old_groups)
    modified_group = Group(header="header edited")
    modified_group.id = selected_group.id
    app.group.modify_group_by_id(selected_group.id, modified_group)

    new_groups = db.get_group_list()
    assert old_groups == new_groups

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



# def test_modify_group_name(app, db, check_ui):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = db.get_group_list()
#     index = randrange(len(old_groups))
#     modified_group = Group(name="Name edited")
#     modified_group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, modified_group) # создаем объект класса с конструктором по умолчанию
#
#     new_groups = db.get_group_list()
#     old_groups[index] = modified_group  # делаем замену групп (но id не изменится, тк мы его сохранили выше)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)  # сравнение соответствия физичского НАЛИЯЧИЯ той или иной группы
#
#     if check_ui:
#         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
#     # # итог этого теста свидетельствуют, что id у групп сохранились и несмотря на то что порядок групп при модификации
#     # # поменялся, мы эти группы отсортировали и теперь у них правильное соотвтсвие по id и именам (благодаря modified_group.id = old_groups[0].id)
