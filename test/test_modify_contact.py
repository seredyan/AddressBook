
import model
from model.contact import Contact

def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    modified_contact = Contact(name="Anna", lastname="D", address="Address edited")
    modified_contact.id = old_contacts[0].id
    app.contact.modify_contact(modified_contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_phone(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_contact(Contact(mobile="Cell phone number edited"))


def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_contact(Contact(email="email edited"))



def test_modify_contact_landline(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_contact(Contact(landline="Landline edited"))

