# -*- coding: utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Address


class TestNewAddress(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_new_address(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd, user="admin", password="secret")
        self.create_contact(wd, Address(name="Georg",
                                        lastname="Wells", street="Lenina St, 10-11\nVoronezh, Russia",
                                        landphone="555555555", mobile="77777777777", email="dd@mail.ru"))
        self.return_homepage(wd)
        self.logout(wd)

    def login(self, wd, user, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def create_contact(self, wd, address):
        # init adding new address
        wd.find_element_by_link_text("add new").click()
        # fill address firm
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(address.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.street)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(address.landphone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(address.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(address.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    # def is_element_present(self, how, what):
    #     try:
    #         self.wd.find_element(by=how, value=what)
    #     except NoSuchElementException as e:
    #         return False
    #     return True
    #
    # def is_alert_present(self):
    #     try:
    #         self.wd.switch_to_alert()
    #     except NoAlertPresentException as e:
    #         return False
    #     return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()