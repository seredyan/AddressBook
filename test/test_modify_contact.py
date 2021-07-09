
import model
from model.contact import Contact

def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    modified_contact = Contact(address="Address edited")
    modified_contact.id = old_contacts[0].id
    app.contact.modify_contact(modified_contact)

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    #old_contacts[0] = modified_contact  ?? в отличие от теста удаления контакта эта строчка не нужна, тк ИМЯ контакта НЕ менял!!??
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    modified_contact = Contact(mobile="Cell phone number edited")
    app.contact.modify_contact(modified_contact)
    modified_contact.id = old_contacts[0].id

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    modified_contact = Contact(email="email edited")
    app.contact.modify_contact(modified_contact)
    modified_contact.id = old_contacts[0].id

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



def test_modify_contact_landline(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    modified_contact = Contact(landline="Landline edited")
    app.contact.modify_contact(modified_contact)
    modified_contact.id = old_contacts[0].id

    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

