# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="First", header="beginning", footer="finishing")) # создаем объект класса с конструктором по умолчанию


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

