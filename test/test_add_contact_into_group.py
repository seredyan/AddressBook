import random

from model.contact import Contact
from model.group import Group
from random import randrange
import time


def test_add_contact_into_group(app, db):
    if db.get_contact_list() == []:
        app.contact.create(Contact(name='test'))


    contacts_list = db.get_contact_list()
    selected_contact = random.choice(contacts_list)
    app.contact.add_contact_into_group(selected_contact.id)



def test_print_lists(app, db):
    groups = db.get_group_list()
    # contacts = db.get_contact_list()
    datas = db.get_contacts_in_groups_list()
    print(' группы: ', datas)#, ' контакты: ', contacts)
    for i in datas:
        print(i)
