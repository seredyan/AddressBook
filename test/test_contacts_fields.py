

from model.contact import Contact
import re
import random
#from random import randrange


def test_fields_on_homepage(app, db, check_ui):  # метод ПРЯМОЙ  проверки
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="testName", lastname="testLastname", address='test Address', email='test1@mail.com', email2='test2@mail.com', email3='test3@mail.com', landline='11', mobile='22', workphone='33'))
    all_contacts = db.get_contact_list()
    selected_contact = random.choice(all_contacts)
    index = all_contacts.index(selected_contact)

    contact_from_home_page = app.contact.get_contact_list_join()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)


    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_all_contacts_on_home_page_to_dbase(app, db):
    all_contacts = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list_join()

    print('количество в БД: ', len(all_contacts), 'количесво на гл странице: ', len(contacts_from_home_page))
    print('DB: ', all_contacts, 'homepage: ', contacts_from_home_page)

    assert all_contacts == contacts_from_home_page





def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.landline, contact.mobile, contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))



def clear(s):
    return re.sub("[() -+]", "", s) # убираем в телефонах круглые скобки, пробелы, тире  и плюсы(чтобы при проверке исключить разные формы ввода номеров)



#
# def test_fields_on_homepage_direct_ui(app):  # метод ПРЯМОЙ  проверки
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
#

