# -*- coding: utf-8 -*-

from model.group import Group


 


def test_add_group(app, db, json_groups, check_ui):  # осущ связь тестовых ф-й с данными, хранящимися в файлах в формате json
    added_group = json_groups
    old_groups = db.get_group_list()
    app.group.create(added_group)

    # assert len(old_groups) + 1 == app.group.count() # исп метод group.count вместо создания нового списка (для ускорения) и проверки условий для след assert
    # этот assert уже не нужен, тк берем данные уже с БД


    new_groups = db.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравнение соответствия физичского НАЛИЯЧИЯ той или иной группы

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



    # assert old_groups == new_groups  # сравнения соответствия НАЛИЯЧИЯ той или иной группы
                                     # однако нельзя сравнивать просто как здесь, тк порядок в списке нарушится
                                     # и assert не сработает (см ролик 4_3 sorting_lists)





# # сбор данных из UI
# def test_add_group(app, json_groups):  # осущ связь тестовых ф-й с данными, хранящимися в файлах в формате json
#     added_group = json_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(added_group)
#
#     assert len(old_groups) + 1 == app.group.count() # исп метод group.count вместо создания нового списка (для ускорения) и проверки условий для след assert
#
#     new_groups = app.group.get_group_list()
#     old_groups.append(added_group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)










# def test_add_group_constant_data(app, data_groups):  # тест создания группы с фиксированными данными (для отладки)
#     added_group = data_groups
#     old_groups = app.group.get_group_list()
#     app.group.create(added_group)
#
#     assert len(old_groups) + 1 == app.group.count()
#
#     new_groups = app.group.get_group_list()
#     old_groups.append(added_group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
