# -*- coding: utf-8 -*-

from model.contact import Contact


def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="Georg",
                                    lastname="Wells", address="Lenina St, 10-11\nVoronezh, Russia",
                                    landphone="555555555", mobile="77777777777", email="dd@mail.ru"))

    app.session.logout()








