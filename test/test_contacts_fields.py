
import re

from random import randrange






def test_fields_on_homepage(app):  # метод ПРЯМОЙ  проверки
    all_contacts = app.contact.get_contact_list_split()
    index = randrange(len(all_contacts))

    contact_from_home_page = app.contact.get_contact_list_split()[index] # проверка для первого контакта (пока не для всех)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname

    assert contact_from_home_page.address == contact_from_edit_page.address

    assert contact_from_home_page.email == contact_from_edit_page.email
    assert contact_from_home_page.email2 == contact_from_edit_page.email2
    assert contact_from_home_page.email3 == contact_from_edit_page.email3

    assert contact_from_home_page.landline == clear(contact_from_edit_page.landline)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)


def clear(s):
    return re.sub("[() -]", "", s) # убираем в телефонах круглые скобки, пробелы и тире(чтобы при проверке исключить разные формы ввода номеров)