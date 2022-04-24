number = int(input())
if number > 5:
    print("Введенное число больше 5")
elif number == 5:
    print("Равно 5")

else:
    print('Число меньше 5')

# Можно и в одну строку
if number == 10: print("Число равно 10")

# Вложенные условия
number = int(input())
if number > 10:
    if number < 20:
        print("Число больше 10, но меньше 20")

# Аналог через логические операторы
number = int(input())
if number > 10 and number < 20:
    print("Число больше 10, но меньше 20")

# Можно и так
number = int(input())
if 10 < number < 20:
    print("Число больше 10, но меньше 20")


