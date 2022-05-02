number = input()
if len(number) >= 8 and number.isdigit():
    print("*" * (len(number) - 4) + number[-4:])
else:
    print("Ошибка")