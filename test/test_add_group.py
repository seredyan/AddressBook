# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # добавили спец символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



# testdata = [    # комбинируем разные варианты случайностей
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(3)
]

@pytest.mark.parametrize("added_group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, added_group):
    old_groups = app.group.get_group_list()
    app.group.create(added_group)

    assert len(old_groups) + 1 == app.group.count() # исп метод group.count вместо создания нового списка (для ускорения) и проверки условий для след assert

    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max) # сравнение соответствия физичского НАЛИЯЧИЯ той или иной группы



    # assert old_groups == new_groups  # сравнения соответствия НАЛИЯЧИЯ той или иной группы
                                     # однако нельзя сравнивать просто как здесь, тк порядок в списке нарушится
                                     # и assert не сработает (см ролик 4_3 sorting_lists)



