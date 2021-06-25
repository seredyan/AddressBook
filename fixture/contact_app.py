
from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from selenium import webdriver

class Application:

    def __init__(self):     # запуск браузера через этот конструктор
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

