# 46. Проверьте, что в строке только числа
#
# Можно использовать isnumeric() или isdigit():

print('123a'.isnumeric())
# => False

print('123'.isnumeric())
# => True

print("123456".isdigit())

print("123a123".isdigit())
