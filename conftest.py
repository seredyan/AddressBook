
import pytest
from fixture.application import Application


@pytest.fixture(scope="session") # браузер открывается в рамках одной сессии (пока не выполнятся все тесты)
#@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
