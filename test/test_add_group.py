# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()  # вначале получаем старый список групп ДО любых действий с ними
    app.group.create(Group(name="First", header="beginning", footer="finishing")) # создаем объект класса с конструктором по умолчанию
    new_groups = app.group.get_group_list()   # получаем новый список групп после создания новой группы
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
