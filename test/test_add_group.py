# -*- coding: utf-8 -*-

from model.group import Group


# ниже выбирая варианты данных можем генерировать те или иные виды тестовых данных
from data.groups import testdata
# from data.add_group import constant as testdata





def test_add_group(app, data_groups):
    added_group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(added_group)

    assert len(old_groups) + 1 == app.group.count() # исп метод group.count вместо создания нового списка (для ускорения) и проверки условий для след assert

    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравнение соответствия физичского НАЛИЯЧИЯ той или иной группы



    # assert old_groups == new_groups  # сравнения соответствия НАЛИЯЧИЯ той или иной группы
                                     # однако нельзя сравнивать просто как здесь, тк порядок в списке нарушится
                                     # и assert не сработает (см ролик 4_3 sorting_lists)



