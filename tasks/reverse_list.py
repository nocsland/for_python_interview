# Получить от пользователя текст, разбить по словам и вывести полученные слова в обратном порядке
my_list = input().split()
reverse_list = my_list[::-1]
print(' '.join(reverse_list))

# Лаконичный вариант той же задачи
print(' '.join(input().split()[::-1]))