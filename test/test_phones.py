
#from model.contact import Contact
import re
import random
import string

#
# def test_phones_on_homepage(app):
#     contact_from_home_page = app.contact.get_contact_list()[0] # проверка для первого контакта (пока не для всех)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_homepage(app):
    contact_from_home_page = app.contact.get_contact_list()[0] # проверка для первого контакта (пока не для всех)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.landline == contact_from_edit_page.landline
    assert contact_from_home_page.mobile == contact_from_edit_page.mobile
    assert contact_from_home_page.workphone == contact_from_edit_page.workphone




def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)  # проверка для первого контакта (пока не для всех)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.landline == contact_from_edit_page.landline
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.landline, contact.mobile, contact.workphone]))))



def clear(s):
    return re.sub("[() -]", "", s) # убираем в телефонах круглые скобки, пробелы и тире(чтобы при проверке исключить разные формы ввода номеров)
