# 5. Объясните функцию range
#
# Range генерирует список целых чисел. Ее можно использовать тремя способами.
#
# Функция принимает от одного до трех аргументов. Обратите внимание, что я завернул каждый пример в список, чтобы видеть
# генерируемые значения.
#
# range(stop) — генерирует целые числа от 0 до целого числа stop:

def range_one():
    return [i for i in range(10)]


# результат => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range_one())


# range(start, stop) — генерирует целые числа от start до stop:

def range_two():
    return [i for i in range(2, 10)]


# результат => [2, 3, 4, 5, 6, 7, 8, 9]
print(range_two())


# range(start, stop, step) — генерирует целые числа от start до stop с интервалами step:

def range_three():
    return [i for i in range(2, 10, 2)]


# => [2, 4, 6, 8]
print(range_three())

# есть еще один способ:

print(list(range(2, 10, 2)))
# => [2, 4, 6, 8]
