# 55. Особые методы списка .sort() и .reverse()
#
# У списка (и только у него) есть особые методы .sort() и .reverse() которые делают то же самое, что соответствующие
# функции sorted() и reversed(), но при этом:
#
# Меняют сам исходный список, а не генерируют новый; Возвращают None, а не новый список; поддерживают те же
# дополнительные аргументы; в них не надо передавать сам список первым параметром, более того, если это сделать — будет
# ошибка — не верное количество аргументов.

my_list = [2, 5, 1, 7, 3]
my_list.sort()
print(my_list)  # [1, 2, 3, 5, 7]

# Обратите внимание: Частая ошибка начинающих, которая не является ошибкой для интерпретатора, но приводит не к тому
# результату, что хотят получить.

# Ошибочный подход
my_list = [2, 5, 1, 7, 3]
my_list = my_list.sort()
print(my_list)

# Верный подход
my_list = [21, 12, 53, 54, 65]
my_list_new = sorted(my_list)
print(my_list_new)

my_list = [2, 5, 1, 7, 3]
my_list.sort()
print(my_list)

# Ошибочный подход reverse
my_list = [2, 5, 1, 7, 3]
my_list = my_list.reverse()
print(my_list)

# Верный подход
my_list = [21, 12, 53, 54, 65]
my_list_reversed = reversed(my_list)
print([i for i in my_list_reversed])

my_list = [2, 5, 1, 7, 3]
my_list.reverse()
print(my_list)
