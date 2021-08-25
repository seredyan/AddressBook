import random

from model.contact import Contact
from random import randrange

def test_modify_contact_address(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    index = old_contacts.index(selected_contact)
    modified_contact = Contact(address="Address EDITED")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()
    old_contacts[index] = modified_contact
    print('old_contacts: ', old_contacts)
    print('new_contacts: ', new_contacts)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(), key=Contact.id_or_max)


def test_modify_contact_phone(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    modified_contact = Contact(mobile="cell edited")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()
    print('old_contacts: ', old_contacts)
    print('new_contacts: ', new_contacts)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_email(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    modified_contact = Contact(email="EDITED@anymail.com")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()

    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(),
                                                                     key=Contact.id_or_max)



def test_modify_contact_landline(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    modified_contact = Contact(landline="Landline edited")
    modified_contact.id = selected_contact.id
    app.contact.modify_contact_by_id(selected_contact.id, modified_contact)

    new_contacts = db.get_contact_list()

    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(),
                                                                     key=Contact.id_or_max)


## modify by index (sample)
def test_modify_contact_address_by_index(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    modified_contact = Contact(address="Address EDITED")
    modified_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, modified_contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list_split()
    # # #old_contacts[0] = modified_contact  ?? в отличие от теста удаления контакта эта строчка не нужна, тк ИМЯ контакта НЕ менял!!??
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
