
# import time
from model.contact import Contact
from random import randrange



def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="NAME", lastname='LASTNAME', address='ADDRESS', landline='11', mobile='22', workphone='33', email='1@mail.ru', email2='2@gmail.com', email3='3@ya.ru', second_landline='44'))
    old_contacts = app.contact.get_contact_list_join()
    index = randrange(len(old_contacts))
    modified_contact = Contact(mobile="EDITED")
    modified_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, modified_contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list_join()
    old_contacts[index].all_phones_from_home_page = new_contacts[index].all_phones_from_home_page
    # old_contacts[index].mobile = modified_contact.mobile  # не нужна строчка тк нет отд проверки __eq__  для мобилы
    print('old: ', old_contacts, 'new: ', new_contacts)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="NAME", lastname='LASTNAME', address='ADDRESS', landline='11', mobile='22', workphone='33', email='1@mail.ru', email2='2@gmail.com', email3='3@ya.ru', second_landline='44'))
    old_contacts = app.contact.get_contact_list_join()
    index = randrange(len(old_contacts))
    modified_contact = Contact(email="EDITED@somemail.com")
    modified_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, modified_contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list_join()
    old_contacts[index].all_emails_from_home_page = new_contacts[index].all_emails_from_home_page

    print('old: ', old_contacts, 'new: ', new_contacts)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



def test_modify_contact_landline(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="NAME", lastname='LASTNAME', address='ADDRESS', landline='11', mobile='22', workphone='33', email='1@mail.ru', email2='2@gmail.com', email3='3@ya.ru', second_landline='44'))
    old_contacts = app.contact.get_contact_list_join()
    index = randrange(len(old_contacts))
    modified_contact = Contact(landline="Landline EDITED")
    modified_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, modified_contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list_join()
    old_contacts[index].all_phones_from_home_page = new_contacts[index].all_phones_from_home_page
    print('old: ', old_contacts, 'new: ', new_contacts)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_address(app):
    # time.sleep(15)
    if app.contact.count() == 0:
        app.contact.create(
            Contact(name="NAME", lastname='LASTNAME', address='ADDRESS', landline='11', mobile='22', workphone='33',
                    email='1@mail.ru', email2='2@gmail.com', email3='3@ya.ru', second_landline='44'))
    old_contacts = app.contact.get_contact_list_join()
    index = randrange(len(old_contacts))
    modified_contact = Contact(address="Address EDITED")
    modified_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, modified_contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list_join()
    old_contacts[index].address = modified_contact.address
    print('old: ', old_contacts, 'new: ', new_contacts)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

