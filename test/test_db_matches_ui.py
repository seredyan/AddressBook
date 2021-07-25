
from model.group import Group
from timeit import timeit


    ### внутр тест для проверки работы фикстуры соответствия данных UI и БД
   ###Цель:  сравниваем  def get_group_list(self) из fixture.group  и  def get_group_list(self) из fixture.db
def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip()) # удаляем лишние пробелы (кот могут быть напр даже ПОСЛЕ текста, тк в БД обычно ВСЕ отражено, а в UI многое сглаживается
    db_list = map(clean, db.get_group_list())

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)




# # тест сравнения скорости обработки данных с UI (сбор 1 раз) и БД (сбор 1000 раз)
# def test_group_list_timeit(app, db):
#     print(timeit(lambda: app.group.get_group_list(), number=1))
#     def clean(group):
#         return Group(id=group.id, name=group.name.strip())
#     print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
#
#     assert False # так тест упадет и мы увидим необх инфу на консоли (тк для прошедших тестов эта инфа обычно прячется, но не для упавших)