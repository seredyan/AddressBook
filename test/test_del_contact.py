
from model.contact import Contact
from random import randrange



def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list_split()
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact(index)

    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list_split()
    old_contacts[index:index+1] = []
    #old_contacts[0:1] = []
    # old_contacts.pop(0)
    assert old_contacts == new_contacts