
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
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        #wd.find_elements_by_css_selector("img[alt='Edit']")[index].click()


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
            for element in wd.find_elements_by_name("entry"):
                first_name = element.find_elements_by_tag_name("td")[2].text
                last_name = element.find_elements_by_tag_name("td")[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=last_name, name=first_name, id=id))
        return list(self.contact_cache)
