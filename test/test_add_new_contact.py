# -*- coding: utf-8 -*-

from model.contact import Contact


def test_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(name="Ivan",
                               lastname="Ivanov", address="Pushkina Sqr, 10-11\nMoscow, Russia",
                               landline="555555555", mobile="77777777777", email="ivanov@mail.ru"))

    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)





#
# def test_next_new_contact(app):

#     app.contact.create(Contact(name="Peter",
#                                lastname="Petrov", address="Lenina St, 10-11\nVoronezh, Russia",
#                                landline="3333333", mobile="888888", email="petrov@mail.ru"))
#
#
#



