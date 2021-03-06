# Написать программу, в которой предлагается угадать загаданное компьютером целое случайное число от 0 до 10 за три
#  попытки.

# Первым делом присвойте переменной number значение, полученной с помощью функции randint из модуля random.

# После этого, программа должна дать три попытки на то, чтобы пользователь угадал число number. Для этого, с помощью
# цикла for и функции range надо создать цикл на три итерации.

# В каждой итерации программа должна запрашивать у пользователя число. Если загаданное число меньше, чем число, которое
# ввел пользователь, программа должна вывести на экран: "Загаданное число меньше"
# Если загаданное число больше, чем число, которое ввел пользователь, программа должна вывести на экран текст
# "Загаданное число больше"

# Если пользователь угадал, на экран должно быть выведено "Вы выиграли" Цикл при этом должен закончится с помощью break.

# Если за три попытки пользователь так и не угадал числа, программа должна вывести на экран текст "Вы проиграли"

from random import randint

number = randint(0, 10)
for i in range(1, 4):
    user_number = int(input(f"Попытка {i} "))
    if user_number < number:
        print("Загаданное число больше")
    elif user_number > number:
        print("Загаданное число меньше")
    elif user_number == number:
        print("Вы выиграли")
        break
else:
    print("Вы проиграли")
