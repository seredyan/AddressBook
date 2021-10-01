import random

def test_add_contact_into_group(db, app):

    db.check_available_parameters(app)

    old_data = db.get_data_address_in_groups()  # список контактов в группах

    selected_data = db.get_selected_groups_and_contacts()
    final_group = selected_data[0]
    selected_contact = selected_data[1]
    app.contact.add_contact_into_group(selected_contact, final_group)

    new_data = db.get_data_address_in_groups()
    old_data.append((int(selected_contact), int(final_group)))

    assert sorted(old_data) == sorted(new_data)



def test_remove_contact_from_group(app, db):

    db.check_available_parameters(app)
    if db.get_data_address_in_groups() == []:
        app.contact.add_first_contact_into_first_group()

    old_data = db.get_data_address_in_groups()
    row = random.choice(old_data)
    selected_contact = row[0]
    selected_group = row[1]
    app.contact.remove_contact_from_group(selected_contact, selected_group)

    new_data = db.get_data_address_in_groups()
    old_data.remove(row)

    assert sorted(old_data) == sorted(new_data)




















# def test_add_missing_contact_into_group(app, db):
#
#     if db.get_group_list() == []:
#         app.group.create(Group(name='test'))
#     if db.get_contact_list() == []:
#         app.contact.create(Contact(name='test'))
#
#     test_data = db.get_data_address_in_groups()
#     if test_data == []:
#         app.contact.add_first_contact_into_first_group()
#
#     else:
#
#
#         data_contacts_id = db.get_contact_list_by_id() # список всех контактов
#         data_groups_id = db.get_group_list_by_id()
#         all_groups_list_in_list = []
#         datas = db.get_data_address_in_groups()    #  список контактов в группах
#         selected_group = [] # список выбранных групп
#         contacts_id = [] #
#         selected_contacts_list = []     # список выбранных контактов для отбора одного   # needet_id
#         selected_groups_list = []    #  спикок отобранных групп для выбора одной    # ww
#         groups_with_contacts = [y for x, y, *z in datas]  # вытаскиваем группы из кортежей, получаем список всех групп, в которых есть контакты
#
#                ### вначале ищем группы, в кот не хватает лишь одного контакта чтобы ее заполнить
#         for group in groups_with_contacts:
#             if groups_with_contacts.count(group) == len(data_contacts_id) - 1:
#                 selected_group.append(group)  # отобраны группы для добавления контакта
#             else:
#                 continue
#
#             ### или ищем группы, в кот не хватает более одного контакта чтобы добавить контакт в одну из них
#         if selected_group == []:
#             for group in groups_with_contacts:
#                 if groups_with_contacts.count(group) < len(data_contacts_id) - 1:
#                     selected_group.append(group)  # отобраны группы для добавления контакта
#                 else:     # если все группы в address_in_groups полные, то проверяем наличие путых групп в БД вообще
#                     if len(data_groups_id) > len(list(set(groups_with_contacts))):
#                         for i in data_groups_id:
#                             all_groups_list_in_list.append((list(i)))
#                             all_groups = [x for l in all_groups_list_in_list for x in l]
#                             for group in all_groups:
#                                 if group not in groups_with_contacts:
#                                     selected_group.append(group)
#                     else:   # если ВСЕ  группы в БД уже полны, создаем новый контакт, чтобы добавить его в любую группу
#                         selected_group = groups_with_contacts
#                         added_contact = Contact(name="testNAME", lastname="testLASTNAME", address="testADDRESS")
#                         app.contact.create(added_contact)
#                         new_contact = db.get_contact_list_by_id()
#                         data_contacts_id.append(new_contact[-1])
#                         break
#
#
#         final_group = random.choice(list(set(selected_group)))  # убираем повторяющиеся и ВЫБИРАЕМ ИТОГОВУЮ ГРУППУ для добавления контакта
#
#             #### производим отбор контакта для добавления в группу
#
#         for i in data_contacts_id:
#             contacts_id.append(list(i))
#             list_id = [x for l in contacts_id for x in l]  # получили чистый список id всех контактов
#
#         for gr in datas:  # собираем в список выбранную группу с контактами, которые уже в ней
#             if gr[1] == final_group:
#                 selected_groups_list.append(gr)
#
#         contacts_in_selected_group = [x[0] for x in selected_groups_list]  # получаем контакты, которые уже есть в выбранной группе
#
#         for id in list_id:    # находим контакты, которых еще нет в выбранной группе, и собираем их в список
#             if id not in contacts_in_selected_group:
#                 selected_contacts_list.append(id)
#             else:
#                 continue
#
#         selected_contact = random.choice(selected_contacts_list)      #выбран КОНЕЧНЫЙ КОНТАКТ для добавления в группу
#
#         app.contact.add_contact_into_group(selected_contact, final_group)
#
#         new_test_data = db.get_data_address_in_groups()
#         test_data.append((selected_contact, final_group))
#
#         print(test_data)
#         print(new_test_data)
#
#         assert sorted(test_data) == sorted(new_test_data)
#
