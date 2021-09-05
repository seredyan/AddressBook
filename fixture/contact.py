import optparse
import time
import re
from model.contact import Contact
from selenium.webdriver.support.ui import Select
import random


class ContactHelper:
    def __init__(self, app):
        self.app = app



    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()    # обращение к фикстуре, где находится метод home_page
        # init adding new address
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        #wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()   # старый селектор элемента "submit"
        wd.find_element_by_name("submit").click()
        self.return_homepage()
        self.contact_cache = None


    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_some_contact_ui(0)


    def delete_some_contact(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_some_contact_ui(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(0.3)
        wd.find_element_by_css_selector("div.msgbox")
        self.return_homepage()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_deletable_contact_by_id(id)
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(0.5)
        wd.find_element_by_css_selector("div.msgbox")
        self.return_homepage()
        self.contact_cache = None

    # def modify_contact(self, contact):
    #     wd = self.app.wd
    #     self.app.open_home_page()
    #
    #     #self.select_first_contact()
    #     #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[4]/td[8]/a/img").click()
    #     #wd.find_element_by_xpath("//img[@alt='Edit']").click()
    #
    #     wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
    #     self.fill_contact_form(contact)
    #     wd.find_element_by_name("update").click()
    #     self.return_homepage()
    #     self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()

        # self.select_first_contact()
        # wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[4]/td[8]/a/img").click()
        # wd.find_element_by_xpath("//img[@alt='Edit']").click()

        self.select_modifiable_contact(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_homepage()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_modifiable_contact_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_homepage()
        self.contact_cache = None


    def add_contact_into_group(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # time.sleep(3)

        # time.sleep(4)
        wd.find_element_by_name("to_group").click()
        all_options = wd.find_elements_by_tag_name("option")
        random.choice(all_options).click()
        # time.sleep(4)
        # Select(wd.find_element_by_name("to_group")).select_by_visible_text('First') # пример добавления в конкретную группу(если она есть в списке)
        self.select_some_contact_ui(index)
        wd.find_element_by_name("add").click()
        time.sleep(2)
        # self.return_homepage()
        self.contact_cache = None





    ###     вспомогательные КУСКИ КОДА, повторющиеся внутри различных методов выше


    def select_modifiable_contact(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()




    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_some_contact_ui(self, index):    # чтобы выбрать случайный контакт для удаления
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_modifiable_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def select_deletable_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()





    def change_field_value(self, field_name, text):    #  параметр text - это новый текст вводимый для заполения полей
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.landline)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("phone2", contact.second_landline)



        # wd.find_element_by_name("firstname").click()
        # wd.find_element_by_name("firstname").clear()
        # wd.find_element_by_name("firstname").send_keys(contact.name)
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        # wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # wd.find_element_by_name("address").click()
        # wd.find_element_by_name("address").clear()
        # wd.find_element_by_name("address").send_keys(contact.address)
        # wd.find_element_by_name("home").click()
        # wd.find_element_by_name("home").clear()
        # wd.find_element_by_name("home").send_keys(contact.landphone)
        # wd.find_element_by_name("mobile").click()
        # wd.find_element_by_name("mobile").clear()
        # wd.find_element_by_name("mobile").send_keys(contact.mobile)
        # wd.find_element_by_name("email").click()
        # wd.find_element_by_name("email").clear()
        # wd.find_element_by_name("email").send_keys(contact.email)



    def return_homepage(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None


    def get_contact_list_join(self):     #  # метод ОБРАТНОЙ проверки  (без сплит)
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text

                # другие варианты
                # first_name = row.find_elements_by_tag_name("td")[2].text  # вторая колонка таблицы
                # last_name = row.find_elements_by_tag_name("td")[1].text   # первая колонка таблицы
                # id = row.find_element_by_name("selected[]").get_attribute("value")
                # all_phones = row.find_elements_by_tag_name("td")[5].text.splitlines()
                self.contact_cache.append(Contact(name=first_name, lastname=last_name,
                                                  address=address, id=id, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))

        return list(self.contact_cache)



    def get_contact_list_join_for_db(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text

                self.contact_cache.append(Contact(name=first_name, lastname=last_name, address=address,
                                                  id=id, all_emails_from_home_page=all_emails.split(),
                                                  all_phones_from_home_page=all_phones.split()))

        return list(self.contact_cache)


    def get_contact_list_split(self):  # метод ПРЯМОЙ  проверки   split (работает только, если ВСЕ поля заполнены!!!)
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                emails = cells[4].text.splitlines()
                all_phones = cells[5].text.splitlines()  # если отсутствует один из номеров, то будет пустое место на которое наложится след номер

                # другие варианты
                # first_name = row.find_elements_by_tag_name("td")[2].text  # вторая колонка таблицы
                # last_name = row.find_elements_by_tag_name("td")[1].text   # первая колонка таблицы
                # id = row.find_element_by_name("selected[]").get_attribute("value")
                # all_phones = row.find_elements_by_tag_name("td")[5].text.splitlines()

                self.contact_cache.append(Contact(name=first_name, lastname=last_name,
                                                  id=id, address=address, email=emails[0], email2=emails[1], email3=emails[2],
                                                  landline=all_phones[0], mobile=all_phones[1], workphone=all_phones[2],
                                                  second_landline=all_phones[3]))

        return list(self.contact_cache)



    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_modifiable_contact(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        landline = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        second_landline = wd.find_element_by_name("phone2").get_attribute("value")
        # fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(name=first_name, lastname=last_name, id=id, address=address, email=email, email2=email2, email3=email3,
                       landline=landline, mobile=mobile,
                       workphone=workphone, second_landline=second_landline)



    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()

        # wd.find_elements_by_tag_name("td")[6].click()
        # OR
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()





    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text

        landline = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        second_landline = re.search("P: (.*)", text).group(1)

        return Contact(landline=landline, mobile=mobile, workphone=workphone, second_landline=second_landline)# email=email)



    def get_contact_from_view_page_join(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        all_info_on_page = re.search('H: (.*)\nM: (.*)\nW: (.*)', text).group()
        add_phone = re.search('P: (.*)', text).group()
        phone2 = re.sub('P:', '\n', add_phone)

        all_phones_on_page = re.findall(r'[^H:M:W:]', all_info_on_page)
        all_phones = ''.join(all_phones_on_page)

        total_phones = all_phones + phone2

        emails_list = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)
        all_emails = '\n'.join(emails_list)

        #
        # landline = re.search("H: (.*)", text).group(1)
        # mobile = re.search("M: (.*)", text).group(1)
        # workphone = re.search("W: (.*)", text).group(1)
        # phones_list = [landline, mobile, workphone]
        # all_phones = '\n'.join(phones_list)

        # all_phones_on_page = re.search('H: (.*)\nM: (.*)\nW: (.*)', text).group(1, 2, 3)
        # aaa = '\n'.join(all_phones_on_page)
        # phones_list = [aaa]
        # all_phones = '\n'.join(phones_list)

        # all_phones_on_page = re.search('H: (.*)\nM: (.*)\nW: (.*)', text)
        # landline = all_phones_on_page.group(1)
        # mobile = all_phones_on_page.group(2)
        # workphone = all_phones_on_page.group(3)
        # phones_list = [landline, mobile, workphone]
        # all_phones = '\n'.join(phones_list)


        return Contact(all_phones_from_view_page=total_phones, all_emails_from_view_page=all_emails)
