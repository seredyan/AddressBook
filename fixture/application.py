
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):     # запуск браузера через этот конструктор
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self) # помощник получает ссылку на объект класса Application
                                           # это даст возможность в одном помощнике обращаться к др помощникам
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()
