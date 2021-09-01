
import random
import string
import os.path
import json
import jsonpickle
from model.contact import Contact
import getopt
import sys
import re


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # добавили спец символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_char_email(maxlen):
    random_emails = ["@gmail.com", "@ya.ru", "@mail.ru", "@icloud.com", "@company.com", "@yahoo.com", "@outlook.com"]
    symbols = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randrange(maxlen))))
    return (symbols + random.choice(random_emails))

def random_digits_phone(maxlen):
    symbols = string.digits #+ " " * 3
    return "".join([random.choice(symbols) for i in range(maxlen)])




testdata = [Contact(name=random_string("NAME", 2), lastname=random_string("LASTNAME", 2), address=random_string("countryX", 2),
                    landline=random_digits_phone(3),
                    mobile=random_digits_phone(3), workphone=random_digits_phone(3),
                    second_landline=random_digits_phone(3),
            email=random_char_email(2), email2=random_char_email(2), email3=random_char_email(2)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as file_out:
    jsonpickle.set_encoder_options("json", indent=2)
    file_out.write(jsonpickle.encode(testdata))


