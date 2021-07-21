
import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture                      # объявляем, что собираемся пользоваться этой глобальной переменной
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:                 #  это условие выполняется перед вызовом 1й тестовой ф-ии
        fixture = Application(browser=browser, base_url=base_url)          # инициализируем фикстуру

    else:                     # теперь проверяем, не испортилась ли фикстура
        if not fixture.is_valid():  # если фикстура валидная, то делать ничего не нужно, поэтому ставим NOT чтобы задать дальнейшие шаги.
            fixture = Application(browser=browser, base_url=base_url)  # т.е создаем новую фикстуру для продолжения тестов
    fixture.session.ensure_login(username="admin", password="secret")  # вообще лучше зд НЕ хранить пароль и ук его при запуске
    return fixture



@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    #return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/index.php")


