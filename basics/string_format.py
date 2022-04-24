# Вариант с конкатенацией
a = 10
b = 3
c = a + b
result = str(a) + "+" + str(b) + "=" + str(c)
print(result)

# C - форматирование
a = 10
b = 3
c = a + b
result = "%d+%d=%d" % (a, b, c)
print(result)

# Функция format
a = 10
b = 3
c = a + b
print("{}+{}={}".format(a, b, c))

# Можно указать произвольный порядок подстановки аргументов, указав индекс внутри фигурных скобок
a = 10
b = 3
c = a + b
print("{1}+{0}={2}".format(a, b, c))

# f-строка
a = 10
b = 22
result = f'{a} + {b} = {a + b}'
print(result)
