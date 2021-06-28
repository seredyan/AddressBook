# -*- coding: utf-8 -*-

from model.contact import Contact


def test_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="Ivan",
                               lastname="Ivanov", address="Pushkina Sqr, 10-11\nMoscow, Russia",
                               landline="555555555", mobile="77777777777", email="ivanov@mail.ru"))

    app.session.logout()


#
# def test_next_new_contact(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.create(Contact(name="Peter",
#                                lastname="Petrov", address="Lenina St, 10-11\nVoronezh, Russia",
#                                landline="3333333", mobile="888888", email="petrov@mail.ru"))
#
#     app.session.logout()
#



