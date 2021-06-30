
import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture                      # объявляем, что собираемся пользоваться этой глобальной переменной
    if fixture is None:                 #  это условие выполняется перед вызовом 1й тестовой ф-ии
        fixture = Application()          # инициализируем фикстуру

    else:                     # теперь проверяем, не испортилась ли фикстура
        if not fixture.is_valid():  # если фикстура валидная, то делать ничего не нужно, поэтому ставим NOT чтобы задать дальнейшие шаги.
            fixture = Application()  # т.е создаем новую фикстуру для продолжения тестов
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    #return fixture






