# -*- coding: utf-8 -*-
from fixture.contact_app import Application
import pytest
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="Georg",
                                    lastname="Wells", address="Lenina St, 10-11\nVoronezh, Russia",
                                    landphone="555555555", mobile="77777777777", email="dd@mail.ru"))

    app.session.logout()








