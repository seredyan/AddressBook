
##  Это файл-запускатель сценария ##

from pytest_bdd import scenario
from .group_steps import *


## ролик 10_1

@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass  #  зд заглушка потому что вся реализация описана в сценарии и шагах


@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass  #  зд заглушка потому что вся реализация описана в сценарии и шагах
