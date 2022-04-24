# 38. Как объединить два списка в список кортежей?

# Для объединения в список кортежей можно использовать функцию zip, причем не только двух, но трех и более списков.

a = ['a', 'b', 'c']
b = [1, 2, 3]

print([(k, v) for k, v in zip(a, b)])
# => [('a', 1), ('b', 2), ('c', 3)]
