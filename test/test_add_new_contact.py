# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list_split()
    added_contact = Contact(name="Ivan",
                               lastname="Ivanov", address="Russia",  email="@gmail.com", email2="@yandex.ru", email3="mail.ru",
                               landline="111", mobile="222", workphone="333")
    app.contact.create(added_contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list_split()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#
# def test_next_new_contact(app):

#     app.contact.create(Contact(name="Peter",
#                                lastname="Petrov", address="Lenina St, 10-11\nVoronezh, Russia",
#                                landline="3333333", mobile="888888", email="petrov@mail.ru"))
#
#
#



