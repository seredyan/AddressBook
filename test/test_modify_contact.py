import random

from model.contact import Contact
from random import randrange

def test_modify_contact_address(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="testName", lastname="testLastname", address='test Address', email='test1@mail.com', email2='test2@mail.com', email3='test3@mail.com', landline='11', mobile='22', workphone='33', second_landline='44'))

    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    index = old_contacts.index(selected_contact)
    modified_contact = Contact(address="Address EDITED")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()
    old_contacts[index].address = modified_contact.address
    print('old_contacts: ', old_contacts)
    print('new_contacts: ', new_contacts)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(), key=Contact.id_or_max)


def test_modify_contact_phone(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="testName", lastname="testLastname", address='test Address', email='test1@mail.com', email2='test2@mail.com', email3='test3@mail.com', landline='11', mobile='22', workphone='33', second_landline='44'))

    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    index = old_contacts.index(selected_contact)
    modified_contact = Contact(mobile="cellEDITED")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()
    old_contacts[index].all_phones_from_home_page = new_contacts[index].all_phones_from_home_page

    print('old_contacts: ', old_contacts)
    print('new_contacts: ', new_contacts)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_email(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="testName", lastname="testLastname", address='test Address', email='test1@mail.com', email2='test2@mail.com', email3='test3@mail.com', landline='11', mobile='22', workphone='33', second_landline='44'))

    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    index = old_contacts.index(selected_contact)
    modified_contact = Contact(email="EDITED@anymail.com")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()
    old_contacts[index].all_emails_from_home_page = new_contacts[index].all_emails_from_home_page

    print('old_contacts: ', old_contacts)
    print('new_contacts: ', new_contacts)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(),
                                                                     key=Contact.id_or_max)



def test_modify_contact_landline(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="testName", lastname="testLastname", address='test Address', email='test1@mail.com', email2='test2@mail.com', email3='test3@mail.com', landline='11', mobile='22', workphone='33', second_landline='44'))

    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    index = old_contacts.index(selected_contact)
    modified_contact = Contact(landline="LandlineEDITED")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()
    old_contacts[index].all_phones_from_home_page = new_contacts[index].all_phones_from_home_page
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(),
                                                                     key=Contact.id_or_max)



