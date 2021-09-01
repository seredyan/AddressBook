
from model.contact import Contact
import re

def test_all_contacts_on_home_page_to_dbase(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="testName", lastname="testLastname", address='test Address', email='test1@mail.com',
                               email2='test2@mail.com', email3='test3@mail.com', landline='11', mobile='22',
                               workphone='33', second_landline='44'))

    all_contacts = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list_join_for_db()

    print('количество в БД: ', len(all_contacts), 'количесво на гл странице: ', len(contacts_from_home_page))
    print('DB: ', all_contacts, 'homepage: ', contacts_from_home_page)


    assert sorted(all_contacts, key=Contact.id_or_max) == sorted(contacts_from_home_page, key=Contact.id_or_max)