# 9. Объясните, как работает функция map
#
# Она возвращает объект (итератор), который перебирает значения, применяя функцию к каждому элементу. В случае
# необходимости объект можно преобразовать в список:

def add_three(x):
    return x + 3


li = [1, 2, 3]
print(list(map(add_three, li)))

# => [4, 5, 6]
# Здесь к каждому элементу в списке мы добавляем число 3.

my_list = [1, 2, 41, 58, 64, 25]


# Возводим в квадрат x
def my_func(x):
    return x ** 2


# Еще один способ вывести итератор в виде списка
print([i for i in map(my_func, my_list)])
