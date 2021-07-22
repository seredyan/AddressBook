

#  Задание № 14

import re

from random import randrange



def test_fields_on_homepage(app):  # метод ПРЯМОЙ  проверки
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
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.landline, contact.mobile, contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))



def clear(s):
    return re.sub("[() -+]", "", s) # убираем в телефонах круглые скобки, пробелы и тире(чтобы при проверке исключить разные формы ввода номеров)




# def test_fields_on_homepage_direct(app):  # метод ПРЯМОЙ  проверки
#     all_contacts = app.contact.get_contact_list_split()
#     index = randrange(len(all_contacts))
#
#     contact_from_home_page = app.contact.get_contact_list_split()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#
#     assert contact_from_home_page.name == contact_from_edit_page.name
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#
#     assert contact_from_home_page.address == contact_from_edit_page.address
#
#     assert contact_from_home_page.email == contact_from_edit_page.email
#     assert contact_from_home_page.email2 == contact_from_edit_page.email2
#     assert contact_from_home_page.email3 == contact_from_edit_page.email3
#
#     assert clear(contact_from_home_page.landline) == clear(contact_from_edit_page.landline)
#     assert clear(contact_from_home_page.mobile) == clear(contact_from_edit_page.mobile)
#     assert clear(contact_from_home_page.workphone) == clear(contact_from_edit_page.workphone)


