
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()



# ## пробная альтернативная идея
# def test_delete_first_group(app):
#     app.group.check()
#     #app.group.delete_first_group()