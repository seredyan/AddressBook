

import random
import string
from model.group import Group






constant = [           # простые фиксированные данные помогают в случае отладки тестов
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 4), header=random_string("header", 5), footer=random_string("footer", 5))
#     for i in range(2)
# ]



# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + " "*3
#     # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # добавили спец символы
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



# testdata = [    # комбинируем разные варианты случайностей
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 20)]
# ]


