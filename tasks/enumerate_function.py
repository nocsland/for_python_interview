# Напишите программу, которая делит введённое пользователем предложение на слова. Учтите, что между словами может быть
# больше одного пробела. После этого программа должна вывести на экран слова вместе с порядковыми номерами в
# предложении. Номера должны начинаться с единицы.

data_in = input().split()
for idx, el in enumerate(data_in, 1):
    print(idx, el)