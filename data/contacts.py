


# фиксированные данные для отладки тестов

from model.contact import Contact

testdata = [
    Contact(name="name1", lastname="lastname1", address="testaddress", landline="1111", mobile="2222", workphone="3333",
            email="test@ya.ru", email2="test@gmail.com", email3="test@icloud.com", second_landline='4444'),
    Contact(name="NAME", lastname="LASTNAME", address="TESTADDRESS", landline="123", mobile="456", workphone="789",
            email="TEST2@ya.ru", email2="TEST2@gmail.com", email3="TEST2@icloud.com", second_landline='999')
]