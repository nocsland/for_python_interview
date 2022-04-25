2. Как выполняется интерполяция(форматирование) строк?
Без импорта класса Template есть три способа интерполяции строк:

name = 'Chris'

# 1. f strings
print(f'Hello {name}')

# 2. % operator
print('Hey %s' % (name))

# 3. format
print(
 "My name is {}".format((name))
)