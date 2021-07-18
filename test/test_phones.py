

import re
from random import randrange



def test_phones_on_homepage(app): # метод ОБРАТНОЙ проверки РАНДОМНЫЙ контакт
    all_contacts = app.contact.get_contact_list_join()
    index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list_join()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)





# def test_phones_on_homepage_direct(app):   # метод ПРЯМОЙ  проверки РАНДОМНЫЙ контакт
#
#     all_contacts = app.contact.get_contact_list_split()
#     index = randrange(len(all_contacts))
#     contact_from_home_page = app.contact.get_contact_list_split()[index] # проверка для первого контакта (пока не для всех)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_home_page.landline == clear(contact_from_edit_page.landline)
#     assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
#     assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)

#
#
# def test_phones_on_contact_view_page_direct(app):   # метод ПРЯМОЙ  проверки
#     contact_from_view_page = app.contact.get_contact_from_view_page(1)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
#
#     assert contact_from_view_page.landline == contact_from_edit_page.landline
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     # assert contact_from_view_page.email == contact_from_edit_page.email


def test_phones_on_contact_view_page(app):   # метод ОБРАТНОЙ  проверки
    all_contacts = app.contact.get_contact_list_join()
    index = randrange(len(all_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page_join(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert merge_phones_like_on_view_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_view_page.all_emails_from_view_page == merge_emails_like_on_home_page(contact_from_edit_page)

    # assert contact_from_view_page.all_phones_from_view_page == merge_phones_like_on_home_page(contact_from_edit_page)






def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.landline, contact.mobile, contact.workphone]))))

def merge_phones_like_on_view_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.all_phones_from_view_page]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

def clear(s):
    return re.sub("[() -]", "", s) # убираем в телефонах круглые скобки, пробелы и тире(чтобы при проверке исключить разные формы ввода номеров)
