# 54. Какие коллекции существуют в Python
#
# Список, кортеж, строка, множество, словарь
#
# Как создать:

my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3, 4)
my_string = "Строка"
my_set = {1, 2, 2, 3, 6, 4, 6, 7}
my_dict = {'key1': 'value1', 'key2': 'value2'}

print(type(my_list))
print(type(my_tuple))
print(type(my_string))
print(type(my_set))
print(type(my_dict))

my_set_two = set(my_set)

