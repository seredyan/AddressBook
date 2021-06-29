

from model.contact import Contact

def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(address="Address edited"))
    app.session.logout()


def test_modify_contact_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(mobile="Cell phone number edited"))
    app.session.logout()


def test_modify_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(email="email edited"))
    app.session.logout()


def test_modify_contact_landline(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(landline="Landline edited"))
    app.session.logout()
