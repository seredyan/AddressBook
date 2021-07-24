
from model.group import Group


# внутр тест для проверки работы фикстуры соответствия данных UI и БД
# Цель:  сравниваем  def get_group_list(self) из fixture.group  и  def get_group_list(self) из fixture.db
def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip()) # удаляем лишние пробелы (кот могут быть напр даже ПОСЛЕ текста, тк в БД обычно ВСЕ отражено, а в UI многое сглаживается
    db_list = map(clean, db.get_group_list())

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_l ist, key=Group.id_or_max)