# -*- coding: utf-8 -*-



from model.contact import Contact



def test_add_new_contact(app, db, check_ui): #json_contacts):
    # added_contact = json_contacts
    old_contacts = db.get_contact_list()

    added_contact = Contact(name="AA",
                               lastname="BB", address="ADD",
                               landline="55", mobile="66", workphone='77', second_landline='88', email="C1@YA.RU", email2="C2@YA.RU", email3="C3@YA.RU")

    app.contact.create(added_contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(added_contact)

    print('  старые: ', old_contacts, 'новые: ', new_contacts)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list_split(), key=Contact.id_or_max)


#
# def test_add_new_contact_ui(app, json_contacts):  # тест через UI минуя БД
#     added_contact = json_contacts
#     old_contacts = app.contact.get_contact_list_split()
#     app.contact.create(added_contact)
#
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list_split()
#     old_contacts.append(added_contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





# def test_add_contact_constant_data(app, data_contacts):   # для отладки тестов
#     added_contact = data_contacts
#     old_contacts = app.contact.get_contact_list_split()
#     app.contact.create(added_contact)
#
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list_split()
#     old_contacts.append(added_contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



