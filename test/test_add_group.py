# -*- coding: utf-8 -*-

from model.group import Group


from data.groups import constant   # если хотим создать ФИКСИРОВАННЫЕ данные для ОТЛАДКИ тестов
# import pytest

 


def test_add_group(app, json_groups):  # осущ связь тестовых ф-й с данными, хранящимися в файлах в формате json
    added_group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(added_group)

    assert len(old_groups) + 1 == app.group.count() # исп метод group.count вместо создания нового списка (для ускорения) и проверки условий для след assert

    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравнение соответствия физичского НАЛИЯЧИЯ той или иной группы



    # assert old_groups == new_groups  # сравнения соответствия НАЛИЯЧИЯ той или иной группы
                                     # однако нельзя сравнивать просто как здесь, тк порядок в списке нарушится
                                     # и assert не сработает (см ролик 4_3 sorting_lists)











def test_add_group_constant_data(app, constant):
    added_group = constant
    old_groups = app.group.get_group_list()
    app.group.create(added_group)

    assert len(old_groups) + 1 == app.group.count()

    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
