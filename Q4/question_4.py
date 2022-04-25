# Напишем декоратор, который записывает в журнал вызовы другой функции.

# Напишите функцию декоратора. В качестве аргумента он принимает функцию func. Декоратор определяет функцию
# log_function_called, которая вызывает func() и выполняет некоторый код print(f'{func} called.'). Затем возвращает
# определенную им функцию:

def logging(func):
    def log_function_called():
        print(f'{func} called.')
        func()

    return log_function_called


# Напишем другие функции, к которым добавим декоратор (потом, не сейчас):

def my_name():
    print('chris')


def friends_name():
    print('naruto')


my_name()
friends_name()


# => chris
# => naruto

# Теперь добавим декоратор к ним обоим:

@logging
def my_name():
    print('chris')


@logging
def friends_name():
    print('naruto')


my_name()
friends_name()

# => <function my_name at 0x10fca5a60> called.
# => chris
# => <function friends_name at 0x10fca5f28> called.
# => naruto

# Теперь легко добавить ведение журнала в любую функцию, которую мы пишем. Достаточно написать перед ней @logging.
