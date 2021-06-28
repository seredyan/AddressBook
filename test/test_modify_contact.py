

from model.contact import Contact

def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact_address(Contact(address="Address edited"))
    app.session.logout()


def test_modify_contact_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact_phone(Contact(mobile="Cell phone number edited"))
    app.session.logout()


def test_modify_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact_email(Contact(email="email edited"))
    app.session.logout()


def test_modify_contact_landline(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact_phone(Contact(landline="Landline edited"))
    app.session.logout()
