# pytest_addoption это хук предназначен для добавления параметров к параметрам, уже доступным в командной строке
# pytest.
# Добавление параметров командной строки через pytest_addoption должно выполняться через плагины или в файле
# contest.py расположенного в верхней части структуры каталога проекта. Вы не должны делать это в тестовом подкаталоге.

def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true", help="some boolean option")
    parser.addoption("--foo", action="store", default="bar", help="foo: bar or baz")
