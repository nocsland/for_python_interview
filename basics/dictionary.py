# Словари
# Словарь — неупорядоченный набор пар ключ-значение. Словарь, как и список — изменяемый тип данных.

# В словаре индексом может быть любой неизменяемый тип данных. Словарь обозначается с помощью фигурных скобок, а
# индексы, которые в словаре принято называть ключами, разделяются со значениями двоеточием. Элементы у словаря, как и
# у списка, разделены запятыми.

# Создать пустой словарь
my_empty_dict = {}

# Создать словарь с данными
my_dict = {
    "first": "Первый",
    "second": "Второй",
    3: "Третий"
}

# Вывести значение по ключу
print(my_dict["second"])
print(my_dict[3])

# Обновить данные по ключу. Если будет указан существующий ключ, данные будут перезаписаны.
my_dict[3] = "Third"
print(my_dict[3])

# Если добавить пару с новым ключом, будет создана новая запись
my_dict[4] = "Четвертый ключ"
print(my_dict[4])

my_dict = {'first': "первый", 'second': 'второй', 'third': 'третий'}
for k in my_dict:
    # Вывести все ключи
    print(k)

    # Вывести все пары
for k in my_dict:
    print(k, '=', my_dict[k])
