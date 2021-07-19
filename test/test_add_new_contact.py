# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # добавили спец символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_char_email(maxlen):
    random_emails = ["@gmail.com", "@ya.ru", "@mail.ru", "@icloud.com", "@company.com", "yahoo.com", "@outlook.com"]
    symbols = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(maxlen))))
    return (symbols + random.choice(random_emails))

def random_digits_phone(maxlen):
    symbols = string.digits #+ " " * 3
    return "".join([random.choice(symbols) for i in range(maxlen)])




testdata = [Contact(name=random_string("NAME", 5), lastname=random_string("LASTNAME", 5), address=random_string("countryX", 5),
                    email=random_char_email(5), email2=random_char_email(5), email3=random_char_email(5), landline=random_digits_phone(11),
                    mobile=random_digits_phone(11), workphone=random_digits_phone(11)) for i in range(5)]

@pytest.mark.parametrize("added_contact", testdata, ids=[repr(x) for x in testdata])

def test_add_new_contact(app, added_contact):
    old_contacts = app.contact.get_contact_list_split()
    app.contact.create(added_contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list_split()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)













# def test_add_new_contact(app):
#     old_contacts = app.contact.get_contact_list_split()
#     added_contact = Contact(name="Ivan",
#                                lastname="Ivanov", address="Russia",  email="abc@gmail.com", email2="xy@yandex.ru", email3="we@mail.ru",
#                                landline="111", mobile="222", workphone="333")
#     app.contact.create(added_contact)
#
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list_split()
#     old_contacts.append(added_contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#
# def test_next_new_contact(app):

#     app.contact.create(Contact(name="Peter",
#                                lastname="Petrov", address="Lenina St, 10-11\nVoronezh, Russia",
#                                landline="3333333", mobile="888888", email="petrov@mail.ru"))
#
#
#



