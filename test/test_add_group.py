# -*- coding: utf-8 -*-

from model.group import Group



def test_add_group(app):
    old_groups = app.group.get_group_list()  # вначале получаем старый список групп ДО любых действий с ними
    added_group = Group(name="First", header="beginning", footer="finishing")
    app.group.create(added_group) # создаем объект класса с конструктором по умолчанию
    new_groups = app.group.get_group_list()   # получаем новый список групп после создания новой группы
    assert len(old_groups) + 1 == len(new_groups)   # сравнения соответствия обычного КОЛИЧЕСТВА групп
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравнение соответствия физичского НАЛИЯЧИЯ той или иной группы

    # assert old_groups == new_groups  # сравнения соответствия НАЛИЯЧИЯ той или иной группы
                                     # однако нельзя сравнивать просто как здесь, тк порядок в списке нарушится
                                     # и assert не сработает (см ролик 4_3 sorting_lists)



def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    added_group = Group(name="", header="", footer="")
    app.group.create(added_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
