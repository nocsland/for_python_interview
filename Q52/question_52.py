# 52. Приведите пример генератора словарей (dict comprehension)
# Ниже мы создадим словарь с буквами алфавита в качестве ключей и индексами в качестве значений:

# создаем список букв
import string

# выводим алфавит в виде списка
print(list(string.ascii_lowercase))

# присваиваем переменной alphabet полученный список
alphabet = list(string.ascii_lowercase)

# генерация словаря
d = {val: idx for idx, val in enumerate(alphabet)}

# выводим словарь
print(d)
# => {'a': 0,
# => 'b': 1,
# => 'c': 2,
# => ...
# => 'x': 23,
# => 'y': 24,
# => 'z': 25}
