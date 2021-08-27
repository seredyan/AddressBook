# -*- coding: utf-8 -*-

from model.contact import Contact
import re


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list_join()
    added_contact = Contact(name="Ivan",
                               lastname="Ivanov", address="Russia",  email="a@gmail.com", email2="b@yandex.ru", email3="c@mail.ru",
                               landline="111", mobile="222", workphone="333", second_landline="444")
    app.contact.create(added_contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list_join()

    readded_contact = Contact(name="Ivan", lastname="Ivanov", address="Russia", all_emails_from_home_page=merge_emails_like_on_home_page(added_contact), all_phones_from_home_page=merge_phones_like_on_home_page(added_contact))
    old_contacts.append(readded_contact)

    print('старые: ', old_contacts, 'новые: ', new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



def test_add_contact_for_service(app):

    app.contact.create(Contact(name="aa",
                               lastname="bb", address="add1",
                               landline="11", mobile="22", workphone='33', second_landline='44', email="m1@ya.ru", email2="m2@ya.ru", email3="m3@ya.ru"))



def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.landline, contact.mobile, contact.workphone, contact.second_landline]))))


def clear(s):
    return re.sub("[() -+]", "", s)
