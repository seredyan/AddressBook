

from model.contact import Contact

def test_modify_contact_address(app):
    app.contact.modify_contact(Contact(address="Address edited"))



def test_modify_contact_phone(app):
    app.contact.modify_contact(Contact(mobile="Cell phone number edited"))


def test_modify_contact_email(app):
    app.contact.modify_contact(Contact(email="email edited"))



def test_modify_contact_landline(app):
    app.contact.modify_contact(Contact(landline="Landline edited"))

