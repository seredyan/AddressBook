# -*- coding: utf-8 -*-
from application import Application
import pytest
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="Georg",
                                    lastname="Wells", address="Lenina St, 10-11\nVoronezh, Russia",
                                    landphone="555555555", mobile="77777777777", email="dd@mail.ru"))

    app.logout()





    # def login(self, user, password):
    #     wd = self.wd
    #     wd.find_element_by_name("user").click()
    #     wd.find_element_by_name("user").clear()
    #     wd.find_element_by_name("user").send_keys(user)
    #     wd.find_element_by_name("pass").click()
    #     wd.find_element_by_name("pass").clear()
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//input[@value='Login']").click()
    #
    # def home_page(self, wd):
    #     wd = self.wd
    #     wd.get("http://localhost/addressbook/index.php")
    #
    # def create_contact(self, contact):
    #     wd = self.wd
    #     # open home page
    #     self.home_page(wd)
    #     # init adding new address
    #     wd.find_element_by_link_text("add new").click()
    #     # fill address firm
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(contact.name)
    #     wd.find_element_by_name("lastname").click()
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(contact.lastname)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(contact.address)
    #     wd.find_element_by_name("home").click()
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys(contact.landphone)
    #     wd.find_element_by_name("mobile").click()
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(contact.mobile)
    #     wd.find_element_by_name("email").click()
    #     wd.find_element_by_name("email").clear()
    #     wd.find_element_by_name("email").send_keys(contact.email)
    #     wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
    #
    # def return_homepage(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("home page").click()
    #
    # def logout(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("Logout").click()
    #
    #
    #
    # def tearDown(self):
    #     self.wd.quit()


