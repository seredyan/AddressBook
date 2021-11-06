
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url, headless):     # запуск браузера через этот конструктор

        if browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless: options.headless = True
            self.wd = webdriver.Firefox(options=options)
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless: options.headless = True
            self.wd = webdriver.Chrome(options=options)
        elif browser == "edge":
            self.wd = webdriver.Edge()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        # if browser == "firefox":
        #     self.wd = webdriver.Firefox()
        # elif browser == "chrome":
        #     self.wd = webdriver.Chrome()
        # elif browser == "edge":
        #     self.wd = webdriver.Edge()
        # elif browser == "opera":
        #     self.wd = webdriver.Opera()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.implicitly_wait(3)
        self.session = SessionHelper(self) # помощник получает ссылку на объект класса Application
                                           # это даст возможность в одном помощнике обращаться к др помощникам
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url     # просим браузер сообщить текущий адрес открытой страницы.
            return True              # если браузер сообщит адрес, то возвращаем True.
        except:
            return False           # значит браузер негоден к исп-ю и фикстура тоже



    def open_home_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/index.php"):
            wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()

