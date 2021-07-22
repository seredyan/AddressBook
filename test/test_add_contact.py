# -*- coding: utf-8 -*-



from model.contact import Contact



def test_add_new_contact(app, json_contacts):
    added_contact = json_contacts
    old_contacts = app.contact.get_contact_list_split()
    app.contact.create(added_contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list_split()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








def test_add_contact_constant_data(app, data_contacts):   # для отладки тестов
    added_contact = data_contacts
    old_contacts = app.contact.get_contact_list_split()
    app.contact.create(added_contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list_split()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



