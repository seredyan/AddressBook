

from selenium import webdriver

class Application:

    def __init__(self):     # запуск браузера через этот конструктор
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

  # ниже идут вспомогательные функции

    def login(self, user, password):
        wd = self.wd
        self.home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def create_contact(self, contact):
        wd = self.wd
        # open home page
        self.home_page()
        # init adding new address
        wd.find_element_by_link_text("add new").click()
        # fill address firm
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.landphone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_homepage()


    def return_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def destroy(self):
        self.wd.quit()

