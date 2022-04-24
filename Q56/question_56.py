# 56. Объясните разницу между генератором и итератором
# Генератор создает коллекцию, а итератор извлекает данные из существующей.

# Пример генератора:
def my_generator():
    return [i for i in range(10)]


print(my_generator())

# Пример итератора:
my_list = [1, 10, 15, 25, 64, 86]


def my_iterator():
    return [i for i in my_list]


print(my_iterator())
