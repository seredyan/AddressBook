

import random

from model.contact import Contact
from model.group import Group


def test_remove_contact_from_group(app, db):


    if db.get_group_list() == []:
        app.group.create(Group(name='test'))
    if db.get_contact_list() == []:
        app.contact.create(Contact(name='test'))

    old_data = db.get_data_address_in_groups()
    if old_data == []:
        app.contact.add_first_contact_into_first_group()

    else:
        row = random.choice(old_data)
        selected_contact = row[0]
        selected_group = row[1]
        app.contact.remove_contact_from_group(selected_contact, selected_group)

    new_data = db.get_data_address_in_groups()
    old_data.remove(row)

    assert sorted(old_data) == sorted(new_data)