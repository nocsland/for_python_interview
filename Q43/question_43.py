# 43. В чем разница между pass, continue и break?
#
# Заглушка pass означает «ничего не делать». Обычно мы используем эту функцию, потому что Python не позволяет создавать
# класс, функцию или оператор if без кода внутри.
#
# В приведенном ниже примере вылетит ошибка, если внутри i > 3 не будет кода, поэтому мы используем pass:

a = [1, 2, 3, 4, 5]
for i in a:
    if i > 3:
        pass
    print(i)
# => 1
# => 2
# => 3
# => 4
# => 5

# continue отправляет вас к следующему элементу в цикле, останавливая выполнение для текущего элемента. Таким образом,
# print(i) никогда не получает значения i < 3:

for i in a:
    if i < 3:
        continue
    print(i)
# => 3
# => 4
# => 5

# break прерывает цикл, и последовательность больше не повторяется. Таким образом, на цифре 3 цикл прерывается, а этот и
# следующие элементы не печатаются:

for i in a:
    if i == 3:
        break
    print(i)
# => 1
# => 2