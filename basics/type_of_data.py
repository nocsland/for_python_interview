# Типы данных

# Числа
# int, float, complex
# Мы можем использовать функцию type(), чтобы узнать класс переменной или значения, и функцию isinstance() для проверки
# принадлежности объекта определённому классу.
a = int(10)
b = float(2)
c = complex(2 + 2j)
print(type(a))
print(type(b))
print(type(c))
print(isinstance(1 + 2j, int))

# Целые числа могут быть любой длины, они ограничиваются лишь доступной памятью.

# Числа с плавающей запятой имеют ограниченную точность. Визуально разницу между целым числом и числом с плавающей
# запятой можно заметить в консоли по наличию точки: 1 — целое число, 1.0 — с плавающей запятой.

# Списки
# Списки являются изменяемым типом, т.е. значения его элементов можно изменить

# Список представляет собой упорядоченную последовательность элементов.
# Объявить список довольно просто. Внутрь квадратных скобок помещаются элементы списка, разделённые запятой:
_list = [1, 2.0, 'три']
# Извлечение по индексу
print(_list[2])

# Кортежи
# Так же как и список, кортеж (tuple) является упорядоченной последовательностью элементов. Вся разница заключается
# в том, что кортежи неизменяемы.
# Кортежи используются для защиты данных от перезаписи и обычно работают быстрее, чем списки, т.к. их нельзя изменять.
# Для создания кортежа нужно поместить внутрь круглых скобок элементы, разделённые запятой:
_tuple = (1, 2.0, 'три')

# Мы можем использовать оператор извлечения среза [] для извлечения элементов, но мы не можем менять их значения:
# _tuple[0] = 2 это вызовет ошибку

# Строки
# Строка представляет собой последовательность символов. Мы можем использовать одинарные или двойные кавычки для
# создания строки.  Многострочные строки можно обозначить тройными кавычками, ''' или """:
s1 = "Простая строка"
s2 = """Многострочная
        строка"""
# Как и в случае со списками и кортежами, мы можем использовать оператор [] и со строками.
# Стоит отметить, что строки в Python относятся к категории неизменяемых последовательностей, то есть все функции и
# методы могут лишь создавать новую строку.

# Множества
# Множество является неупорядоченной уникализированной последовательностью. Объявляется множество с помощью элементов,
# разделённых запятой, внутри фигурных скобок:
_set = {1, 2, 3, 3}
print(_set)
# Над множествами можно выполнять такие операции, как объединение и пересечение. Т.к. элементы в множестве должны быть
# уникальны, они автоматически удаляют дубликаты

# Словари
# Словари — неупорядоченные наборы пар ключ-значение.
# Они используются, когда нужно сопоставить каждому из ключей значение и иметь возможность быстро получать доступ к
# значению, зная ключ. В других языках словари обычно называются map, hash или object. Словари оптимизированы для
# извлечения данных. Чтобы извлечь значение, нужно знать ключ.
# Словарь объявляется парами элементов в форме ключ:значение, заключенными в фигурные скобки:
_dict = {a: "значение ключа а", b: "два", c: 3.0}
# Значение может быть любого типа, а вот ключ — только неизменяемого.
# Мы используем ключ, чтобы получить соответствующее ему значение. Но не наоборот:
print(_dict[a])

# Неизменяемые типы данных - числа, строки, кортежи
# Изменяемые типы данных - списки, словари, множества