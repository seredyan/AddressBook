
from model.contact import Contact
from random import randrange



def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="NAME", lastname='LASTNAME', address='ADDRESS', landline='11', mobile='22', workphone='33', email='1@mail.ru', email2='2@gmail.com', email3='3@ya.ru', second_landline='44'))
    old_contacts = app.contact.get_contact_list_join()
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact(index)

    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list_join()
    old_contacts[index:index+1] = []

    # другие варианты
    #old_contacts[0:1] = []
    # old_contacts.pop(0)

    print('старые: ', old_contacts, 'новые: ', new_contacts)
    assert old_contacts == new_contacts