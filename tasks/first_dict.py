# Написать программу, в которой переменной first_dict присвоен словарь. В этом словаре должно быть три ключа:
#
# Первый ключ должен быть строкой, а его значение должно быть целым числом. Значение строки и числа могут быть любыми.
#
# Второй ключ должен быть любым кортежем, а его значение — любым списком.
#
# Третий ключ должен быть числом с плавающей запятой, а его значение — любой строкой
#
# Программа должна вывести на экран значение каждого из ключей.

first_dict = {
    'первый': 1,
    (1, 2): [1, 2],
    3.14: "Число ПИ"
}

print(first_dict)
