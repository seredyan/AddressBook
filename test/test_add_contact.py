# -*- coding: utf-8 -*-



from model.contact import Contact
import re



def test_add_new_contact(app, json_contacts, db, check_ui):

    old_contacts = db.get_contact_list()
    added_contact = json_contacts
    app.contact.create(added_contact)

    new_contacts = db.get_contact_list()
    old_contacts.append(added_contact)

    print('  старые: ', old_contacts, 'новые: ', new_contacts)

    assert old_contacts == new_contacts


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



def test_add_new_single_contact(app, db):

    old_contacts = db.get_contact_list()

    added_contact = Contact(name="AA",
                               lastname="BB", address="ADD",
                               landline="11", mobile="22", workphone='33', second_landline='44',
                            email="C1@YA.RU", email2="C2@YA.RU", email3="C3@YA.RU")

    app.contact.create(added_contact)
    old_contacts.append(added_contact)
    new_contacts = db.get_contact_list()

    print('  старые: ', old_contacts, 'новые: ', new_contacts)

    assert old_contacts == new_contacts





def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.landline, contact.mobile, contact.workphone, contact.second_landline]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear_emails(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))

def clear(s):
    return re.sub("[() -]", "", s)


def clear_emails(s):
    return re.sub("[ ]", "", s)