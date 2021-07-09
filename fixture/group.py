import random

from model.group import Group


class GroupHelper:
    def __init__(self, app):  #
        self.app = app



    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None  # сбрасываем кэш, тк он теперь невалидный.
                                 # при следующем обращении get_group_list кэш будет построен заново.


    def modify_group_by_index(self, index, group):  # ????? new_group_data -как 2й параметр вместо просто group???
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # select Edit group
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(group)   # ????? new_group_data -как 2й параметр вместо просто group???
        # submit group modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        wd = self.app.wd
        self.modify_group_by_index(0)



    def delete_first_group(self):
        self.delete_group_by_index(0)


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


     # вспомогательные КУСКИ КОДА, повторющиеся внутри различных методов выше

    def open_groups_page(self):
        wd = self.app.wd  # доступ к драйверу осущ через ссылку на основной класс Application (где она общая для всех)
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()





    def fill_group_form(self, group):  # вспомогательный кусок кода по заполнению полей
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

        # wd.find_element_by_name("group_header").click()  # заменили эти строчки на вызов метода change_field_value (выше).
        # wd.find_element_by_name("group_header").clear()
        # wd.find_element_by_name("group_header").send_keys(group.header)
        #
        # wd.find_element_by_name("group_footer").click()
        # wd.find_element_by_name("group_footer").clear()
        # wd.find_element_by_name("group_footer").send_keys(group.footer)


    def change_field_value(self, field_name, text):   #  параметр text - это новый текст вводимый для заполения полей
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


 # # пробная альтернативная идея (см правильный вариант твета в скайпе)
 #
 #    def check(self):
 #        wd = self.app.wd
 #        self.open_groups_page()
 #        if wd.find_element_by_name("selected[]") is False:
 #            self.create(group="test")  # доработать с аргументами!!!
 #            self.delete_first_group()
 #
 #        else:
 #            self.delete_first_group()
 #


    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)








