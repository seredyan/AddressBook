
from model.contact import Contact
from random import randrange


def test_add_contact_into_group(app, db):
    if db.get_contact_list() == []:
        app.contact.create(Contact(name='test'))


    list_contacts = app.contact.get_contact_list_join()
    index = randrange(len(list_contacts) - 1)
    app.contact.add_contact_into_group(index)
