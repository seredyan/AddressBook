

from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    modified_group = Group(name="Name edited")
    modified_group.id = old_groups[0].id # сохраняем id модифицируемой группы, чтобы он не потерялся в процессе модификации
    app.group.modify_first_group(modified_group) # создаем объект класса с конструктором по умолчанию
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = modified_group # делаем замену групп (но id не изменится, тк мы его сохранили выше)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # итог этого теста свидетельствуют, что id у групп сохранились и несмотря на то что порядок групп при модификации
    # поменялся, мы эти группы отсортировали и теперь у них правильное соотвтсвие по id и именам (благодаря modified_group.id = old_groups[0].id)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="header edited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
