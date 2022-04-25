# 60. Что такое декоратор?
#
# Декоратор позволяет добавить новую функциональность к существующей функции. Это делается следующим образом. Функция
# передается декоратору, а он выполняет и существующий, и дополнительный код.

def decorator(func):
    '''Основная функция'''
    print('декоратор')

    def wrapper():
        print('-- до функции', func.__name__)
        func()
        print('-- после функции', func.__name__)

    return wrapper


@decorator
def wrapped():
    print('--- обернутая функция')


print('- старт программы...')
wrapped()
print('- конец программы')

# Вывод в консоль

# декоратор
# - старт программы...
# -- до функции wrapped
# --- обернутая функция
# -- после функции wrapped
# - конец программы
