

import re

from random import randrange
from model.contact import Contact


def test_fields_on_homepage(app):  # метод ПРЯМОЙ  проверки
    if app.contact.get_contact_list_join() == 0:
        app.contact.create(Contact(name='testName', lastname='testLastname', address='test Address', email='test@mail.ru', email2='test2@mail.ru', email3='test3@mail.ru', landline='11', mobile='22', workphone='33', second_landline='44'))


    all_contacts = app.contact.get_contact_list_join()
    index = randrange(len(all_contacts))

    contact_from_home_page = app.contact.get_contact_list_join()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname

    assert contact_from_home_page.address == contact_from_edit_page.address

    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)




def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.landline, contact.mobile, contact.workphone, contact.second_landline]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def clear(s):
    return re.sub("[() -+]", "", s) # убираем в телефонах круглые скобки, пробелы и тире и плюс (чтобы при проверке исключить разные формы ввода номеров)