
import random
import string
import os.path
import jsonpickle
from model.group import Group
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a




def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10  # добавили спец символы
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])





testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 4), header=random_string("header", 5), footer=random_string("footer", 5))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) # 2 точки означает что поднимаемся на 2 ур-ня вышеб а потом идем по пути f
# other way:   file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")
# из родительской директории перпходим выше в подкаталог data

with open(file, "w") as file_out:
    jsonpickle.set_encoder_options("json", indent=2)
    file_out.write(jsonpickle.encode(testdata))

