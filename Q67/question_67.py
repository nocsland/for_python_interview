class ToyClass:

    def instancemethod(self):
        """Создаем метод экземпляра класса"""
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        """Создаем метод класса"""
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        """Создаем статический метод"""
        return 'static method called'


# Создаем экземпляр класса ToyClass
my_object = ToyClass()
# Вызываем метод экземляра класса *
print(my_object.instancemethod())
# Вызываем метод класса *
print(my_object.classmethod())
# Вызываем статический метод *
print(my_object.staticmethod())
# * обернуто в print для наглядности
