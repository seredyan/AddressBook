import random

from model.contact import Contact
from random import randrange



def test_delete_some_contact(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    selected_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(selected_contact.id)
    new_contacts = db.get_contact_list()

    assert len(old_contacts) - 1 == len(new_contacts)

    old_contacts.remove(selected_contact)

    assert old_contacts == new_contacts


    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(), key=Contact.id_or_max)




# def test_delete_some_contact_UI(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name="test"))
#     old_contacts = app.contact.get_contact_list_split()
#     index = randrange(len(old_contacts))
#     app.contact.delete_some_contact(index)
#
#     assert len(old_contacts) - 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list_split()
#     old_contacts[index:index+1] = []
#     #old_contacts[0:1] = []
#     # old_contacts.pop(0)
#     assert old_contacts == new_contacts