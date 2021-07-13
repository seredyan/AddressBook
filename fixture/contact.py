
from model.contact import Contact

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
        self.select_some_contact(0)


    def delete_some_contact(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_some_contact(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(0.3)
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

    #     вспомогательные КУСКИ КОДА, повторющиеся внутри различных методов выше

    def select_modifiable_contact(self, index):
        wd = self.app.wd
        # wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_some_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()



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
        self.change_field_value("email", contact.email)


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


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()

                # другие варианты
                # first_name = row.find_elements_by_tag_name("td")[2].text  # вторая колонка таблицы
                # last_name = row.find_elements_by_tag_name("td")[1].text   # первая колонка таблицы
                # id = row.find_element_by_name("selected[]").get_attribute("value")
                # all_phones = row.find_elements_by_tag_name("td")[5].text.splitlines()
                self.contact_cache.append(Contact(name=first_name, lastname=last_name, id=id,
                                                  landline=all_phones[0], mobile=all_phones[1],
                                                  workphone=all_phones[2]))#, fax=all_phones[3]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_modifiable_contact(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        landline = wd.find_element_by_name("home").get_attribute("value") # выбираем поле редактирования домашн телефона
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        # fax = wd.find_element_by_name("fax").get_attribute("value")
        return Contact(name=first_name, lastname=last_name, id=id,
                       landline=landline, mobile=mobile,
                       workphone=workphone)#, fax=fax)